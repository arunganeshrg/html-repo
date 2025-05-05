def solution(A):
    MOD = 10**9
    income = A[0]  # Start with 1 asset, sell it at day 0
    holding = False  # We sold it

    for i in range(1, len(A)):
        if not holding and A[i] < A[i - 1]:  # Price dropped → buy
            income -= A[i]
            holding = True
        elif holding and A[i] > A[i - 1]:  # Price rose → sell
            income += A[i]
            holding = False

    return income % MOD

print(solution([4, 1, 2, 3]))
