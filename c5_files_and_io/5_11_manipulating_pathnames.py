# manipulating pathnames
import os 

path = '/root/data.csv'

print(os.path.basename(path))

# Get the directory name
print(os.path.dirname(path))

# Join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))

# Expand the users home directory
path = 'Data/data.csv'
print(os.path.expanduser(path))

# split the file extension
print(os.path.split(path))

