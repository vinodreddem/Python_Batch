'''
Question
=============================================
Write a function that groups a string into parentheses clusters. 
Each cluster should be balanced - Every opening bracket '(' must exist with its matching closing bracket ')' in the same cluster.

Examples
=============================================
split("()()()") ➞ ["()", "()", "()"]
split("((()))") ➞ ["((()))"]
split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]
split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
'''


def bracket_clusterizer(s):
    ''' Insert code here '''


def main():
    pass

def test_set_1():
    tests = []
    tests.append(bracket_clusterizer("()()()") == ["()", "()", "()"])
    tests.append(bracket_clusterizer("((()))") == ["((()))"])
    tests.append(bracket_clusterizer("((()))(())()()(()())") == ["((()))", "(())", "()", "()", "(()())"])
    tests.append(bracket_clusterizer("((())())(()(()()))") == ["((())())", "(()(()()))"])
    passed = 0
    for test in tests:
        if test: passed += 1
    print(f"Set 1: {passed}/4 test cases passed!")

def test_set_2():
    tests = []
    tests.append(bracket_clusterizer("()()()") == ["()", "()", "()"])
    tests.append(bracket_clusterizer("") == [])
    tests.append(bracket_clusterizer("()()(())") == ["()", "()", "(())"])
    tests.append(bracket_clusterizer("(())(())") == ["(())", "(())"])
    tests.append(bracket_clusterizer("((()))") == ["((()))"])
    tests.append(bracket_clusterizer("()(((((((((())))))))))") == ["()", "(((((((((())))))))))"])
    tests.append(bracket_clusterizer("((())()(()))(()(())())(()())") == ["((())()(()))", "(()(())())", "(()())"])
    tests.append(bracket_clusterizer("((()))(())()()(()())") == ["((()))", "(())", "()", "()", "(()())"])
    tests.append(bracket_clusterizer("((())())(()(()()))") == ["((())())", "(()(()()))"])
    tests.append(bracket_clusterizer("(()(()()))()(((()))()(()))(()((()))(())())") == ["(()(()()))", "()", "(((()))()(()))", "(()((()))(())())"])
    passed = 0
    for test in tests:
        if test: passed += 1
    print(f"Set 2: {passed}/10 test cases passed!")

if __name__ == "__main__":  
    main()
    #test_set_1()
    #test_set_2()