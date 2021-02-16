# Making temporary files and directories

# after usage of folder we want to delete

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # seek back to the begining and read the data
    f.seek(0)
    data = f.read()
    print(data)
    # temporary file is destroyed
    # f = TemporaryFile('w+t')
    # f.close()

# with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
#     ...

# use namedtemporaryFile()
from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is: ', f.name)

# delete=false keyword argument

with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is ', f.name)

# to make a temporary directory,use tempfile.Temporarydirectory()
from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('dirname is: ', dirname)
# direcory and all contents destroyed

import tempfile

print(tempfile.mkstemp())
print(tempfile.mkdtemp())

print(tempfile.gettempdir())

f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
print(f.name)
