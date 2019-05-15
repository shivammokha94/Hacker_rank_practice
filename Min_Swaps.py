
def findi(t, arr):
    if t in arr:
        return arr.index(t)

    

arr = [4, 3, 1, 2]
c = 0
n = len(arr)

for i in range(n - 1):
    t = min(arr[i:])
    v = findi(t, arr)
    
    if arr[i] > arr[v]:
        arr[i], arr[v] = arr[v], arr[i]
        c = c + 1

print(arr)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()