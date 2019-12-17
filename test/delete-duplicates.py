from collections import Counter
import sys

lines = open(sys.argv[1], 'r').readlines()

dic = Counter()
for l in lines :
    l = l.replace('&amp;', 'and')
    l = l.replace('’', '\'')
    l = l.replace('‘', '\"')
    l = l.replace('”', '\"')
    dic[l.lower()] += 1

w = open(sys.argv[2], 'w')

for word in dic.keys() :
    w.write(word)

w.close()
