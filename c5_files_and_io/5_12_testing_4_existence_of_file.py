# Testing for the Existence of a file
# Need to text whether or not a file or directory exists

# os.path 

import os

print(os.path.exists('/etc/passwd'))
print(os.path.exists('/root/data.csv'))
print(os.path.exists('/root/not_exist.csv'))

# what kind of file it might be
print(os.path.isfile('/etc/passwd'))

# is a directory
print(os.path.isdir('/etc/passwd'))

# is a symbolic link
print(os.path.islink('/root/local/bin/python3'))

# Get the file linked to
print(os.path.realpath('/usr/local/bin/python3'))

print(os.path.getsize('/etc/passwd'))

# print(os.path.getsize('./hello.txt'))
print(os.path.getmtime('/etc/passwd'))

import time

print(time.ctime(os.path.getmtime('/etc/passwd')))








