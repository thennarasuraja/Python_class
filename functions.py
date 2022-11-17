# def add_and_multiply(a, b, d=10,c=9):
#     sum = a+b*c+d
#     return (sum, c,d)
# x,y,z=add_and_multiply(b=245, c=391, a=7, d=29)
# print(x, y,z)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
k=10
for  i in range(k,0,-1):
    if k>0:
        sum+=k

# def args_ex(*a):
#     print(a)
#     sum = a[0]+a[1]+a[2]
#     return (sum)
# print(args_ex(12.33,4,5,6))

# def kwargs_ex(**a):
#     print(a)
#     sum = a["a"]+a["b"]+a["c"]
#     return (sum)
# print(kwargs_ex(a=12.33,b=4,c=5,d=6))
# y= add_and_multiply(25, 39)
# print(y)
# x=add_and_multiply(245, 391, 7,8)
# print(x)

# a = 25
# b = 39
# c = 70
# d = a+b*c
# print(d)
# e = 245
# f = 391
# g = 7
# h = e+f*g
# print(h)