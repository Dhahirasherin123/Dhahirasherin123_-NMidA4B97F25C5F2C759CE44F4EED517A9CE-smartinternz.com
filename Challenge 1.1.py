def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


Num = int(input("enter the value : "))
res = factorial(Num)
print("the factorial of {} is {}".format(Num, res))
