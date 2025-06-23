# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        # Помещаем элементы в стек в обратном порядке
        for el in nestedList[::-1]:
            self.stack.append(el)
    
    def next(self):
        # Гарантированно возвращает целое число
        return self.stack.pop().getInteger()
    
    def hasNext(self):
        # Пока стек не пуст
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            lst = top.getList()
            for el in lst[::-1]:
                self.stack.append(el)
        return False