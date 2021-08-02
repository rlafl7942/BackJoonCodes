str=list(map(str,input()))
str.reverse()
class Stack(list):
    def __init__(self):
        self.top=[]
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()
    def isEmpty(self):
        if len(self.top)==0:
            return True
        else:
            return False
input=Stack()
compare=Stack()
result=0
for i in str:
    input.push(i)
while True:
    tmp=input.pop()
    if tmp=='(':
        compare.push(tmp)
    elif tmp=='[':
        compare.push(tmp)
    elif tmp==')':
        if compare.pop()=='(':
            result=result+2
    elif tmp==']':
        if compare.pop()==']':
            result=result+3


