UECM3033 Assignment #2 Report
========================================================

- Prepared by: **Wong Chun Weng**
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/wongcw30utar/UECM3033_assign1](https://github.com/wongcw30utar/UECM3033_assign1)

#### Explain your selection criteria here. :
- By the **definition of positive definite matrix**, a matrix is said to be positive definite if it is symmetric and if x<sup>T</sup>Ax > 0 for every non-zero _n_-dimensional vector x.
- By **Convergence theorem for SOR method**, result for SOR method will converges if and only if A is positive definite.
- Thus, before solving for Ax = b, _**solve(A,b) function**_ will check whether A has only positive eigenvalues and whether is a symmetric matrix or not.
- If A has at least one negative eigenvalue or not a symmetric matrix, then it will solved by using LU factorization.
- If A has only positive eigenvalues and is a symmetric matrix, then it will solved by using SOR method.

#### Explain how you implement your `task1.py` here:
- solution for first linear system is **[1.0, 1.0, 1.0]**
- solution for second linear system is **[0.99999999999999423, -1.0000000000000049, 4.0, -3.500000000000004, 6.9999999999999947, -1.0000000000000002]**
- Matrix A and b is passed into self defined function **_solve(A,b)_**.
- **_solve(A,b)_** will check Matrix A whether is a Symmetric Positive Definite Matrix or not.
- If it is not, then it will solved by LU Factorization method.
- Else, it will solved by SOR method.

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file:

![Ari_original.jpg](Ari_original.jpg)

#####  How many non zero element in $\Sigma$?
- Given $\Sigma$ is a _N_ x _M_ matrix and assume all σ are non zero.
- It has N non zero elements.
- In this case, $\Sigma$ has 800 non zero elements.

### Put here your lower and better resolution pictures. Explain how you generate these pictures from `task2.py`:

###### Compression - Lower Resolutions : 
- ![ariana_low.jpg](ariana_low.jpg)

###### Compression - Higher Resolutions :
- ![ariana_better.jpg](ariana_better.jpg)

- Initially, fragment of code is given in `task2.py` and it is able to read an image and separate it's RGB values into 3 different arrays.
- Note that Singular Value Decomposition is needed for image compression. Thus, `numpy.linalg.svd` is used for computing $\Sigma$, U and V<sup>T</sup> for each R,G,B arrays.
- Create new matrix $\Sigma$30 which is same dimensions as $\Sigma$, but keeping first 30 non zero elements, and set the remaining non zero elements to zero.
- Performing multiplication between U,$\Sigma$30,V<sup>T</sup>. A new R,G,B value is generated.
- Combine 3 seperated new R,G,B arrays into one, and show it.
- A compressed image is generated.
- Next, repeat the same procedure as mentioned above, but this time keep the first 200 non zero elements for $\Sigma$.


##### What is a sparse matrix?
- It is a matrix in which a large portion of its entries are zero.
- In Image Compression with SVD, $\Sigma$ is computed and it is a sparse matrix.
- By only keeping first 30 or 200 non zero elements in $\Sigma$, and set the remaining entries as zero, a much sparser sparse matrix is generated.
- In fact, a sparse matrix can be stored in an efficient manner, leading to smaller file sizes.
- Therefore, a much sparser sparse matrix is smaller file sizes and more blur.

-----------------------------------

<sup>last modified: 2016-03-11</sup>
