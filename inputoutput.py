# x=input()
# j=""
# for i in x.split( ):
#     j+=i+" "
# # print(j, end="")
# x=input()
# print(type(x), sep="")
# x = input()
# x=x.split(" ")
# length= x[0]
# k=x[1]
# arr=[]
# for i in range(int(length)):
#     arr+= input()

# print(length, k)
# print(arr)
# x = input()
# x=x.split(" ")
# y= x[1]
# x=x[0]
# arr=""
# for i in range(0,int(x)):
#     arr+=str(input())+" "
# print(x," ",y)
# print(arr, sep=" ")


x = input().split(" ")
arr= input().split(" ")
string=""

for i in range(0,int(x[0])):
    string+=arr[i]+" "
print(x[0], x[1], sep=" ")
print(string)