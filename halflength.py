import math
S = "zewmyde"
newlen = len(S)
operation_repeated = 0
for i in range(0, len(S)):
    flag = False
    for j in range(0, i):
        if j >= math.floor(len(S)/2):
            break
        else:
            print(S, len(S))
            if S[0]==S[1]:
                S = S.replace(S[-1], "", 1)
            else:
                S = S.replace(S[0], "", 1)

            for k in S:
                count_char = S.count(k)
                # print(S, count_char, math.floor(len(S)/2))
                if count_char == (len(S)/2):
                    flag = True
                    break
            operation_repeated = operation_repeated+1
    if flag == True:
            break
print(operation_repeated)
