'''
Created on Feb 25, 2016

@author: vtassan
'''
import sys  



def allchar():
    reload(sys)  
    sys.setdefaultencoding('utf8')
    str = '0394'
    print u'\u2122'
    print str
#     for i in range(0,100):
#         print u'\u0001'+str(i)

if __name__ == '__main__':
    allchar()