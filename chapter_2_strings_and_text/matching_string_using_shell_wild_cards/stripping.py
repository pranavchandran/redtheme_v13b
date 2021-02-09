# white space strpping
s = '    hello world \n'
print(s.strip())

print(s.rstrip())
print(s.lstrip())

# charachter stripping
t = '-------hello======='
print(t.lstrip('-'))
print(t.rstrip('.='))
print(s.rstrip())
print(t.strip('-='))

# stripping does not apply to any text in the middle
# of a string
s = '   hello       world   \n'
s = s.strip()
print(s)

# if u want to do anything in the innerspace use replace()
print(s.replace('  ', ''))

# Sanitizing and cleaning up text



