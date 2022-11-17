max = 1000

query = 4

one = 1

two = 100

arr = [40, 60, 10, 70]

res = 0
for i in range(0, query):

    if i % 2 == 0:
        print(two, arr[i], " = ", abs(two - arr[i]))
        if (two>arr[i]):
            res += abs(two - arr[i])
        else:
            res += abs(arr[i]-two)
        two = abs(arr[i])

    else:

        print(one, arr[i], " = ", abs(one - arr[i]))
        if (one>arr[i]):
            res += abs(one - arr[i])
        else:
            res += abs(arr[i]-one)
        one = abs(arr[1])

    print(res)
