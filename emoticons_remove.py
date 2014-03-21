#!/usr/bin/python
##########Author:Akshay Minocha | ksnmi #########
##########mailto:akshayminocha5[at]gmail.com#####

import sys
import pickle

#pickle because the list is too small. This is a universal list independent of the language

def ambiguated_output(list_of_tokens):
  l=[]
  for word in list_of_tokens:    # list of tokens is the double list
    s='^'
    j='/'.join(word)
    s=s+j+'$'
    l+=[s]
  return l
    
   

def main():
  emo=pickle.load(open("emoticons_pickle"))
  lines=sys.stdin.readlines()
  for line in lines:
    x=[]
    for i in line.split():
      if i in emo:
        #x+=[[i,'<smiley>']]
        continue
      else:
        #x+=[[i,i]]
        x+=[i]
    #new_content=ambiguated_output(x)
    #print " ".join(new_content)
    new_content=" ".join(x)
    print new_content
  
if __name__=="__main__":
  main()
