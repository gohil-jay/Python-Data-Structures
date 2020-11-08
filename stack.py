class stack(object):
    def __init__(self, limit):
        self.stack = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    def push(self, data):
        if (len(self.stack) >= self.limit):
            print("Stack Overflow")
        else:
            self.stack.append(data)

    def pop(self):
        if (len(self.stack) <= 0):
            print("Stack Underflow")
            return -1
        else:
            return self.stack.pop()

    def peek(self):
        if (len(self.stack) <= 0):
            print("Stack Underflow")
            return -1
        else:
            return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

def num_conversion(decimal, base):
    myStack = stack()
    while (decimal>0):
        a = decimal % base
        myStack.push(a)
        decimal //= base

    result = ""

    while (myStack.isEmpty() != 1):
        result += str(myStack.pop())

    return result

def reverse_string(string):
    myStack = stack(len(string))
    for i in string:
        myStack.push(i)

    result = ""
    while (myStack.isEmpty() != 1):
        result += str(myStack.pop())
    return result

def isOperand(char):
    return ((ord(char) >= ord('a')) and (ord(char) <= ord('z')) or (ord(char) >= ord('A')) and (ord(char) <= ord('Z')))

def precedence(char):
    if (char == '+' or char == '-'):
        return 1
    if (char == '/' or char == '*'):
        return 2
    if (char == '^'):
        return 3
    else:
        return -1

def infix_to_postfix(myExp, myStack):

    postFix = []

    for i in range(len(myExp)):
        if (isOperand(myExp[i])):
            postFix.append(myExp[i])
        elif(myExp[i] == '('):
            myStack.push(myExp[i])
        elif(myExp[i] == ')'):
            topOperator = myStack.pop()
            while((myStack.isEmpty() != 1) and (topOperator != '(')):
                postFix.append(topOperator)
                topOperator = myStack.pop()
        else:
            while ((myStack.isEmpty() != 1) and (precedence(myExp[i]) <= precedence(myStack.peek()))):
                postFix.append(myStack.pop())
            myStack.push(myExp[i])

    while(myStack.isEmpty() != 1):
        postFix.append(myStack.pop())
    return ' '.join(postFix)

"""               
if __name__ == '__main__':
    myStack = stack()
    for i in range(15):
        myStack.push(i)
    print(myStack)
    myStack.pop()
    print(myStack)
    print("----")
    print(myStack.peek())
    print("----")
    print(myStack.isEmpty())
    print("----")
    print(myStack.size())

print("-----------------------------------")
print(num_conversion(15,2)) #base = 2 === decimal-to-binary
print("-----------------------------------")
print(reverse_string('abcsds'))
"""


print("____________________________________________________")

myExp = 'a+b*(c^d-e)^(f+g*h)-i'
myExp = [x for x in myExp]

myStack = stack(len(myExp))
z = infix_to_postfix(myExp, myStack)
print(z)

#-------------------------------------------------------------------------------------

"""
# Author: OMKAR PATHAK

import Stack

def isOperand(char):
    return (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z'))

def precedence(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char  == '/':
        return 2
    elif char == '^':
        return 3
    else:
        return -1

def infixToPostfix(myExp, myStack):
    postFix = []
    for i in range(len(myExp)):
        if (isOperand(myExp[i])):
            postFix.append(myExp[i])
        elif(myExp[i] == '('):
            myStack.push(myExp[i])
        elif(myExp[i] == ')'):
            topOperator = myStack.pop()
            while(not myStack.isEmpty() and topOperator != '('):
                postFix.append(topOperator)
                topOperator = myStack.pop()
        else:
            while (not myStack.isEmpty()) and (precedence(myExp[i]) <= precedence(myStack.peek())):
                postFix.append(myStack.pop())
            myStack.push(myExp[i])

    while(not myStack.isEmpty()):
        postFix.append(myStack.pop())
    return ' '.join(postFix)

if _name_ == '_main_':
    myExp = 'a+b*(c^d-e)^(f+g*h)-i'
    myExp = [i for i in myExp]
    print('Infix:',' '.join(myExp))
    myStack = Stack.Stack(len(myExp))
    print('Postfix:',infixToPostfix(myExp, myStack))

"""
