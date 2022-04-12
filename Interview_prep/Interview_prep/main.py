






# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
#     def __repr__(self):
#         return self.data
        
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def __repr__(self):
#         node = self.head 
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node=node.next
#         nodes.append("None")
#         return " -> ".join(nodes)  

# llist = LinkedList()
# first_node = Node('a')
# llist.head = first_node
# second_node = Node('b')
# third_node = Node('c')
# first_node.next = second_node
# second_node.next = third_node
# print (llist)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.previous = None
        
#     def __repr__(self):
#         return self.data
    
# class LinkedList():
#     def __init__(self, nodes = None):
#         self.head = None
#         if nodes is not None:
#             node = Node(data = nodes.pop(0))
#             self.head =  node
#             for elem in nodes:
#                 node.next = Node(data = elem)
#                 node = node.next
                
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next
    
#     def add_first(self, node):
#         node.next = self.head
#         self.head = node
    
#     def add_last(self, node):
#         if not self.head:
#             self.head = node
#             return
#         for current_node in self:
#             pass
#         current_node.next = node
        
#     def add_after(self, target_node_data, new_node):
#         if not self.head:
#             raise Exception('List is empty')
        
#         for node in self:
#             if node.data ==target_node_data:
#                 new_node.next = node.next
#                 node.next = new_node
#                 return
#         raise Exception("that data wasn't found in the list :(")
        
#     def add_before(self, target_node_data, new_node):
#         if not self.head:
#             raise Exception('List is empty')
        
#         if self.head.data == target_node_data:
#             return self.add_first(new_node)
        
#         prev_node = self.head
#         for node in self:
#             if node.data ==target_node_data:
#                 prev_node.next = new_node
#                 new_node.next = node
#                 return
#             prev_node = node
#         raise Exception("that data wasn't found in the list :(")
        
#     def remove_node(self, target_node_data):
#         if not self.head:
#             raise Exception('List is empty')
            
#         if self.head.data == target_node_data:
#             self.head=self.head.next
#             return
        
#         previous_node = self.head
#         for node in self:
#             if node.data == target_node_data:
#                 previous_node.next = node.next
#                 return
#             previous_node = node
#         raise Exception("that data wasn't found in the list :(")
        
        
        
            
#     def __repr__(self):
#         nodes = []
#         node = self.head
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append('None')
#         return ' -> '.join(nodes)
            
# llist1 = LinkedList(nodes = ['d', 'e', 'f'])

# llist = LinkedList()

# for node in llist1:
#     print (node)
    
# print (llist1)
# node1 = Node('a')
# node2 = Node('b')
# node3 = Node('c')

# node1.next = node2
# node2.next = node3
# llist1.head = node1

     








# import string
# def map_key():
#     possible_letters = string.ascii_lowercase
#     possible_numbers = string.digits
#     key_map = {}
#     key_len = {}
#     count = 0
#     for n in possible_numbers:
#         num = int(n)
#         if num in [7, 9]:
#             key_len[num]= 4
#         elif num in [0,1]:
#             key_len[num]= 0
#         else:
#             key_len[num]= 3
#         #breakpoint()
#         if num == 0:
#             key_map[num] = ' '
#         elif num == 1:
#             key_map[num] = ''
#         else:
#             key_map[num] = possible_letters[count: count+key_len[num]]
#         count += key_len[num]
        
#     return key_map
# #print(map_key())


# def keypad_string(keys):
#     '''
#     Given a string consisting of 0-9,
#     find the string that is created using
#     a standard phone keypad
#     | 1        | 2 (abc) | 3 (def)  |
#     | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
#     | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
#     |     *    | 0 ( )   |     #    |
#     You can ignore 1, and 0 corresponds to space
#     >>> keypad_string("12345")
#     'adgj'
#     >>> keypad_string("4433555555666")
#     'hello'
#     >>> keypad_string("2022")
#     'a b'
#     >>> keypad_string("")
#     ''
#     >>> keypad_string("111")
#     ''
#     '''
#     mapper_key = map_key()
#     st =''
#     count = 0
#     idx = 0
#     current_key =''
#     for num in keys:
#         if num == current_key:
#             print (num, 'num')
#             count+=1
#         current_key =  num
#         print(current_key, 'current_key',   \
#               count, 'count')
#         if count != 0:
#             len_set =  count % 3
#             if len_set == 2:
#                 idx = 2
#             if len_set == 2: 
#                 idx = 1
#             if len_set == 1:
#                 idx = 0
        
#         print(idx)
#         st += mapper_key.get(int(num))[idx]
        
        
        
#     return st

# print(keypad_string('22345'))
    
    
    
#     lst = []
#     i = 0
#     while i < len(keys):
#         j = keys[i]
#         print (j, 'j', i, 'i')
#         if int(j) == 0:
#             lst.append('y')
#             i+=1
#         if int(j) == 1:
#             lst.append('x')
#             i+=1
#         if int(j) == 2:    
#             l1 = []
#             while int(keys[int(i)])==2:
#                 #print(c1)
#                 l1.append(2)
                
#                 #print(l1)
#                 if i == len(keys) -1:
#                     break
#                 i+=1
#             l2 = len(l1)%3
#             print (l2,'l2')
#             #breakpoint()
#             if l2 == 0:
#                 lst.append('c')
#             if l2 == 1:
#                 lst.append('a')
#             if l2 == 2:
#                 lst.append('b')
#             i+=1
#         if int(j) == 3:    
#             l1 = []
#             while int(keys[int(i)])==3:
#                 #print(c1)
#                 l1.append(3)
#                 # i+=1
#                 if i == len(keys) -1:
#                     break
#                 i+=1
                    
#                 print(l1)
#             l2 = len(l1)%3
#             print (l2,'l2')
#             #breakpoint()
#             if l2 == 0:
#                 lst.append('f')
#             if l2 == 1:
#                 lst.append('d')
#             if l2 == 2:
#                 lst.append('e')
#             i+=1    
#             print(lst , 'lst')
#     st = ''.join(lst)
#         #breakpoint()
#     return st
# print (keypad_string('222333322222200113222'), 'done')

# # def dupe_cout(l:list, vals: str):
    






# def majority_element_indexes(lst):
#'''    
#     Return a list of the indexes of the majority element.
    
#     Majority element is the element that appears more than 
#     floor(n/2) times.
    
#     If there is no majority element, return []
    
#     >>> majority_element_indexes([1, 1, 2])
#     [0, 1]
#     >>> majority_element_indexes([0, 1, 2])
#     []
#     >>> majority_element_indexes([])
#     []

#     '''
#     from collections import Counter
#     #breakpoint()
#     C = Counter(lst)
#     te= sorted(C.keys(), key=lambda x: -C[x])
#     print (te)
#     M = max([(v,k) for k,v in C.items()])
#     if M[0] >= len(lst)/2:
#         l_out = [i for i,j in enumerate(lst) if M[1] == j]
#         return l_out
#     return []
    
    

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod

# print(majority_element_indexes([1, 1, 2, 3, 3, 3, 3]))

# def f(x):
#     assert x<0, 'x needs to be less than 0'
#     return x

# print(f(10))



# class A:
#     def f(self):
#         '''
#         >>> a= A()
#         >>> a.f()
#         Hello World
#         'Hello World'
#         '''
#         print('Hello World')
#         return 'Hello World'
    
#     @property
#     def error(self):
#         '''
#         >>> A().error
#         Traceback (most recent call last):
#         ...
#         Exception: I am an error
#         '''
#         raise Exception('I am an error')
        
#     def d(self, x):
#         '''
#         >>> a=A()
#         >>> a.d(10)
#         Args: 10
#         'Valid input'
#         >>> a.d(-1)
#         Traceback (most recent call last):
#         ...
#         ValueError: Invalid input

#         '''
#         if x <= 0:
#             raise ValueError('Invalid input')
#         print (f'Args: {x}')
#         return 'Valid input'
    
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

# import math

# l = [2.3456, -2.3456, 2.3454, -2.3454]
# print (list(math.trunc(i,3) for i in l))
# math.trunc()


# import math
# def round_up(num):
#     x = num * 100
#     y = math.floor(x)
#     breakpoint()
#     return y/100
    
# math.trunc()
# import string
# print('A' in string.ascii_lowercase)

# from collections import namedtuple

# Car = namedtuple('car', 'make model year mileage')

# c1 =Car('toy', 'cel', 1997, 122)



# import pickle
# import dill
# square = lambda x: x**2

# dump = dill.dumps(square)
# print(dump)
# class example_class:
#     a_number = 35
#     a_string = "hey"
#     a_list = [1, 2, 3]
#     a_dict = {'first':'a', 'second': 2, 'third': [1, 2, 3]}
#     a_tuple = (22, 23)
    
# my_object=example_class()

# my_pickled_object = pickle.dumps(my_object)
# print (f'this is my pickled object:\n{my_pickled_object}\n')

# my_object.a_dict = None

# my_unpickled_object = pickle.loads(my_pickled_object)
# print (f'a_dict of  is my unpickled object:\n{my_unpickled_object.a_dict}\n')






# from collections import defaultdict, Counter
# def top_three_letters(string):
#     '''
#     >>> top_three_letters('aaabbc')
#     [('c', 1), ('b', 2), ('a', 3)]
        
#     '''
#     c = defaultdict(list)
#     # for i in (string):
#     #     #breakpoint()
#     #     if not c[i]:
#     #         c[i]=1
#     #     else:
#     #         c[i]+=1
#     # return sorted([(k,v) for k,v in c.items()],key=lambda x:x[1], reverse = False)
    
#     return Counter(string)   

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()











# from collections import defaultdict


# student = {
#     'Jack': [80, 95],
#     'Jill': [85, 90]   
#     }

# def get_student_grade(name):
#     if name in student:
#         return student.get(name,[])
                        
# def get_grade_assignment(name):
#     return student.setdefault(name, [])
      
# def set_grades_naive(name, score):
#     if name in student:
#         for i in score:
#             student[name].append(i)
#     else:
#         student[name] = []
#         student[name].append(score)

# students=defaultdict(list, student)

# def set_best(name, score):
#         students[name].append(score)