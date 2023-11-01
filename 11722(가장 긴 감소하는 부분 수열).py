array = []
number = int(input())
array = list(map(int, input().split()))
List = []
List.append(array[0])
end = 0


def binary(start, end, element):
    while (start < end):
        mid = int((start+end)/2)
        if (element < List[mid]):
            start = mid + 1
        else:
            end = mid
    return end


for i in range(1, number, 1):
    if (List[len(List)-1] > array[i]):
        List.append(array[i])
        end = len(List) - 1
    else:
        point = binary(0, end, array[i])
        List[point] = array[i]


print(len(List))
