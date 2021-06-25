
test = [1, 2, 4, 5, 6, 23, 45, 56, 223, 456, 6785]

def b_search(lst, tgt):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == tgt:
            return mid
        elif lst[mid] > tgt:
            end = mid - 1
        elif lst[mid] < tgt:
            start = mid + 1


print(b_search(test, 5))
print(b_search(test, 223))
print(b_search(test, 1))
print(b_search(test, 6785))
print(b_search(test, 3))