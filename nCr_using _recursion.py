'''
nCr means if you are given “n” number different items and you have to chose “r” number of items from it
nCr gives the total number of ways possible
nCr = (n-1)C(r-1) + nC(r-1)
'''

# create 2d array, all set to -1
  
def combinations(n, r):
    memo = [[-1 for _ in range(r + 1)] for _ in range(n + 1)]

    def calc_combinations(n, r):
        if r == 0 or r == n:
            return 1
        if memo[n][r] != 0:
            return memo[n][r]
        memo[n][r] = calc_combinations(n - 1, r - 1) + calc_combinations(n - 1, r)
        return memo[n][r]

    return calc_combinations(n, r)

n = int(input("Enter a number of differnt items"))
r = int(input("Enter number of items you want to choose"))
result = combinations(n, r)
print(f"Number of combinations of {n} choose {r} is: {result}")