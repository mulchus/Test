def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2	# Haxopm cepepuny Maccuea
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)


def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


array = [38, 27, 43, 3, 9, 82, 10]

merge_sort(array)

print( "OTCopTMpoBaHHbiM MaccuB:", array)

# Алгоритм быстрой сортировки
unsorted = [33, 2, 3, 45, 6, 54, 33]
quick = lambda l: quick([x for x in l[1:] if x <= l[0]]) + [l[0]] + quick([x for x in l if x > l[0]]) if l else []
print(quick(unsorted))
