# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:13:46 2019

@author: jaredalbert
"""


#C:\Users\jaredalbert\AppData\Local\Temp\Temp1_0bebb8f3b47c5fd442ad3a7566f7619a09d26efd89bd23523ae004e45dddd895.zip\naturestrollers\messages.zip
#file1 = 'C:\\Users\\jaredalbert\\AppData\\Local\\Temp\\Temp1_0bebb8f3b47c5fd442ad3a7566f7619a09d26efd89bd23523ae004e45dddd895.zip\\naturestrollers\\messages.zip'
#path1 = 'C:\\yahoo groups download\\test.txt'

#path2= 'C:\\Python27\\NEWS.txt'
#with open('seeking_alpha_201804.txt', 'r') as file:
#with open(path1, 'a+') as f:
#    file = f.write('nonsense')
#
#with open(path1, 'r+') as f:
#    file = f.read()
#
#    print(file)
import mailbox
import sys

file4 = 'C:/yahoo_groups_download/naturestrollers/messages_unzipped/18123187.mbox.00001'
#import gzip
#file2 = 'C:\\Users\\jaredalbert\\AppData\\Local\\Temp\\Temp2_0bebb8f3b47c5fd442ad3a7566f7619a09d26efd89bd23523ae004e45dddd895.zip\\naturestrollers\\messages.zip\\18123187.mbox.00001'
#file3 = 'C:\\Users\\jaredalbert\\Downloads\\0bebb8f3b47c5fd442ad3a7566f7619a09d26efd89bd23523ae004e45dddd895\\naturestrollers\\messages'
#with gzip.open(file2, 'r') as f:
#    file = f.read()
#C:\Users\jaredalbert\AppData\Local\Temp\Temp2_0bebb8f3b47c5fd442ad3a7566f7619a09d26efd89bd23523ae004e45dddd895.zip\naturestrollers\messages.zip

#file1 = r'C:\\Users\\jaredalbert\\AppData\\Local\\Temp\\Temp1_0bebb8f3b47c5fd442ad3a7566f7619a09d26efd89bd23523ae004e45dddd895\.zip\\naturestrollers\\messages\\18123187\.mbox\.00001.zip'
mbox1 = mailbox.mbox(file4)
#for k in mbox1.iterkeys():
#    try:
#        #print(f'key number:{k}, {mbox1.get_message(key = k)}')
#        message = mbox1[k]
#        print (message.)
#    except KeyError:
#        print('error')
#        continue
    #print(f'From: {message['from']}')

#msg1= mbox1.get_message(key =1)
#print (str(msg1))
message = mbox1[1]
print(message.items())
print(message.get_payload())