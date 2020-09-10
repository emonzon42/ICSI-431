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
def three_tuples(S):
    return [(i,j,k) for i in S for j in S for k in S if (i+j+k == 0)]

#5 Dictionaries
def dict_init():
    return {'Neo':'Keanu', 'Morpheus':'Laurence', 'Trinity':'Carrie-Anne'}

def dict_find(dlist, k):
    return [i[k] if k in i else 'not present' for i in dlist]

#6 Filereading
def file_line_count(filename):
    f = open(filename, 'r')
    i = 0
    if(f.readable):
        for x in f.readlines():
            i+=1
    f.close()
    return i

#7 Mini Search Engine

if __name__ == '__main__':
    test_print()
    list_set_length()
    print(set_intersect( {1,2,3,3}, {3,4,5,6}))
    print(three_tuples({-4,-2, 1, 2, 5, 0}))
    mydict = dict_init()
    mydict['Neo'] = 'DegrassiTyson'
    print(mydict['Neo'])
    print(dict_find([mydict,{'first':'1', 'Neo':'2'}], 'Neo'))
    print(file_line_count('Homework/HW0/stories.txt'))
    
