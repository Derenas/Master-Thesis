'''
Created on Feb 25, 2016

@author: vtassan
'''

import os, sys
import PyPDF2
import codecs
import re

def countoverlappingdistinct(pattern, thestring):
  total = 0
  start = 0
  there = re.compile(pattern)
  while True:
    mo = there.search(thestring, start)
    if mo is None: return total
    total += 1
    start = 1 + mo.start()

def read():
    tmtxt = open('tm.txt','r')
    tm = tmtxt.readline()
    print tm
    reload(sys)  
    sys.setdefaultencoding('utf8')
    fo =open ('16d03.txt', 'w')
    pdfFileObj = open('16d03.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages =  pdfReader.numPages
    for i in range(0,numPages):
        pageObj = pdfReader.getPage(i)
        pageText = pageObj.extractText()
        print pageText[0], countoverlappingdistinct(tm,pageText), countoverlappingdistinct('e',pageText)
        j = i+1
        if(pageText[0] == [0-9] and int(pageText[0]) == j):
            pageText = pageText[3:]
        fo.write(pageText)
        fo.write("\n")
    fo.write("lol")
    fo.close()
    pdfFileObj.close()
    


if __name__ == '__main__':
    read()


