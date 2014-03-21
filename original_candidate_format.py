#!/usr/bin/python
###### author : Akshay Minocha ###############
###### mailto: akshayminocha5@gmail.com ######
# Returns a list of words ( specify the dictionary and enjoy a disambiguated hashtag )
# input here is coming from easy_tokenize2.py
#which means that it is still not in the ambiguated format
# the output of this script will be in the format
#each token is represented as  ^original/candidate1/candidate2$
import pickle
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
  x=line[1:-1]   # ^ and $ symbols are ommitted
  tokens=x.split("/")
  return tokens


def separate_word_punctuator(word):
    x=set(string.punctuation)
    words=[]
    for i in range(0,len(word)):
      if i in x:
        words=[word[:i],word[i:]]
        break
    if len(words)==0:
      return [word]
    else:
      return words
    
def main():
    sentences = sys.stdin.readlines()
    for sentence in sentences:
        x=sentence.split()
        dl=[]
        for i in x:
          dl+=[[i,i]]
        
        print " ".join(ambiguated_output(dl))


if __name__=="__main__":
    main()
