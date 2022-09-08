#!/usr/bin/env python

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int]
    malformed = 0 #create a counter for malformed lines
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3 or fieldN == 10 or fieldN == 11: #check that we have 3-9 or 12 columns, but not 10 or 11 columns 
            print(f"Line {i} appears malformed", file=sys.stderr) 
            continue 
           
        try: 
            if fieldN >= 9: #make sure the file we're working with has at least 9 columns
                rgb = fields [8] #pull out the 9th column
                rgb_list = rgb.split(',') #convert the 9th column into a list 
                for i, item in enumerate(rgb_list): 
                    rgb_list[i] = int(item) #makes it the items in our list an integer
                fields[8] = rgb_list  #replace the 9th column with our list 
        
            #make sure we only do this for files that have 12 columns 
            if fieldN == 12:
                blockSizes = fields[10].rstrip(",").split(",") #strip the extra comma from blockSizes (column11) and convert column 11 into a list
                blockStarts = fields[11]
            #convert items within blockSizes and blockStarts into integers 
            for i, item in enumerate(blockSizes): 
                blockSizes[i] = int(item) #makes the items in our list an integer
            fields[10] = blockSizes #replace the 10th column with our converted list 
            for i, item in enumerate(blockStarts): 
                blockStarts[i] = int(item) #makes the items in our list an integer
            fields[11] = blockStarts
            #check that blockSizes and blockStarts length matches blockCount (column10)
                #pull out the value of blockCount
                #check that length of blockSizes and blockStarts == blockCount 
            blockCount = int(fields[9])
            if len(blockStarts) != blockCount: 
                malformed += 1 
            if len(blockSizes) != blockCount:
                malformed += 1
            fields[9] = blockCount #replace the 10th column, with its integer version 
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
            #mike is converting all of the columns to the correct data type 
        try:    
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)      
    fs.close()
    return bed
        
if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
