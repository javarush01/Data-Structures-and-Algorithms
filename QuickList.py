"""
This program was meant to see if dictionaries could store and update the data, such as count, max, and min. However,
theoretically, it is possible that dictionary functions run in O(n) time instead of O(1). Therefore, there is a possibility that
this code could have poor runtime complexity.

"""
class QuickList(object):
    def __init__(self):
        self.qList = []
        self.size = 0
        self.max = None
        self.min = None
        self.index = {}
        self.count = {}

    def push(self, val):
        self.qList += [val]
        self.size += 1
        if val not in self.index:
            self.index[val] = [self.size - 1]
        else:
            self.index[val].append(self.size - 1)

        if val not in self.count:
            self.count[val] = 1
        else:
            self.count[val] += 1
        if not self.max:
            self.max = val
        else:
            if self.max and val > self.max:
                self.max = val
        if not self.min:
            self.min = val
        else:
            if self.min and val < self.min:
                self.min = val

    def pop_right(self):
        t = self.qList[-1]
        self.qList.pop()
        self.size -= 1
        if self.count[t] == 1:
            self.count.pop(t)
        else:
            self.count[t] -= 1
        if len(self.index[t]) == 1:
            self.index.pop(t)
        else:
            self.index[t].pop()
        return t

    def pop_left(self):
        t = self.qList[0]
        self.qList.pop(0)
        self.size -= 1
        if self.count[t] == 1:
            self.count.pop(t)
        else:
            self.count[t] -= 1
        if len(self.index[t]) == 1:
            del self.index[t]
        else:
            self.index[t].pop(0)
        return t

    def get_size(self):
        return self.size

    def get_count(self, val):
        return self.count[val]

    def get_index(self, val):
        return self.index[val]

    def swap(self, index1, index2):
        t = self.qList[index1]
        self.qList[index1] = self.qList[index2]
        self.qList[index2] = t

    def clear(self):
        self.qList = []

    def __str__(self):
        return str(self.qList)
