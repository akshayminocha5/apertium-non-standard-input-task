#!/usr/bin/python
########author: Akshay Minocha############
########mailto:akshayminocha5@gmail.com###
#In accordance with the Apertium stream format ... http://wiki.apertium.org/wiki/Apertium_stream_format
import re
import sys
def main():
  text=sys.stdin.readlines()
  for line in text:
    x=re.sub('\@',r'\@',line)
    x=re.sub('\^','\^',x)
    x=re.sub('\$','\$',x)
    x=re.sub('\<','\<',x)
    x=re.sub('\>','\>',x)
    x=re.sub('\}','\}',x)
    x=re.sub('\{','\{',x)
    x=re.sub('/','\/',x)
    #x=re.sub(r'*','\*',x)
    print x[:-1]
  
if __name__=="__main__":
  main()
