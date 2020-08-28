"""
Eli M.
ICSI 431
8.27.20
HW 0
"""

#1 Test Python
def test_print():
    print("This is a test statement.")


#2 Define Objects
def list_set_length():
    items_list= list([1, 2, 3, 4, 3, 2, 1])
    items_set = set({1, 2, 3, 4, 3, 2, 1})
    print(len(items_list))
    print(len(items_set))

#3 Comprehension
def set_intersect(S, T):
    return {x for x in S if(set(T).__contains__(x))}

#4 Tuples   



if __name__ == '__main__':
    test_print()
    list_set_length()
    print(set_intersect( {1,2,3,3}, {3,4,5,6}))