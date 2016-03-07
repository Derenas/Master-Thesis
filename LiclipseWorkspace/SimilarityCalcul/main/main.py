'''
Created on Mar 7, 2016

@author: vtassan
'''

from lxml import etree

def xmltotxt():
    tree = etree.parse("foo.xml")
    for line in tree.xpath("/pdf2xml/page/text"):
        print(line.text)

def read():
    readfile = open('../00a01.txt','r')
    for line in readfile.readlines():
        print line
    readfile.close()


if __name__ == '__main__':
    read()