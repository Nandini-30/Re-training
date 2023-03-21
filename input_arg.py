def most_common(arr):
    freq = {} 
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return max(freq, key=freq.get)

def array():
  my_array = [1, 2, 2, 4, 7]
  result = most_common(my_array)
  print(result) 

array();