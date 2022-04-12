# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:39:04 2019

@author: jaredalbert

"""
import cProfile



from collections import Counter
profiler = cProfile.Profile()
profiler.enable()
def main():
    vehicle_list = 'daimler mercedes audi vw volkswagen porsche ford gm \
                        general+motors mclaren fisker tesla rivian toyota \
                        honda lexus infiniti jaguar land rover aston ferrari\
                        maserati bmw rolls royce bently lucid faraday škoda'.split()
           
    vehicle_list.sort()
            
    with open('seeking_alpha_201804.txt', 'r') as file:
        file = (file.read())
        
    transcript_list = list(map(lambda x:x.lower(), file.split()))
    transcript_dict = Counter(transcript_list)
    
    incidence_list = []
    for vehicle in vehicle_list:
        #print(vehicle)
        incidence_list.append((vehicle, transcript_dict[vehicle]))
    
    count_list = [(v,k) for (k,v) in incidence_list]
    
    count_list.sort(key = lambda tup:tup[0], reverse = True) 
    print(count_list)   
        
    print(dict(incidence_list)) 
    profiler.print_stats(sort='cumtime')  
    
if __name__ == '__main__':
    for _ in range(1,15):
        main()
    
