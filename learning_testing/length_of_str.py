## -*- coding: utf-8 -*-
#"""
#Created on Mon May 27 11:02:37 2019
#
#@author: jaredalbert
#"""
#import typing
#class Solution:
#    def lengthOfLongestSubstring(self, s: str) -> int:
#        max, l = 0,0
#        for i in range(len(s)):
#            print(f's[i], {s[i]}')
#            counter = set()
#            
#            for item in s[i:]:
#                if item in counter:
#                    l = len(counter)
#                    counter.clear()
#                    counter.add(item)
#                    print(counter)
#                    print('l:',l)
#                    
#                    print('max:', max)
#                else:
#                    counter.add(item)
#                    l = len(counter)
#                    print(counter)
#                    print('l:',l, 'max: ', max)
#            
#                max = l if l > max else max
#                   
#                
#        return (f'max: {max}')
#        
#s = Solution()
#print(s.lengthOfLongestSubstring(" "))
#
#v ="dvdf"
#for i in range(len(v)):
#            print(v[i])
#            
#import typing
#class Solution:
#    def lengthOfLongestSubstring(self, s: str) -> int:
#        largest, l = 0,0
#        counter = set()
#        for i in range(len(s)):
#            for item in s[i:]:
#                if item not in counter:
#                    counter.add(item)
#                    l = len(counter)
#                                 
#                    print(f'counter: {sorted(counter)}, item: {item}')
#                    print('l:',l)
#                    
#                    print('max:', largest)
#                else:
#                    counter.clear()  
#                    
#                    print(f'counter: {counter}')
#                    print('l:',l, 'max: ',largest)
#            
#                largest = max(l, largest)
#                   
#                
#        return (f'max: {largest}')
#        
#s = Solution()
#print(s.lengthOfLongestSubstring("jbpnbwwd"))

s ="dvdfffdesar"
#my_dict = {}
#for i in range(len(v)):
#    my_dict[v[i]] = i        
#    print(my_dict)
#    
#start = 0; length = 0; seenChars = {}
#
#for i in range(len(s)):
#    if s[i] in seenChars:
#        start = max(start, seenChars[s[i]] + 1) 
#   
#    length = max(length, i - start +1)
#    seenChars[s[i]] = i
#    
#print(length, seenChars) 

print('test')
        