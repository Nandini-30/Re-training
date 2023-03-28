#logic part
def copy(arr):
    return [row[:] for row in arr]

def paste(dest, src):
    for i in range(len(src)):
        for j in range(len(src[0])):
            dest[i][j] = src[i][j]

# presentation part
import logic2

def print_array(arr):
    for row in arr:
        print(row)


arr1 = [[1, 2], [3, 4]]
arr2 = logic2.copy(arr1)
logic2.paste(arr2, [[5, 6], [7, 8]])

print("Original array:")
print_array(arr1)
print("Copied array:")
print_array(arr2)





