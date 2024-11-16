'''
Mohammed Nagla's Repository link - https://github.com/mohamed19874/Mohamed-nagla
Hishaam's Repository link - https://github.com/hb7464/hb7464 
Munzir's Repository link - https://github.com/munzir1910/GCIS123 
'''

def generate_sorted_data(size):
    #Generates an array of size random integers between 1 and 100 and sorts it using insertion sort.

    import random

    mydata = [random.randint(1, 100) for _ in range(size)]

    # Insertion sort implementation
    for i in range(1, len(mydata)):
        nagla = mydata[i]
        n = i - 1
        while n >= 0 and nagla < mydata[n]:
            mydata[n + 1] = mydata[n]
            n -= 1
        mydata[n + 1] = nagla

    return mydata

def binary_search(sorted_array, target):

    '''A function designed to find a specified target value in a sorted array
    and return its index if it is found and return None if the value is not in the array'''

    left = 0                        #Start of the array
    right = len(sorted_array) - 1   #End of the array

    while left <= right:
        middle = (left + right) // 2

        if sorted_array[middle] == target:
            return middle
        elif sorted_array[middle] > target:
            right = middle - 1
        elif sorted_array[middle] < target:
            left = middle + 1
            
    return None

def main():

    '''The main function to call the function to generate and array a
    nd sort it with time complexity'''

    import time

    size = int(input("Enter the number of elements you want: "))
    
    start = time.perf_counter()
    Arr = generate_sorted_data(size)
    end = time.perf_counter()

    print(f'The sorted array: {Arr} \nTime Taken to generate and sort: {end-start}')

    target = int(input("Enter a value to be found: "))
    start = time.perf_counter()

    print(f'Target found at {binary_search(Arr,target)} index')

    end = time.perf_counter()

    print(f'Time taken to find target: {end-start}')

if __name__ == '__main__':
    main()