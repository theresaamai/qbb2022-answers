# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
filename = "random_snippet.vcf"
for line in open(filename):
    print(line.strip('\r\n'))
for i, line in enumerate(open(filename)):
    if i == 0:
        print(line.strip('\r\n'))
import sys
filename = sys.argv[1:]
if len(sys.argv) >2:
    n_lines = int(sys.argv[2])
else:
    n_lines = 10
counter = 0
for line in open((filename)):
    if counter < n_lines and not line.startswith('#'):
        print(line.strip ('\r\n\ '))
        counter = counter + 1
    counter = filename
for line in open((filename)):
    if counter < n_lines:
        print(line.strip('\r\n'))

# You appear to have a good start here, but need a little better understanding
# for using lists. First off, I think it would be really helpful to keep your
# scripts cleaned up. This script clearly has several different ideas being 
# implemented. You want to get right of anything that isn't actually working
# towards your goal. You also want to add comments, as this will help you
# organize your thoughts and think through each step. It will also make it much
# easier for other reads (and you should you take a break and come back to your
# script) to read and understand what you were trying to do. It's also easier
# to read if you include blank lines to break up your script into blocks of
# code working on the same task. The list "sys.argv" has an entry for each thing
# following "python" when you call the script. Item zero is the name of your
# script, item 1 is the filename you pass, item 2 is the number of lines, if you
# include that when you call your script. So your line should be
# "filename = sys.argv[1]", since you only want a single item from the list.
# Getting the number of lines is spot on. Your two different for loops both are
# a little off, but put together are correct. You should not have "counter = filename"
# since your counter is an integer that you are using to keep track of the number
# of lines you've read from the file. In the second for loop, you aren't keeping
# track of the number of lines. PUt them together and you've got a functional
# "head" tool. In order to make the "tail" tool, you need to be able to load all
# of the lines, keeping them in a list. Then you need to only print out the last
# "n_lines" number of items from that list. You're on the right track, but have 
# got a few more steps to take. Please reach out to a TA or instructor if you
# need help with any of this. Keep it up, you're doing fine. - Mike

