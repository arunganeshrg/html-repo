def method(R,V):
    balanceA = 0
    balanceB = 0
    minA = 0
    minB = 0

    print("Length of the String:", len(R))

    for i in range(len(R)):
        if(R[i] == "A"):
            balanceA -= V[i]
            print("A Balance", balanceA)
            balanceB += V[i]
            print("B Balance", balanceB)
        else:
            balanceB -= V[i]
            print("B Balance", balanceB)
            balanceA += V[i]
            print("A Balance", balanceA)
        minA = min (minA, balanceA)
        minB = min (minB, balanceB)

    return [abs(minA), abs(minB)]


R = "BAABA"
V = [2, 4, 1, 1, 2]

X = method(R, V)
print(X)