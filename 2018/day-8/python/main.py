import os
import sys

class Node(object):
    def __init__(self, input, index):
        self.input = input
        self.root = index
        
        self.childnum = self.input[self.root]
        self.entrynum = self.input[self.root + 1]
        
        self.children = []
        self.entries = []

    def run(self):
        curadd = 0
        for i in range(self.childnum):
            self.children.append(
                Node(self.input, self.root + 2 + curadd)
            )
            self.children[-1].run()
            curadd += self.children[-1].getFullLength()
        
        start = self.root + 2 + self.getChildrenLength()
        self.entries = [self.input[start + i] for i in range(self.entrynum)]

    def getChildrenLength(self):
        return sum(child.getFullLength() for child in self.children)

    def getFullLength(self):
        return 2 + self.getChildrenLength() + self.entrynum

    def sumEntries(self):
        return sum(child.sumEntries() for child in self.children) + sum(self.entries)

    def __repr__(self):
        return f'Node at index {self.root}'

    # Part 2
    def getValue(self):
        if self.childnum == 0:
            return sum(self.entries)
        elif self.childnum >= 1:
            return sum(
                0 if childi > self.childnum else self.children[childi - 1].getValue() for childi in self.entries
            )

def main(input):
    root = Node(input, 0)
    root.run()
    
    # Part 1 Solution
    print(root.sumEntries())

    # Part 2 Solution
    print(root.getValue())

if __name__ == "__main__":
    TEST_INPUT = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    FILE_PATH = os.path.join(sys.path[0], '..', 'input')
    main(
        list(map(
            int, open(FILE_PATH).read().split()
        ))
    )