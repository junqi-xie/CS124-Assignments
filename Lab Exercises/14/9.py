def merge(l1, l2):
    l = []
    i, j = 0, 0
    while i != len(l1) and j != len(l2):
        if l1[i] <= l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1
    l += l1[i:len(l1)] + l2[j:len(l2)]
    return l

def sort(l):
    if len(l) == 1:
        return l
    else:
        n = len(l)
        return merge(sort(l[:n // 2]), sort(l[n // 2:n]))

l = eval(input())
print(sort(l))