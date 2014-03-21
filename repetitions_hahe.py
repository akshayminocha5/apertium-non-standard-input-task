#!/usr/bin/python
import sys 
d=["ha","he","ho"]

for line in sys.stdin.readlines():
  new_line=[]
  temp=""
  flag=0
  for i in line.split():
    if i.lower() in d:
      flag=1
      temp+=i 
      continue
    if flag==1:
      new_line+=[temp]
      temp=""
      flag=0
    new_line+=[i]
  if len(temp)!=0:
    new_line+=[temp]
  print " ".join(new_line)
