# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:11:09 2019

@author: jaredalbert
"""
#
#nums1 = [1, 21000]
#nums2 = [3, 4, 5, 7, 8, 9, 100]
#
#nums3 = sorted(nums1 + nums2)
#length = int(len(nums3))
#if length % 2 == 1:
#    return (nums3[length//2])
#else:
#    return (nums3[(length+1)//2] + nums3[(length-1)//2])/2

#    
#s = 'abcda'
#step = 0
#counter = 0
#for i in range(1, len(s)-1):
#    #print (i)
#    
#    print(s[i])
#    if s[i+1]==s[i]:
#            while s[i+step]==s[i-step]:
#                increment +=1
#                counter = max(counter, increment)
#                increment = 0
#print(counter)
##
#def reverse(x):
#    if abs(x)<=0xffffffff:
#        return 0
#    s = str(x)
#    
#    if x < 0:
#        
#        y = int( '-'+''.join([i for i in s[::-1]])[:-1])
#    else:
#       
#        y = int( ''.join([i for i in s[::-1]]))
#    
#    return y
#
#x = -24563
#print(reverse(x))        
 
#s = '-1234'
#y = int('-'+''.join([i for i in s[::-1]])[:-1])
#print (y)

#d = {}
#for i,j in enumerate(s[::-1]):
#    d[i] = j
#print (d.items())
#
#x = [(v,k) for k,v in d.items()]
#print(x)
#

'''6. ZigZag Conversion'''

#s = "PAYPALISHIRING"
#num_rows = 3
#
#def gen_matrix(s:str, num_rows: int) -> list:
#    
#    direction = 0  #0 is down, 1 is up
#    row_count = 0
#    #container, row = [], []
#    matrix =[[0 for i in range(len(s))] for j in range(num_rows)]
##    print(matrix)
#    for i in range(len(s)):
#        
#        matrix[row_count][i] = s[i]
#        
#        
#        if direction == 0: 
#            row_count+=1
#            if row_count == num_rows-1:
#                direction = 1
#                #row_count = num_rows
#                
#                
#        else: 
#           row_count -=1
#           if row_count == 0:
#               direction = 0
#               row_count = 0
##        print(matrix)       
##        print(row_count, i, direction)
#    return matrix
#   
#print(gen_matrix(s, 4))
#
#def process_matrix(m:list) ->str:
#    container = []
#    for l in m:
#        for c in l:
#            if c != 0:
#                container.append(c)
#    s = ('').join(container)
#    return s
#print (process_matrix(gen_matrix(s,3)))
                
#
#
#def gen_matrix(s:str, numRows: int) -> list:
#    
#    direction = 0  #0 is down, 1 is up
#    row_count = 0
#    container = []
#    
#    matrix =[[0 for i in range(len(s))] for j in range(numRows)]
##    print(matrix)
#    if numRows == 1 or len(s) <= numRows:
#            matrix = s
#            return s
#    for i in range(len(s)):
#        
#        matrix[row_count][i] = s[i]
#        
#        
#        
#        if direction == 0: 
#            row_count+=1
#            if row_count == numRows-1:
#                direction = 1
#                #row_count = num_rows
#                
#                
#        else: 
#           row_count -=1
#           if row_count == 0:
#               direction = 0
#               row_count = 0
##        print(matrix)       
##        print(row_count, i, direction)
#   
#
#    print(matrix)
#    for l in matrix:
#        for c in l:
#            if c != 0:
#                container.append(c)
#    s = ('').join(container)
#    return s
#s = 'AB'
#num_rows = 1
#print (process_matrix(gen_matrix(s,1)))
#                

'''8. String to Integer (atoi)'''

#s = ""
#
#def myAtoi(s:str) -> int:
#    sign = False
#    sign_bank = ['-','+']
#    num_bank = ['0','1','2','3','4','5','6','7','8','9']
#    
#    string = s.strip()
#    
#    ret_list = []
#    
#    if not string:
#        return 0
#    if string[0] in sign_bank + num_bank:
#        ret_list.append(string[0])
#        sign = True
#    if string[0] not in sign_bank + num_bank:
#        return 0
#    for c in string[1:]:
#        if c in num_bank:
#            
#            ret_list.append(c)
#        if ret_list and c not in num_bank:
#            break
#        
#            
#    if len(ret_list) == 1 and ret_list[0] in sign_bank:
#        return(0)
#    if not ret_list:
#        return(0)
#    y = (int(''.join(ret_list)))
#        
#
#    if y >= 2**31:
#            return 2**31-1
#    if y < -2**31:
#        return -2**31
#    return y
#
#    
#print(myAtoi(s))   
#    
    
    
#def myAtoi(s:str) -> int:
#    signed = 0
#    sign = {43,45}
#    num_bank = {48,49,50,51,52,53,54,55,56,57}
#    x = []
#    for c in s:
#        print(c)
#        if not x or ord(c) not in (sign,  num_bank):
#            
#            if ord(c) == 32:
#                continue
##            else:
##                break
##        if not x and ord(c) in num_bank:
##            x.append(ord(c))
#        if not x and ord(c) in sign:
#            x.append(ord(c))
#            signed = True
#        if not x and ord(c) in num_bank:
#            x.append(ord(c))
#        if x:
#            if ord(c) not in (sign &  num_bank):
#                break
#    
##                break
##        
##    if not x:
##        
##         x = [ord(c) for c in s if ord(c) in sign]
#        
#      
#    return list(map(lambda x: chr(x), x))#''.join(map(chr,x))#[chr(c) for c in x]
#print(myAtoi(s))       



'''9. Palindrome Number'''
#def isPalindrome( x: int) -> bool:
#    s = str(x)
#    return [c for c in s] == [c for c in s[::-1]]
'''without converting to string first'''
'''still needs worknot finished'''

#import math
#def isPalindrome( x: int) -> bool:
#    num_len = math.floor(math.log10(x))+1
#    while num_len >0:
#        num = x%10
#        x//=10
#        num_len -=1
#        print(x, num)
#    return num_len
#print (isPalindrome(12345))

##    
#'''10. Regular Expression Matching'''
#import re
#pat = re.compile(rf'^{p}$')
#find = pat.search('.f')
#print (find.group())
#
#'''11. Container With Most Water'''
#'''Slow but accurate'''
#l = [1,8,6,2,5,4,8,3,7]
##
##def maxArea(height: [int]) -> int:
##    most = 0
##    for i,h1 in enumerate(height):
##        for j,h2 in enumerate(height):
##            most = max(most, min(h1,h2) * abs(j -i))
##            print(i,h1,j,h2, min(h1,h2) * abs(j -i), most)
##    return(most)
##maxArea(l)
## 
#l = [3,1,8,6,2,5,4,8,3,7,2]           
#def maxArea(height: [int]) -> int:
#    max_area = 0
#    ls = 0
#    rs = len(height) - 1
#    #print(ls,rs, height[ls])
#    while (ls <= rs):
#        if height[ls] >= height[rs]:
#            max_area = max(max_area, height[rs] * (rs - ls))
#            rs -= 1
#        if height[ls] < height [rs]:
#            max_area = max(max_area, height[ls] * (rs - ls))
#            ls += 1
#    return (max_area)
#print(maxArea(l))
    
    
    
    
#    
#'''Given a string, determine if it is a palindrome, 
#considering only alphanumeric characters and ignoring cases.
#Note: For the purpose of this problem, we define empty 
#string as valid palindrome.'''
#
#s = "A man, a plan, a canal: Panama"
#import re
#
#def isPalindrome(s: str) -> bool: 
#    new_s = re.sub(r'\W+', '', s).lower()  
#    return all (n==m for n,m in zip(new_s, reversed(new_s)))
#       
#print (isPalindrome(s))    
#def intToRoman(num: int) -> str:
#    roman_dict = {'1':'I', '2':'II', '3': 'III}
#    s = ''
#    num = str(num)
#    for char in num:
#        s = s + roman_dict.get(char)
#    print(s)

#intToRoman(11)

#num = 3994
'''12 int to roman numeral'''
#def intToRoman(num: int) -> str:
#    conversion_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), \
#                       (100, 'C'), (90,'XC'), (50, 'L'), (40, 'XL'), \
#                       (10, 'X'), (9,'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
#    s = ''
#    for tup in conversion_list:
#        while num >= tup[0]:
#            #print(num, tup[1], s)
#            s = s + tup[1]
#            num -= tup[0]
#    return s       
#    
#
#
#print(intToRoman(num))  
'''5. Longest Palindromic Substring'''
#s = 'abcdadcbaa'
#def longestPalindrome(s: str) -> str:
#    ml = 0
#    for i,j in enumerate(s):
#        while i < c:
#            
#        c = s.find(j, i+1)
#        print ('j: ', j, 'c: ', c, 'ml: ', ml, s[i], s[c])
##        while i < c:
#        count = 0
##            if s[i] != s[c]:
##                break
#        while s[i] == s[c] and i < c:
#            print ('j: ', j, 'c: ', c, 'ml: ', ml, s[i], s[c])
#            count +=1
#            ml = max(ml, count)
#            i+=1
#            c-=1
#                #print(ml, i, c)
#            
#    return ('ml', ml)
#print(longestPalindrome(s))
#s ="ccc"             
#import re
#
#def longestPalindrome(s: str) -> str:
#    max_len = 0
#    ns = s
#    my_dict = {}
#    
#    if not s:
#        return ''
#    if len(s) == 1:
#        
#        return s
#    if len(s) == 2:
#        if s[0] == s[1]:
#            return s
#        else:
#            return s[0]
#    else:
#        for i, j in enumerate (s):
#            #print('j: ', j)
#            ml = [m.start(0) for m in re.finditer(j,s)]
#            print('ml:', ml)
#            for n in ml[1:]:
#                print('s[i]', s[i],'s[n]',  s[n], 'n: ', n)
#                count = 0
#                ss = ''
#                i2 = i
#                
#                while ns[i2] == ns[n] :
#                    print(f'ns[i2]: {ns[i2]} == ns[n]: {ns[n]}' )
#                    count += 1
#                    ss = ss + ns[n]
#                    my_dict[len(ss)] = ss 
#                    print('my_dict', my_dict.items())
#                    max_len = max(max_len, count)
#                    print ('ns[i2]', ns[i2],'j: ', j,'i2: ', i2, 'n', n, 'ns[n]',  ns[n], 'max len',max_len,\
#                           'count',count, 'ss', ss)
##                    i2 += 1 
##                    n -= 1
#                    if i2 == len(s) -1:
#                        break
#                    if n == 0:
#                        break
#                    n -= 1 
#                    i2 += 1 
#                    
#        return(('answer', my_dict.get(max_len)))
#    #        print(i,j, ml)
#print(longestPalindrome(s))
#    #print([m.start(0) for m in re.finditer('a', s)])  
#
#

import re
def longestPalindrome(s: str) -> str:
    ns = s
    max_len = 0   
    my_dict = {}
    if not s:
        return ''
    if len(s) == 1:
        
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    for i, j in enumerate(s):
        ss=''
        i2 = i
        ms = [m.start(0) for m in re.finditer(j, s)]
        for n, m in enumerate(ms):
            count = 0
            while s[i2] == s[n]:
                ss = ss + ns[n]
                n-=1
                i2+=1
                if n == i:
                    my_dict[len(ss)] = ss 
                    max_len = max(max_len, count)
                count +=1
                
    return(('answer', my_dict.get(max_len)))  
      
s = 'aba'
print(longestPalindrome(s))               



         