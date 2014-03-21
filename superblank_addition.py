#!/usr/bin/python

import sys
import re

def replace_hashtags(line):
  flag=0
  new=""
  for i in line:
    if i=="#":
      new+="<htxy"
      flag=1
      continue
    if flag==1:
      if i.isalpha():
        new+=i
        continue
      else:
        new+=">"
        flag=0
        new+=i
        continue
    if flag==0:
      new+=i
  return new 
  

def main():
  s=sys.stdin.readlines()
  for line in s:
    line=re.sub('/','<bbxyzzy>',line)
    line=replace_hashtags(line)
    print line[:-1]
    
  

if __name__=="__main__":
  main()
