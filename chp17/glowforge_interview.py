#
# 
# Your previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/profile
# 
# Enjoy your interview!
# 
# Alright I'm in!
# 
# 

from collections import defaultdict

def count_mistakes1(array, low, high):
    
    mistakes = 0
    
    correct = defaultdict(int)
    
    for item in array:
        #out of range
        if item < low or item > high:
            mistakes += 1
    
        #detect dups
        elif correct.get(item) > 0:
            mistakes +=1
        
        else:
            correct[item] += 1
    
    mistakes += (high - low + 1) - len(correct.keys())
   
    return mistakes


def count_mistakes2(array, low, high):
    mistakes = 0
    
    array.sort()
    array_len = len(array)
    for idx,item in enumerate(array):
        #out of range
        if item < low or item > high:
            mistakes += 1
    
        #detect dups
        elif (idx +1) < array_len:
            if (item == array[idx + 1]):
                mistakes +=1       
    
    mistakes += (high - low + 1) - (array_len - mistakes)
   
    return mistakes


def count_mistakes(array, low, high):  
    correct = defaultdict(int)
    error_items = []
    
    for item in array:
        #out of range
        if item < low or item > high:
            error_items.append(item)
    
        #detect dups
        elif correct.get(item) > 0:
            error_items.append(item)
        
        else:
            correct[item] += 1
    
    for i in range(low, high+1):
        if i not in correct.keys():
            error_items.append(i)
   
    return error_items
            
        
if __name__ == "__main__":
    
    assert 0 == len(count_mistakes([1,2,3,4,5], 1,5))
    
    assert 1 == len(count_mistakes([1,1,2,3,4,5], 1,5))
    assert 1 == len(count_mistakes([1,2,3,4,5,6], 1,5))
    assert 1 == len(count_mistakes([1,2,3,4,5,0], 1,5))
    
    assert 2 == len(count_mistakes([1,4,5], 1,5))
    
    assert 3 == len(count_mistakes([1,2,3,4,5,6,6,6], 1,5))
    print("All good")
