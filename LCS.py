__author__ = 'changyunglin'

# compute the longest common subsequence of X(1...m) and Y(1...n)
# this only print out common sub character in this two string
# they are not suppose to be continuous


string1 = 'AATCC'
string2 = 'ACACG'


def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # a matrix to store the LCS number
    C = [[0] * (n+1) for _ in range(m+1)]    # this includes the

    for r in range(1, m+1):
        for c in range(1, n+1):
            if X[r-1] == Y[c-1]:
                C[r][c] = C[r-1][c-1] + 1
            else:
                C[r][c] = max(C[r][c-1], C[r-1][c])
    return C


def backTrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ''
    elif X[i-1] == Y[j-1]:
        return backTrack(C, X, Y, i-1, j-1) + X[i-1]  # X[i-1]: returns the same element we found
    else:   #X[i-1] != Y[j-1]:
        if C[i-1][j] > C[i][j-1]:
            return backTrack(C, X, Y, i-1, j)
        else:
            return backTrack(C, X, Y, i, j-1)


def backAllTrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([''])
    elif X[i-1] == Y[j-1]:
        return set([Z + X[i-1] for Z in backAllTrack(C, X, Y, i-1, j-1)])
    else:
        R = set()
        if C[i-1][j] >= C[i][j-1]:
            R.update(backAllTrack(C, X, Y, i-1, j))
        if C[i-1][j] <= C[i][j-1]:
            R.update(backAllTrack(C, X, Y, i, j-1))
        return R


C = LCS(string1, string2)
for e in C:
    print e
print "Some LCS: '%s'" % backTrack(C, string1, string2, len(string1), len(string2))
print "All LCSs: %s" % backAllTrack(C, string1, string2, len(string1), len(string2))