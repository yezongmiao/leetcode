def sort_list(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
                a[i],a[j]=a[j],a[i]
    return a
if __name__ == "__main__":
    list = [1, 7, 4, 89, 34, 2]
    print(sort_list(list))