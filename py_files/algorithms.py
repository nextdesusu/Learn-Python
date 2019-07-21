import copy as c
import random as r

list_of_nums1 = [6, 3, 1, 10, 32, 54, 12, 45, 100, 453, 23, 5, 3, 5, 1, 6, 121]
list_of_nums2 = [24, 434564, 23, 5454, 23, 4546, 232, 656, 2324]
list_of_nums3 = [35, 23, 121, 11, 2, 1, 5, 6, 7, 3, 0]

############################################ BUBBLE SORT ##################################################
def bubble_sorting(used_list):
    sorted_ = False
    while not sorted_:
        sorted_ = True
        for num in range(len(used_list) - 1):
            if used_list[num] > used_list[num + 1]:
                used_list[num], used_list[num + 1] = used_list[num + 1], used_list[num]
                sorted_ = False
    return used_list
###########################################################################################################

############################################ INSERT SORT ##################################################
def insert_sorting(used_list):
    for num in range(len(used_list) - 1):
        if used_list[num] > used_list[num + 1]:
            used_list[num], used_list[num + 1] = used_list[num + 1], used_list[num]
            elem = used_list[num]
            iterator = 0
            finded = False
            used_list.pop(num)
            while not finded:
                if elem < used_list[iterator]:
                    used_list.insert(iterator, elem)
                    finded = True
                iterator += 1           
    return used_list
###########################################################################################################

############################################ SELECTION SORT ###############################################
def selection_sort(used_list):
    for iterator in range(len(used_list)):
        min_elem = used_list[iterator]
        changed = False
        for num in range(iterator, len(used_list)):
            if used_list[num] < min_elem:
                min_elem = used_list[num]
                num_of_min_elem = num
                changed = True
        if changed:
            used_list[iterator], used_list[num_of_min_elem] = used_list[num_of_min_elem], used_list[iterator]
        iterator += 1
    return used_list
###########################################################################################################

############################################ MERGE SORT ###################################################
def merge_sort(used_list):
    if len(used_list) <= 1:
        return used_list
    middle = (len(used_list)) // 2
    left_part = used_list[:middle]
    right_part = used_list[middle:len(used_list)]
    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)
    result = merge(left_part, right_part)
    return result

def merge(left_part, right_part):
    result = []
    while len(left_part) > 0 and len(right_part) > 0:
        if left_part[0] <= right_part[0]:
            result.append(left_part[0])
            left_part.pop(0)
        else:
            result.append(right_part[0])
            right_part.pop(0)
    if len(left_part) > 0:
        for l_index in left_part:
            result.append(l_index)
    if len(right_part) > 0:
        for r_index in right_part: 
            result.append(r_index)            
    return result
###########################################################################################################

############################################ QUICK SORT ###################################################
def quick_sort(used_list):
    helper(used_list, 0, len(used_list) - 1)
    print(used_list)
    
def helper(used_list, left, right):
    if left < right:
        s_point = partition(used_list, left, right)
        
        helper(used_list, left, s_point - 1)
        helper(used_list, s_point + 1, right)

def partition(used_list, left, right):
    pivot = used_list[left]
    done = False
    left_v = left + 1
    right_v = right
    while not done:
        while left_v <= right_v and used_list[left_v] <= pivot:
            left_v += 1
        while used_list[right_v] >= pivot and right_v >= left_v:
            right_v -= 1
        if right_v < left_v:
            done = True
        else:
            used_list[left_v], used_list[right_v] = used_list[right_v], used_list[left_v]
    used_list[left], used_list[right_v] = used_list[right_v], used_list[left]
    return right_v
###########################################################################################################

#print("unsort - ", list_of_nums2)
#print("bubble - ", bubble_sorting(c.deepcopy(list_of_nums2)))
#print()
#print("unsort - ", list_of_nums2)
#print("insert - ", insert_sorting(c.deepcopy(list_of_nums2)))
#print()
#print("unsort - ", list_of_nums2)
#print("insert - ", selection_sort(c.deepcopy(list_of_nums2)))
#print()
#print("unsort - ", list_of_nums2)
#print("merge  - ", merge_sort(c.deepcopy(list_of_nums2)))
print()
print("unsort - ", list_of_nums2)
print("quick  - ", quick_sort(c.deepcopy(list_of_nums2)))
#ÍÀÏÈÑÀÒÜ ÊÂÈÊÑÎĞÒ