'''
Givenanarrayofintegers,writeamethodtofindindicesmandnsuchthatifyou sorted elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest such sequence).
17.7
17.8
17.9
EXAMPLE
Input:1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19 Output: (3, 9)
'''

def ssl(the_list):

    if the_list is None: return None

    #get front of list
    front = [the_list[0]]
    for i in range(1, len(the_list)):
        item = the_list[i]
        if item >= front[-1]:
            front.append(item)
            front_idx = i
        else:
            break


    #get back of list
    back = [the_list[-1]]
    for j in range(len(the_list)-1, front_idx, -1):
        item = the_list[j]
        if (item <= back[-1]) and (item >= front[-1]):
            back.append(item)
            back_idx = j
        else:
            break


    #then we need to go through the middle and update the back / front indexes

    for k in range(front_idx, back_idx + 1):
        while k < front[-1]:
            front.pop()
            front_idx -= 1
        while k > back[-1]:
            back.pop()
            back_idx += 1


    return (front_idx, back_idx)

if __name__ == "__main__":

    print ssl([1,2,3,4,8,7,6,9,15,16,17])




    


