"""

LCS(Longest Common Sequence) 
최장 길이 공통 부문자열 길이 계산하기

- 교재 p.115

http://www.columbia.edu/~cs2035/courses/csor4231.F11/lcs.pdf
https://www.youtube.com/watch?v=EAXDUxVYquY

Examples:
>> lcs('abcbdab','bdcaba')
4

>> lcs('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA','GTCGTTCGGAATGCCGTTGCTCTGTAAA')
20

"""


def lcs_len(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    X = list(input("X: ").strip())
    Y = list(input("Y: ").strip())
    start = time.process_time()
    print(lcs_len(X, Y))
    print(f"Processing time: {(time.process_time()-start)%1e9 + 7}")

"""

- 위 알고리즘은 LCS 길이만을 저장한다. LCS 자체를 알고 싶다면 어떻게 해야할까? (p.116)

def lcs(X, Y):
    n = len(X)
    m = len(Y)
    dp = [['' for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + X[i-1]
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    return dp[-1][-1]


"""
