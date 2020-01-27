import re

s = input()
templ = input()
found = re.search(templ.replace('@', '.').replace('(', "\(").replace(')', "\)"), s)

print( found.start() if found else -1 )
