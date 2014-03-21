#!/usr/bin/python
import sys
import re
def ambiguated_output(list_of_tokens):
  dl=[]
  for word_token in list_of_tokens:
    s='^'
    s+=word_token[0]+"/"
    l=[]
    for word in word_token[1:]:
      if word in l:
        continue
      else:
        l+=[word]
    j='/'.join(l)
    s=s+j+'$'
    dl+=[s]
  return dl

def disambiguated_output(line):
  x=line[1:-1]   # ^ and $ symbols are ommitted   not liine.. this is per token
  tokens=x.split("/")
  return tokens

def main():
  s=sys.stdin.readlines()
  for line in s:
    x=[]
    tokens=line.split()
    for i in tokens:
      x+=[disambiguated_output(i)[-1]]
    new_line=" ".join(x)
    new_line=re.sub('<bbxyzzy>','/',new_line)
    x=[]
    for word in new_line.split():
      if word[:5]=="<htxy":
        x+=["#"+word[5:-1]]
        continue
      x+=[word]
    print " ".join(x)
if __name__=="__main__":
  main()
