line = 'asdf  fjdf;  afed,fjek,asdf,  foo'
import re
new_line = re.split(r'[;,\s]\s*', line)
print(new_line)

# Example what happens here
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']

print(values)
print(delimiters)
new_j = ''.join(v+d for v,d in zip(values, delimiters))
print(new_j)

new_re = re.split(r'(?:,|;|\s)\s*', line)
print(new_re)

