def func(n):
    return lambda a: a*n
# a*2
doubler = func(2)
print(doubler(3))
quintipler = func(5)
print(quintipler(3))


def price_calc(start, hourly_rate):
    return lambda hours: start + hourly_rate * hours

walking_cost = price_calc(10,30)
print(walking_cost(2))

premium_cost = price_calc(1,25)
print(premium_cost(2))
# OR
print(price_calc(1,25)(2))

print((lambda a,b,c:a+b+c)(2,3,4))

print((lambda a,b,c=2: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))
print((lambda *args: sum(args))(2,3,4,50))
