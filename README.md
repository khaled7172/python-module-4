# python-module-4
*This project has been created as part of the 42 curriculum by khhammou*

## Description
print() automatically adds a new line and flushes stdout
sys.stdout.write() is lower level, must manually add \n

using with statement to open files:
with open("filename", "r") as file:
    data = file.read()
Automatically closes the file when the block ends, even if an exception occurs
Modes available to pick inside a file:
"r" -> read mode, reads the contents of a file, File must exist, cursor starts at beginning, you can only read not write
If file doesn't exist -> FileNotFoundError
"w" Write mode, if file exists, it is erased(truncated)
if file does not exist, it is created
you cannot read
when you write new content, old content is removed
"a" Append mode, add contents to end of a file
If file exists -> content added to end
if file doesnt exist -> it is created
cursor starts at end of file
use .write in this mode like "w"
"r+" Read + Write mode, File must exist
cursor starts at beginning, you can read & write
you may need cursor movement:
file.seek(0) because the cursor moves as you read/write
file.seek(0) moves cursor back to beginning of the file (byte position 0)
file.seek(len(file) + 1) moves cursor to position at end of file
"w+" Write + Read mode, Read and write but overwrite file first
if file exists, erased
if file doesn't exist ->created
Allows reading and writing
f.write()
f.seek(0)
print(f.read())# to read from the start
"a+" Append + read
writes always go to end of file
file created if missing
cursor initially at end
"rb" reads binary data like images, videos, pdfs, executables
"wb" write binary
"ab" append binary
"t" text mode is default
well actually default is rt which treats file as text and outputs as string
OSError like No such file or directory
permission denied (attempting to write into a read only file)
no space left on device
Invalid argument passing invalid argument during file operations

Go crazy:
autopep8 --in-place --aggressive --aggressive ft_garden_management.py
### Instructions

You run this code by doing python3 file_name.py

## Resources

The internet

## AI Usage

Testing my code with test cases and helping me find syntax errors