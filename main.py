from exception import ElementNotInList


def binary_search(array: [], x: int, lo=0, hi=None):
    if hi is None:
        hi = len(array)

    while lo < hi:
        mid = (lo + hi) // 2
        midVal = array[mid]
        if midVal < x:
            lo = mid + 1
        elif midVal > x:
            hi = mid
        else:
            return mid - 1
    raise ElementNotInList('Элемент не входит в список', array.index(mid - 1))


def tryParseString(string):
    try:
        _array = string.split(' ')
        _array = list(map(int, _array))
        _array.sort()
        return _array
    except:
        return 'Не удалось распарсить строку'


inputString = '1 25 2 12 4 9 26 17 5 7 11'
inputInt = int(input('введите любое число, только целое =) '))

arr = tryParseString(inputString)
result = None
resultMsg = None

if type(arr) != str:
    try:
        result = binary_search(arr, inputInt)
    except ElementNotInList as e:
        resultMsg, resultIndex = e()


if resultMsg is not None:
    print(resultMsg)
    print(resultIndex)
elif result is not None:
    print(result)

print(arr)
