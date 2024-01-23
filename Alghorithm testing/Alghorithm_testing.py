# iterative function to get factorials
# def iterative_factorial(n):
#     fact = 1
#     for i in range(2, n+1):
#         fact *= i
#     return fact
# print(iterative_factorial(5))

# recursive function to get factorials
# def recur_factorial(n):
#     if n == 1:
#         return n
#     else:
#         temp = recur_factorial(n-1)
#         temp = temp * n
#     return temp
# print(recur_factorial(5))

# better recursive function to get factorials
# def recur_factorial(n):
#     if n == 1: return n
#     else: return n * recur_factorial(n-1)
# print(recur_factorial(5))

# def permute(string, pocket=""):
#     if len(string) == 0:
#         print(pocket)
#     else:
#         for i in range(len(string)):
#             letter = string[i]
#             front = string[0:i]
#             back = string[i+1:]
#             together = front + back
#             permute(together, letter + pocket)
# print(permute("ABC",""))

# linear search
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
arr = [2,5,8,9,10,16,22]
target = 10

print(search(arr,target))

# iterative binary search

def binary_itr(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
        
arr = [2,5,8,10,16,22,25]
target = 10

result = binary_itr(arr, 0, len(arr)-1,target)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")

#recursive binary search    
def binary_recur(arr, start, end, target):
   if end >= start:
        mid = start + end - 1 // 2
        if arr[mid] < target:
            binary_recur(arr, mid + 1, end, target)
        elif arr[mid] > target:
            return binary_recur(arr, mid - 1,target)
        else:
            return mid
        
arr = [2,5,8,10,16,22,25]
target = 10

result = binary_itr(arr, 0, len(arr)-1,target)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")


def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, iterations
A = [9,8,7,6,5,4,3,2,1]
print(bubble_optimized(A))