#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''

def partition(array, low, high):
    pivot = array[high]
    i = low -1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quicksort(array, low, high):
    if low < high:
        
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)
        return array






        

#WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION


#WHAT DOES IT RETURN?


def main():
    with open("numbers.txt") as myFile:
        data = myFile.readline().split(',\[\]')
        print(type(data))
        
        #data = data.replace('[',"")
        #data = data.replace(']',"")
        #data = data.split(',')
    #data = [1, 7, 4, 1, 10, 9, -2]
    #print("Unsorted Array")
    data1 = data[0]
    data1 = data1.replace('[', "")
    data1 = data1.replace(']', "")
    print(data1)
    print(type(data1.split(',')))
    data2 = data1.split(',')
    print(type(data2[0]))
    data3 = list(map(int, data2))
    print(data2[0])
    print(data3[0])
    print(type(data3[0]))
    sorted_list = quicksort(data3, 0, len(data3)-1)
    print(sorted_list)
    with open(r'sorted.txt', 'w') as fp:
        fp.writelines(str(sorted_list))
    #print(data1[2])
    #print(data)
    #print(data[0])
     
    #size = len(data[0])
     
    #quicksort(data[0], 0, size - 1)
    
     
    #print('Sorted Array in Ascending Order:')
    #print(data[0])
    
    #sorted = quicksort()
    #data = myFile.readline()

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE



    return 0 #WHAT DOES IT RETURN?


if __name__ == "__main__":
    main()
    
