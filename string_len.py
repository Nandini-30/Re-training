def word_lengths(x):
    result = []
    for i in x:
       result.append(len(i))
    return result

def list():
  my_list = ["hello how are you", "hi", "How are you"]
  result = word_lengths(my_list)
  print(result) 

list();