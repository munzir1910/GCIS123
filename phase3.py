
'''
Mohammed Nagla's Repository link - https://github.com/mohamed19874/Mohamed-nagla
Hishaam's Repository link - https://github.com/hb7464/hb7464 
Munzir's Repository link - https://github.com/munzir1910/GCIS123 
'''

#Phase 3

'''
A python file that contains a function to generate an array of desired size and sorts it using 
user-defined mergesort functions
'''

def generate_sorted_array_with_merge(size):

    '''The main function that generates an array of a specified size, passed as an argument
    by the user, and then calls the user-defined function "mergesort(arr)" to sort it using 
    mergesort'''

    import random as rdm
    import array as ar
    
    #Array Generation using list comprehension 
    # (creating a list of random elements and then converting it to an array)

    L = [rdm.randint(1, 100) for i in range(size)]

    Arr = ar.array('i',L)
    print(f'Array before sorting: {Arr}')

    #Array Sorting with merge sort

    return mergesort(L)

def mergesort(arr):

    '''A function designed to split the array recursively and use the merge(left,right) function
    to sort it'''

    if arr is None: 
        return None

    elif len(arr) <= 1: #Checks to see if only 1 element or less is left in the array
        return arr
    
    mid = len(arr) // 2 

    #Recursion that continuously calls itself to split the array into individual elements

    left = mergesort(arr[:mid])  
    right = mergesort(arr[mid:])

    #merge(left,right) sorts the elements while merging the array back together

    return merge(left,right)

def merge(left,right):

    '''A function to check the elements from the left '''

    import array as ar
    
    if not left:
        return right
    
    elif not right:
        return left
    
    sorted_arr = [] #Intializing a list to hold the elements and the convert to an array
    i = j = 0  #Checking the index of left and right one by one 

    while i < len(left) and j < len(right): #ensuring that we wont go out of index

        if left[i] < right[j]: #The actual sorting
            sorted_arr.append(left[i])
            i+=1 #going to the next index
        
        else:
            sorted_arr.append(right[j])
            j+=1 #going to the next index

    sorted_arr += left[i:] #Adding any remaining part of the left side to the sorted list
    sorted_arr += right[j:] #Adding any remaining part of the right side to the sorted list

    return ar.array('i',sorted_arr)

def main():
    
    '''The main function to call the function to generate and array a
    nd sort it with time complexity'''

    import time

    size = int(input("Enter the number of elements you want: "))
    
    start = time.perf_counter()
    Arr = generate_sorted_array_with_merge(size)
    end = time.perf_counter()

    print(f'The sorted array: {Arr} \nTime Taken to generate and sort: {end-start}')

    target = 72 #Alternatively can be changed to input

    #Timing linear search on the Array
    start = time.perf_counter()

    for ind in range(len(Arr)):
        if Arr[ind] == target:
            print(f'{target} is at {ind} index')
            break
    else:
        print(f'{target} not found in array')

    end = time.perf_counter()
    print(f'Time taken to find target with linear search: {end-start}')

    #Timing binary search on the Array
    from phase1_phase2 import binary_search #importing the binary search function from phase 2
    start = time.perf_counter()

    print(f'{target} found at {binary_search(Arr,target)} index')

    end = time.perf_counter()

    print(f'Time taken to find target with binary search: {end-start}')

    '''Generally as the size of the array increases, binary search becomes increasingly faster
    at finding the target value'''

if __name__ == '__main__':
    main()