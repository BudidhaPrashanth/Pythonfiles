from  numpy import  *
arr1 = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr1.ndim)
print(arr1.size)
print(arr1.shape)
print(arr1.flatten())
print(arr1.reshape(3,3)) #row ,col
print(arr1.resize(9,1))
print(arr1)

mat = matrix(arr1)
print(diagonal(mat))
print(mat.dtype)
print(mat.min())
print(mat.max())

m1 = matrix("1 2 3 ;4 5 6; 7 8 9")
m2 = matrix('4 5  6;7 8 9; 1 2 3 ')
print(m1+m2)
print(type(m1))

print(arr1.itemsize) #in bytes each element
a = arr1.astype(complex) # to change dtype already  exiting one
print(a)