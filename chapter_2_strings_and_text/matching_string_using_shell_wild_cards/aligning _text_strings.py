# Aligning of strings the ljust(), rjust() and center()

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.rjust(20, '='))
print(text.center(20,'*'))

# format() function can also be used to align things
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

# fill the charachter other than a space
print(format(text, '=>20'))
print(format(text, '=>20'))
print(format(text, '*^20s'))

# These format codes can also be used in the format() method when formatting
# multiple values.

print('{:>10s}{:>10s}'.format('Hello', 'World'))

x = 1.2345
print(format(x, '>20'))

print(format(x, '^10.2f'))

print('%-20s'%text)
print('%20s'%text)










