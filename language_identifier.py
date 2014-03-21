#!/usr/bin/python
import langid
import sys
def main():
  s=sys.stdin.readlines()
  test_content=""
  if len(s)<10:
    test_content=" ".join(s)
  else:
    test_content=" ".join(s[:10])
  print langid.classify(test_content)[0]





if __name__=="__main__":
  main()
