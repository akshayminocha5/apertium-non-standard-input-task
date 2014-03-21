#!/usr/bin/python

import sys
import string
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

def disambiguated_output(word):
  x=word[1:-1]   # ^ and $ symbols are ommitted
  tokens=x.split("/")   
  return tokens

def main():
  some_known={"i":"I","i'd":"I'd","i've":"I've","i'm":"I'm","i'll":"I'll"}
  s=sys.stdin.readlines()
  for line in s:
    dl=[]
    x=line.split()
    for i in x:
      dl+=[disambiguated_output(i)]
    index=[]
    flag=0
    for i in range(0,len(dl)):
      if i==0:
        if dl[i][-1][0]!=dl[i][-1][0].capitalize():           # not capital
          index+=[i]
      if dl[i][-1].lower() in some_known:
        index+=[i]
        if flag==1:
          flag=0
        continue
      if flag==1:
        flag=0
        if dl[i][-1][0] in string.punctuation:
          flag=1
          continue
        if dl[i][-1][0]!=dl[-1][0].capitalize():
          index+=[i]
          continue
      if dl[i][-1][0] in string.punctuation:
        flag=1
    new=[]
    for i in range(0,len(dl)):
      if i in index:
        w=dl[i][-1].capitalize()
        new+=[dl[i]+[w]]
      else:
        new+=[dl[i]+[dl[i][-1]]]
    print " ".join(ambiguated_output(new))


if __name__=="__main__":
  main()
