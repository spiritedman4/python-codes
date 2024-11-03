
def remote_control():
    yield "HBO"
    yield "Discovery"
    yield "VH1"
    yield "StarSports"

itr=remote_control()

print(itr)
print(next(itr))
print(next(itr))
print(next(itr))

#fibonacci series

def gen_fib_series(number):
    a,b=0,1

    while a < number:
        yield a
        a,b=b,a+b

for fib in gen_fib_series(100):
    print(fib)
