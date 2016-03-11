import numpy as np
import copy as cp
ITERATION_LIMIT = 10
#Your optional code here
#You can import some modules or create additional functions

def lu(A, b):
    sol = []
    # Edit here to implement your code
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    A = LUdecomp(A)
    n = len(A)
    sol = cp.copy(b)
    for k in range(1,n):
        sol[k] = sol[k] - np.dot(A[k,0:k], sol[0:k])
    sol[n-1]=sol[n-1]/A[n-1, n-1]
    for k in range(n-2, -1, -1):
        sol[k] = (sol[k] - np.dot(A[k,k+1:n], sol[k+1:n]))/A[k,k]

    return list(sol)

def sor(A, b):
    sol = []
    # Edit here to implement your code
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    omega = computeOmega(A)
    sol = np.zeros_like(b)
    for itr in range(ITERATION_LIMIT):
        for i in range(len(b)):
            sums = np.dot( A[i,:], sol )
            sol[i] = sol[i] + omega*(b[i]-sums)/A[i,i]
    return list(sol)

def solve(A, b):
    condition = not(np.all(np.linalg.eigvals(A) > 0) & (np.transpose(A) == A).all() ) # Check whether A has only positive eigenvalues and whether a symmetric matrix or not.
    if condition:   #If A has at least one negative eigenvalue or not a symmetric matrix, then it will solved by using LU factorization.
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:           #If A has only positive eigenvalues and is a symmetric matrix, then it will solved by using SOR method.
        print('Solve by sor(A,b)')
        return sor(A,b)
        
def computeOmega(A): 
    D = np.diag(np.diag(A))
    l_plus_u = D - A
    D_inv = np.linalg.inv(D)
    Kj = np.dot(D_inv,l_plus_u)
    
    #spectral radius
    spec_radius = np.amax(np.linalg.eigvals(Kj))
    
    return (2*(1-np.sqrt(1-(spec_radius*spec_radius)))/(spec_radius*spec_radius)) 

def LUdecomp(A):
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i,k] != 0.0:
                lam = A[i,k] / A[k,k]
                A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                A[i, k] = lam
    return A

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = [[2,1,6], [8,3,2], [1,5,1]]
    b = [9, 13, 7]
    sol = solve(A,b)
    print(sol)
    
    A = [[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]
    b = [ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]
    sol = solve(A,b)
    print(sol)
