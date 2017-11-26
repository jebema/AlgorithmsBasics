# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:22:37 2017

@author: Jessica
"""

def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)  #Calls partition function with the whole array, it returns an index saying from where 
        #to the left are the elements smaller than the last element [r] and from where to the rigest the bigger ones
        # q represents the new position from the last element that had position [r]
        quicksort(A,p,q-1) #A recurrent call to wuicksort with smaller segments, the ones from the left from q (p..q) are smaller than q, 
        quicksort(A,q+1,r) #A recurrent call to wuicksort with smaller segments, the ones from the right from q (q+1..r) are bigger than q, 
        
def partition(A,p,r): 
    x = A[r] # Sets x with the information from the last element [r]
    i = p-1 # An index that stars before de beggining of the segments
    for j in range(p,r,1):  #Traverse from 1 to one before the last element [r]
        if A[j]<=x:  #If the element j has a less value than x,
            i = i+1 #Then we increment the index i
            A[i], A[j] = A[j], A[i] #And exchange the values from i and j index. This way, the elements being in the left
            #From the start to i are all smaller than the element x in [r]. And all the elements in the right from j are bigger than x
    A[i+1], A[r] = A[r], A[i+1] #Finally, exchange the element x to be just in the middle from its smaller and bigger values,
    return i+1 #This function return the index where x is set in order to keep with the quicksort.

#A = [5,2,4,9,7,1,3,2,6]
A = [2,8,7,1,3,5,6,4]

n = len(A)
quicksort(A,0,n-1)   #n-1 because it starts in index = 0
print(A)
            