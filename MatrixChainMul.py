'''
print the answer

'''
def printMat(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print("{:^6d}".format(m[i][j]), end='|')
        print()

'''
This function will print the way that the braces recursive.

'''
def printResualt(s,i,j):
    if i==j:
        print("A",i," ",end="")
    else:
        print("(",end="")
        printResualt(s,i,s[i][j])
        printResualt(s,s[i][j]+1,j)
        print(")",end="")

'''
The algorithm
'''
def MatrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = None
            for k in range(i, j):
                if m[i][j] is None:
                    m[i][j]=m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                    s[i][j]=k
                else:
                    # q = cost/scalar multiplications
                    q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j]=k
    return m[1][n-1],m,s
def main():
    arr = [30,35,15,5,10,20,25]

    size = len(arr)
    m=list()
    s=list()
    a,m,s=MatrixChainOrder(arr, size)
    print("Dynamic Matrix")
    print("-"*15)
    printMat(m)
    print("Ancestors Matrix")
    print("-"*15)
    printMat(s)
    print("Answer Matrix")
    print("-"*15)
    printResualt(s,1,size-1)
    print("\nnumber of calculation {}".format(a))
    print()

if __name__ == '__main__':
    main()
