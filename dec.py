import time

def calc(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()
    print(str((end-start)*1000))
    return result



array = range(1,10000)
out_a = calc(array)
print(out_a)




