# QBB2022 - Day 2 - Homework Exercises Submission 
#!/usr/bin/env python3

import sys #package that allows us to read in input from the command file (ex. vcf files)

def parse_vcf(fname): #defining a function called parse_vcf, this takes an argument called "fname"
    vcf = [] #creating an empty list named vcf to store the vcf information into
    info_description = {} #creating a dictionary 
    info_type = {} #creating a dictionary
    format_description = {} #creating a dictionary
    type_map = { # allows us to use information from the header to tell python what data types to expect
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0 #initializing the variable to count the number of malformed vcf files 
	#trying to open a vcf file 
    try: 
        fs = open(fname) #creating a variable called fs, which is storing the opened vcf file 
    except: #if the above doesn't work out, then we will print the below 
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

    for h, line in enumerate(fs): #loop through every line in the vcf file, keeping track of the line number
        if line.startswith("#"): # for header lines only 
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: #if we are not in a header line, do this: 
            try: # Try doing all of this
                #fields is a list that stores the info in one line of the vcf
                fields = line.rstrip().split("\t") #splits each line on a tab character, so that every column is an item in                 the list now named "fields"
                fields[1] = int(fields[1]) #convert the SNP position into an integer, remember if this doesnt work, we will automatically go to the "except block"
                if fields[5] != ".": #if this quality column is not a dot, then convert it into a float(decimal). if the QUAL column is not empty (i.e., it has a decimal in it that represents the SNP quality)
                    fields[5] = float(fields[5]) #then forcibly convert it into a decimal
                info = {} #create a dictionary to store the information in the info column -lines 76-83 are going to be about parsing the INFO column 
                #we want the info dictionary to look like this: {"AC" : 91, 
                                                                #"AN" : 5096}
                for entry in fields[7].split(";"): #the list looks like: ["AC-91", "AC=5096", ..., "NS=2548]
                #the first entry we are working with is "AC=91"
                    temp = entry.split("=") #temp is a list. if we're working with "AC=91", temp = [AC, "91"]
                    if len(temp) == 1: #if there's only one item in the temp list ("AC="), what we want to do is update the dictionary so that we know that AC has no value for this SNP
                        info[temp[0]] = None # we are adding "AC" to the dictionary. temp[0]="AC"
                        #dictionaries have keys and values. You can add info to a dictionary by doing dict_name[new key] = new value Ex. info["AC"] = 91 
                    else: #otherwise, the INFO field is not empty and we're good 
                        name, value = temp # temp is a list, that looks like ["AC", "91"], we want to add these to the dictionary, this code is a way of saying that there are 2 elements in the list, and we want to label them. so name = "AC", value = "91". Steph's version: name = temp[0] value = temp[1]
                        #in these next 2 lines, we are converting the data in each entry to its correct data type. this data type was specified in the header section that we parsed above 
                        Type = info_type[name] #here we are getting the name of the data type that the entry should be. Ex. Type = info_type["AC"]. info_type is a dcitionary we made in the header parsing section that tells us what data type that entry should be
                        info[name] = type_map[Type](value) #here, we're getting the python function for converting the entry to the correct data type. Ex. For AC: info["AC"] = type_mapp["Integer"]["91"]. This will turn into info["AC"] = integer("91")
                fields[7] = info #Replace the 8th of the "fields" list (i.e., the list of columns in this line with the "info" dictionary that we just made) fields[7] used to be: "AC=91, AN=5096....", but now it is {"AC" : 91, 
                                                                                                #"AN" : 5096}
                if len(fields) > 8: #if we still have more columns after the info column (the 7th column), then we still have more stuff to do 
                #example of fields[8] (the FORMAT column): GT:DP:AF:BG:RU
                    fields[8] = fields[8].split(":") #we are splitting the format column by ":"
                    #Ex: "GT:DP:AF:BG:RU" -> ["GT", "DP", "AF", "BG","RU"]
                    if len(fields[8]) > 1: #if there are multiple things in the FORMAT column, we have to deal with all of them individually: 
                        #FORMAT: GT:DP. HG00097: 0|0:0.3
                        for i in range(9, len(fields)): #this goes through all the genotype columns after the FORMAT column -> For us, this is range(9, 2513)
                            fields[i] = fields[i].split(':') #split each genotype column along a ":" 
                            #0|0:0.3 -> [0|0, "0.3"]
                            #our "fields" list turns into: [0|0:0.3, "1|1:0.5"] -> [["0|0", "0.3"]], ["1|1], .. "0.5""]]
                    else: #if the genotypes don't have more than one value in them, then we're good we just do this:
                        fields[8] = fields[8][0] # fields[8] is ["GT"]. this will make fields[8] = "GT". we set the value of fields[8] to be "GT" (or, the first item in the fields[8] list)
                vcf.append(fields) #we finished reformatting/cleaning all of the columns; now we add this line to our VCF list. The list is storing all the information from the VCF file. 
                #fields is a list that contains the information for the current line that we're working on. 
            except: #if anything in the try block fails, then:
                malformed += 1 #increment the "malformed" variable by 1 
            #these next three lines are modifying the first line of the vcf list to match information from the header 
    vcf[0][7] = info_description #
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    #if there were any malformed lines, we're going to print out the number of lines so the user knows 
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
        #at the very end of running the function, return the vcf list. give me the data back. 
    return vcf
2. There are 100 unlabeled records 


