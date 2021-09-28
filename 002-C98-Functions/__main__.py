# File swpper
# Made by somePythonProgrammer as a WhiteHat project.

# read the files
global file1_contents,file2_contents
with open('file_1.txt') as f1, open('file_2.txt') as f2:
    file1_contents = f1.read()
    file2_contents = f2.read()

# write the files, swapping them.
open('file_1.txt','w').write(file2_contents)
open('file_2.txt','w').write(file1_contents)

print('Successfully swapped the two files!')
print('file 1: {}, file 2: {}!'.format(file1_contents,file2_contents))
