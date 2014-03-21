#!/usr/bin/python
########Author Akshay Minocha ( ksnmi | minocha )##############
########mailto:akshayminocha5@gmail.com########################

import pickle
#substitution list
import sys
temp=open("temp_language").read().split()[0]
d=pickle.load(open("abbr_dict_"+temp))
import re

def main():
  global d
  text=sys.stdin.readlines()
  for i in text:
    sent=[]
    x=i.split()
    for j in x:
      if j.lower() in d:
        sent+=[d[j.lower()]]    # substituting the word here
      else:
        sent+=[j]
    print " ".join(sent)
  
if __name__=="__main__":
  main()
