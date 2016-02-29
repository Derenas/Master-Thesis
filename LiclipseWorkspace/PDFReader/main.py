'''
Created on Feb 25, 2016

@author: vtassan
'''

import PyPDF2

def read():
    fo =open ('16d03.txt', 'w')
    pdfFileObj = open('16d03.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages =  pdfReader.numPages
    for i in range(0,numPages):
        pageObj = pdfReader.getPage(i)
        page = pageObj.extractText().encode('utf-8')
        print page[0], i+1
        j = i+1
        if(page[0] != ' ' and int(page[0]) == j):
            page = page[3:]
        fo.write(page)
        fo.write("\n")
    fo.close()
    pdfFileObj.close()
    


if __name__ == '__main__':
    read()

