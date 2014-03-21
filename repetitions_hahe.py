#!/usr/bin/python
import sys 
import pickle
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


def main():
  lang=open("temp_language").read().split()[0]
  d=pickle.load(open("hahe_"+lang))
  
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
    print " ".join(ambiguated_output(new_line))


if __name__=="__main__":
  main()
