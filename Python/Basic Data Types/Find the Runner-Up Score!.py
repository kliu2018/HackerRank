if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    list1=list(set(list1))
    list1.sort()
    print(list1[-2])
