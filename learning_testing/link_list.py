# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:05:44 2019

@author: jaredalbert
"""

class Node:  
    def __init__(self, data):
        # store data
        self.data = data
        # store reference (next item)
        self.next = None
    
       
class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def plist(self):
        printval = self.headval
        while printval is not None:
            print (printval.data)
            printval = printval.next
        
class ConstructLList:
    def __init__ (self, num):
        self.num = num
        
    def build_list_from_num(self):
        return [int(item) for item in reversed(str(self.num))]
    
    def build_llist(self):
        rlist = self.build_list_from_num()
        llist = SLinkedList()
        llist.headval = rlist[0]
        for item in rlist[1:]:
            i = Node(item)
            
             
           
        
c =  ConstructLList(1234)
#c.build_list_from_num()
print(c.build_llist() )
    
llist = SLinkedList()

llist.headval = Node('mon')
ln1 = Node('tues')
ln2 =Node('weds')

llist.headval.next = ln1
ln1.next = ln2

llist.plist()

