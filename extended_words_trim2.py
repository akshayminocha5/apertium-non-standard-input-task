#!/usr/bin/python
#This is the script which works for the text written in English or INTENDED to be written in English. This text may or may not be grammatically correct. Our aim is to normalise the repititions in the word.
########Author Akshay Minocha ( ksnmi | minocha )##############
########mailto:akshayminocha5@gmail.com########################
import sys
import itertools
import string
import pickle
# this script takes in from stdin normal input.. not line per token format

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
 
def separate_word_punctuator(word):
    x=set(string.punctuation)
    words=[]
    for i in range(0,len(word)):
      if word[i] in x:
        words=[word[:i],word[i:]]
        break
    if len(words)==0:
      return [word]
    else:
      return words
 
 
def check_repitition(word):
  # returns 1 if the number of characters is >=3 
  # returns 0 if it thinks the word has non repititive characters (otherwise)
  punc=string.punctuation
  if word[0] in punc:
    return 0
  flag_count=0
  flag=''
  for i in range(0,len(word)):
    if i==0:
      flag=word[0]
      flag_count=1
      continue
    else:
      if word[i]==flag:
        if word[i] in punc:
          flag_count=0
        flag_count+=1
        if flag_count>2:
          return 1
      else:
        flag=word[i]
        flag_count=1
  return 0
 
def generate_variations(word):
  flag_count=0
  flag=''
  temp=word[0]
  list_of_rep=[]
  for i in range(0,len(word)):
    if i==0:
      flag=word[0]
      flag_count=1
      continue
    else:
      if word[i]==flag:
        flag_count+=1
        if flag_count>3:
          continue
        if flag_count>2:
          list_of_rep+=[len(temp)-2]
          continue
        else:
          temp+=word[i]
      else:
        flag=word[i]
        flag_count=1
        temp+=word[i]
  return (temp,list_of_rep)
 
def generate_all_variations(tuple_info):
  #0th -> original candiate normalised( 1stage )
  # all repititions which are detected earlier ( have either 1 or 2 repititions as the final output of this script)
  length=len(tuple_info[1])  # all the index positions where the repititions > 3 were made
  all_words=[]
  list_of_index=tuple_info[1]
  word=tuple_info[0]
  for x in map(''.join, itertools.product('01', repeat=length)):
    #print word
    temp=word[:list_of_index[0]+1]
     
    flag=list_of_index[0]+2
    for i in range(0,len(x)):
      if x[i]=="1":
        temp+=word[list_of_index[i]]
      if i+1<len(x):
        temp+=word[flag:list_of_index[i+1]+1]
        flag=list_of_index[i+1]+2
      else:
        temp+=word[flag:]
    all_words+=[temp]
  return all_words
 
def main():
  #wordlist=pickle.load(open("wordlist_dic"))
  input1=sys.stdin.readlines()
  #output format of the first stage will be 
  #^original_word/candidate1/candidate2/candidate3 and so on$
  list_of_tokens=[]
  lang=open("temp_language").read().split()[0]
  english_wordlist=pickle.load(open("wordlist_dic_"+lang))
   
  for line in input1:
    list_of_tokens=line.split()   #each line has multiple words.. all are being added to list of tokens
    double_list_sentence=[]
    for j in list_of_tokens:
      i=disambiguated_output(j)[-1]    # as the dis amb is per token
      if i=="RT" or i[0]=="@" or i[0]=="#" or i in string.punctuation:
        x=[i,i]
        double_list_sentence+=[x]
        continue
      if check_repitition(i)==1:
        sep=separate_word_punctuator(i)
        if len(sep)==1:
          gv=generate_variations(i)
          x=[i]
          for j in generate_all_variations(gv):
            x+=[j]
        else:
          gv1=generate_variations(sep[0])
          x=[i+sep[1]]
          for j in generate_all_variations(gv1):
            x+=[j+sep[1]]
      else:
        x=[i,i]
      double_list_sentence+=[x]
    #print double_list_sentence  we need to do the processing line by line to avoid large chunks ( big file ~> RAM)
    #sentence=[]
    #print double_list_sentence
    #sys.exit(0)
    sentence=[]
    for j in double_list_sentence:
      chosen_word=[]
      for k in j:
        sep=separate_word_punctuator(k)
        if len(sep)==1:
          if k.lower() in english_wordlist:
            chosen_word=[k]
            break
        if len(sep)==2:
          if sep[0].lower() in english_wordlist:
            chosen_word=[sep[0]+sep[1]]
            break
      if len(chosen_word)==0:
        chosen_word=[j[0]]   # original candidate
      sentence+=[chosen_word[0]]
    #print len(sentence)
    #print len(list_of_tokens)
    new_list=[]
    for el in range(0,len(list_of_tokens)):
      temp=disambiguated_output(list_of_tokens[el])
      temp+=[sentence[el]]
      new_list+=[temp]
    #non_re_sentence=" ".join(sentence)
    #print non_re_sentence
    #print new_list
    print " ".join(ambiguated_output(new_list))
   
   
if __name__=="__main__":
  main()

