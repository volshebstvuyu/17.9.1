from exception import ElementNotInList


def binary_search(array: [], x: int, lo=0, hi=None):
    if hi is None:
        hi = len(array)
    if x < array[-1]:
        while lo < hi:
            mid = (lo + hi) // 2
            midVal = array[mid]
            if midVal < x:
                lo = mid + 1
            elif midVal > x:
                hi = mid
            else:
                return mid - 1
    else:
        raise ElementNotInList('Элемент не входит в список', len(array) - 1)
    raise ElementNotInList('Элемент не входит в список', mid - 1)


def try_parse_string(string):
    try:
        string = string.strip()
        _array = string.split(' ')
        _array = list(map(int, _array))
        _array.sort()
        return _array
    except:
        return 'Не удалось распарсить строку'


def read_choice():
    try:
        choice = input('Вы хотите ввести числа сами? (y/n)')
        if choice.lower() != 'y' and choice.lower() != 'n':
            raise Exception
    except:
        read_choice()
    if choice.lower() == 'y':
        return True
    return False


if read_choice():
    inputString = input('введите числа через пробел ')
    print(inputString)
else:
    inputString = '1 25 2 12 4 9 26 17 5 7 11'
inputInt = int(input('введите любое число для поиска, только целое =) '))

arr = try_parse_string(inputString)
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
