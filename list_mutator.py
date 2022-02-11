'''
Question
=============================================
Write a class 'Mutate' with a data member 'lst'.
This data member will hold a list of numbers

The following methods need to be implemented that directly mutate 'lst'
repeat(n): Repeat lst 'n' times.
add(x): Adds 'x' to the end of the lst.
remove(m, n): Removes all elements between indices 'm' and 'n' INCLUSIVE in lst.
concat(x): concatenates lst with 'x' (ANOTHER LIST).

Examples
=============================================
lst = [1, 2, 3, 4]
repeat(lst, 3) ➞ [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4] 
add(lst, 1) ➞ [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1]
remove(lst, 1, 12) ➞ [1]
concat(lst, [3, 4]) ➞ [1, 3, 4]
'''


''' Insert code here '''
    


def main():
    pass

def test_set_1():
    tests = []
    obj = Mutate([1, 2, 3, 4])
    tests.append(obj.lst == [1, 2, 3, 4])
    obj.repeat(3)
    tests.append(obj.lst == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
    obj.add(1)
    tests.append(obj.lst == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1])
    obj.remove(1, 12)
    tests.append(obj.lst == [1])
    obj.concat([3,4])
    tests.append(obj.lst == [1, 3, 4])
    passed = 0
    for test in tests:
        if test: passed += 1
    print(f"Set 1: {passed}/5 test cases passed!")

def test_set_2():
    tests = []
    obj = Mutate([5,2,3])
    tests.append(obj.lst == [5,2,3])
    obj.repeat(4)
    tests.append(obj.lst == [5,2,3,5,2,3,5,2,3,5,2,3])
    obj.add(1)
    obj.add(0)
    tests.append(obj.lst == [5,2,3,5,2,3,5,2,3,5,2,3,1,0])
    obj.remove(1,1)
    obj.remove(2,10)
    tests.append(obj.lst == [5,3,1,0])
    obj.concat([3,4])
    tests.append(obj.lst == [5,3,1,0,3,4])
    passed = 0
    for test in tests:
        if test: passed += 1
    print(f"Set 2: {passed}/5 test cases passed!")

if __name__ == "__main__":  
    main()
    #test_set_1()
    #test_set_2()