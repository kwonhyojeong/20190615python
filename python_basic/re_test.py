import re

p = re.compile('[a-z]+')

m = p.finditer("3.7.3pytHon")
for r in m:
    print(r)