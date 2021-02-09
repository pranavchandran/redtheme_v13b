from collections import namedtuple
# reformatting text to a fixed number of columns
s = 'Look into my eyes, look into my eyes, the eyes, the eyes,\
    the eyes, not around the eyes,dont look around the eyes\
    look into my eyes, you are under'

import textwrap
# print(textwrap.fill(s, 40))

# print(textwrap.fill(s, 40, initial_indent='    '))

print(textwrap.fill(s, 40, subsequent_indent='    '))

# on the subject of terminal size
import os

print(os.get_terminal_size().columns)

# using Htmlescape function
s = 'Elements are written as "<tag>text</tag>"'
import html
print(s)

print(html.escape(s))

# disable escaping of quotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeno'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy&quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
modified_ = p.unescape(s)
print(modified_)

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))

text = 'foo = s3 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
        ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# scanner = master_pat.scanner('foo'=42)
# print(scanner.match())

Token = namedtuple('Token', ['type','value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

PRINT = r'(P<PRINT>print)'
NAME = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9])'
master_patb = re.compile('|'.join([PRINT, NAME]))
for tok in generate_tokens(master_patb, 'printer'):
    print(tok)

# for tok in generate_tokens(master_pat, 'foo = 42'):
#     print(tok)

# scanner = master_pat.scanner('foo = 42')
# print(scanner.match())

# print(_.lastgroup, _.group())
# print(_.lastgroup)

# tokens = (tok for tok in generate_tokens(master_pat,text) if tok.type!= 'WS')
# for tok in tokens:
#     print(tok)

# LT = r'(?P<LT><)'
# LE = r'(?P<LE><=)'
# EQ = r'(?P<EQ>=)'

# a_master_pat = re.compile('|'.join([LT, LE, EQ]))
# print(a_master_pat)

# PRINT = r'(P<PRINT>print)'
# NAME = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9])'
# master_patb = re.compile('|'.join([PRINT, NAME]))
# for tok in generate_tokens(master_patb, 'printer'):
#     print(tok)


