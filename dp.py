# def is_square(n):   
#     return n >= 0 and (n ** 0.5) % 1 == 0

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))



def solve(st):
    if len(st) % 2 != 0:
        return -1
    
    stack = []
    counter = 0

    for p in st: 
        if p == '(':
            stack.append(p)
        elif p == ')' and stack:
            stack.pop()
        elif p == ')':  #stack is empty
            counter += 1
            stack.append(p)
        print(stack)
            
    return counter + len(stack) // 2

# print(solve('))(('))




def solve(st):
    if len(st) % 2 != 0:
        return -1
    
    stack = []
    counter = 0
    for p in st: 
        if p == ')' and stack:
            stack.pop()
        elif p == '(':
            stack.append(p)
        elif p == ')':
            counter += 1
            stack.append(p)
            
    if len(stack) % 2 != 0:
        return -1
    else:
        return counter + len(stack) // 2

# print(solve('))(('))

st = '))(('

def solve(s):
    if len(s) % 2: return -1
    #imagine a simple symmetric random walk; '(' is a step up and ')' is a step down. We must stay above the original position
    height = 0; counter = 0
    for x in s:
        if x == '(':
            height += 1
        else:
            height -= 1
        if height < 0: 
            counter += 1
            height += 2
    #counter is the number of flips from ')' to '(', height//2 number of opposite flips
    return counter + height // 2


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def solve(s):
    l = len(s)
    if l % 2 != 0: return -1
    stack = Stack(); count = 0; i = 0
    while i < len(s):
        if s[i] == "(":
            stack.push(s[i])
        else:
            if stack.is_empty():
                count += 1
            else: stack.pop()
        i += 1
    q = (count + stack.size())//2
    return q if count % 2 == 0 and stack.size() % 2 == 0 else q + 1


def solve(s):
    t = None
    while t != s:
        t, s = s, s.replace('()', '')
    return -1 if len(s) % 2 else sum(1 + (a == tuple(')(')) for a in zip(*[iter(s)] * 2))

def solve(s):
    if len(s) % 2: return -1
    count, swap = 0, 0
    for i,c in enumerate(s):
        count += (c == '(') - (c == ')')
        if count < 0:
            swap += 1 ; count = 1
        elif count > len(s)-i: 
            swap += 1 ; count -= 2
    return swap



def solve(st):
    if len(st) % 2 != 0:
        return -1
    
    stack = []
    counter = 0

    for p in st: 
        print(p)
        if p == '(':
            stack.append('Open')
        elif p == ')' and stack:
            stack.pop()
        elif p == ')':  #stack is empty
            counter += 1
            stack.append('Closed')
        print(f"Stack: {stack}")
        print(f"Counter: {counter}")
        print()
            
    return counter + len(stack) // 2

def solve(s):
    if len(s) % 2 != 0:
        return -1  # If the string length is odd, it's not possible to balance parentheses
    
    stack = []
    reversals_needed = 0
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                reversals_needed += 1
    
    return reversals_needed + len(stack) // 2  # Add half of remaining open parentheses as each 

print(solve('))(('))