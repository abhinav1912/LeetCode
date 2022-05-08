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
    def __init__(self, nestedList: [NestedInteger]):
        self.l = []
        self.flatten(nestedList)
        self.i = 0
    
    def flatten(self, l):
        for i in l:
            if i.isInteger():
                self.l.append(i.getInteger())
            else:
                self.flatten(i.getList())

    def next(self) -> int:
        x = self.l[self.i]
        self.i += 1
        return x
    
    def hasNext(self) -> bool:
        return self.i < len(self.l)
