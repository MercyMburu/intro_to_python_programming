import re
text='''hell
This is a sentence
1234
test45
this is a number 5
'''
pattern="come"
match=re.search(pattern,text)
print(match)

text="We are learning python"
pattern=r'^We'
matches=re.findall(pattern,text)
print(matches)

text="We are learning python"
pattern= r'python$'
matches=re.findall(pattern,text)
print(matches) 

text=f"""
My email is user@example.com, or contact@domain.com"""

pattern=r"\b[a-z]+@+[a-z]+\.com\b"
match=re.findall(pattern,text)
print(match)



