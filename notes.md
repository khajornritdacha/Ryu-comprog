# ComProg Notes

## Tips

1. อ่านโจทย์ดีๆ ทำความเข้าใจตัวอย่างก่อนเริ่มคิดและเขียนโค้ด
2. เวลารัน Error ลองอ่าน Error code ดู จะช่วยให้เข้าใจว่าเราผิดเพราะอะไร
3. เวลาติดบัค print ออกมาเยอะๆ แล้วจะเห็นว่าตัวเองผิดอะไรง่ายขึ้น
4. เวลาติดบัค ค่อยๆ comment แล้ว run ทีละส่วนดู จะช่วยให้เข้าใจว่าเราผิดเพราะอะไร

## Coding

### String Compare

"Two" != "TWO" เพราะ string เทียบกันทุกตัวอักษร

### Sorting

ถ้าหากอยาก sort [a, b, c] โดย

1. b จากน้อยไปมาก
2. a จากมากไปน้อย
3. c จากมากไปน้อย

ให้สร้าง list ที่เป็น [b, -a, -c] เช่น

```python
arr = [[10, 5, 7], [1, 2, 3], [5, 4, 3]]
# convert into desired format
arr = [[5, -10, -7], [2, -1, -3], [4, -5, -3]]
arr.sort()
print(arr)

# output
# [[-10, 5, -7], [-5, 4, -3], [-1, 2, -3]]
```

### Sorted Vs list.Sort

#### Sorted

- return new sorted list but not modified original list

```python
arr = [10, 5, 7]
print(sorted(arr))
print(arr)
# output
# [5, 7, 10]
# [10, 5, 7]
```

#### list.Sort

- modified original list

```python
arr = [10, 5, 7]
arr.sort()
print(arr)
# output
# [5, 7, 10]
```

### Slicing

- slice list or list-like object
- syntax `list[start:stop:step]`

#### Example

```python
num="0123456789"
print(num[0:5])
print(num[0:5:2])

# output
# 01234
# 024
```

### != is not =! (Not Equal)

- `!=` is correct
- `=!` is wrong

### Escape Sequence

- newline `\n` (most common)
- tab `\t`

### Map Function

```python
arr = list(map(int, input().split()))
print(arr)
# input
# 1 2 3 4 5
# output
# [1, 2, 3, 4, 5]
```

### Range and Index

- If you want to iterate through all elements in list L you can use `range(len(L))`

```python
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
for i in range(len(arr) - 1):
    print(arr[i], end=" ")
print()
# output
# 1 2 3 4 5
# 1 2 3 4
```

## Numpy

### Insert in Numpy

- insert value in numpy array

```python
import numpy as np
arr = np.zeros((3, 2), int)
arr[0] = [1, 2]
arr[1] = [3, 4]
print(arr)
# output
# [[1 2]
#  [3 4]
#  [0 0]]
```

### Broadcasting

- convert smaller array into bigger ones

```python
import numpy as np
arr1 = np.array([[1], [2]])
arr2 = np.array([10, 20])
print(arr1 * arr2)
# output
# [[10 20]
#  [20 40]]
```

### Convert to list

- convert array to list

```python
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.tolist())
# output
# [[1, 2], [3, 4], [5, 6]]
```

### Matrix Multiplication with Numpy

- use `np.dot(A, B)` to multiply Matrix A with B

```python
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))
# output
# [[19 22]
#  [43 50]]
```

## Misc

### Exit(0)

- to force exit program (used to end program)

```python
x = int(input())
if x == 0:
    exit(0)
print(x)
# Exit program when x equals to 0
```

### Scope

- variabled declared within function can only be called in that function

```python
def func():
    x = 10
    print(x)
print(x)
# output
# NameError: name 'x' is not defined
```

### Cancel Program Terminal

- press `ctrl + c`
