import re
# not greedy
comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'
text2 = '''/* this is a multiline comment */'''
ans1 = comment.findall(text1)
print(ans1)

ans2 = comment.findall(text2)
print(ans2)

# Adding support fornewlines
comment_v0 = re.compile(r'/\*((?:.|\n)*?)\*/')
ansv0_1 = comment_v0.findall(text2)
print(ansv0_1)

comment_v1 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
ansv1 = comment_v1.findall(text2)
print(ansv1)




