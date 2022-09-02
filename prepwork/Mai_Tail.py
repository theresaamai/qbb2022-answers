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



