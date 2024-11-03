import time

def calc_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f'The total time taken for {func.__name__} is {str((end-start)*10000)} ')
        return result
    return wrapper

@calc_time
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

numbers=range(0,100)

calc_square(numbers=numbers)

