def sort_list(a):
    length=len(a)
    for i in range(0,len(a)-1):
        for q in range(0,length-i):
            if a[q]>=a[length-1-i]:
                a[length - 1 - i], a[q] = a[q], a[length - 1 - i]
    return a


if __name__ == "__main__":
    list = [1, 7, 4, 89, 34, 2]
    print(sort_list(list))