
class LinkList():
    def __init__(self, ll, head):
        self.ll = ll
        self.head = head

    def __repr__(self):
        part = []
        if self.head in self.ll:
            succr = self.head
            while succr != '-1':
                data, succr = self.ll[succr]
                part.append( '{}->'.format(data) )
        return ''.join(part) + 'NULL'

    def print(self, head=None):
        if head == None: head = self.head
        if head in self.ll:
            succr = head
            while succr != '-1':
                data, succr = self.ll[succr]
                print('{}->'.format(data), end='')
        print('NULL')

    def length(self, head=None):
        count = 0
        if head == None: head = self.head
        if head in self.ll:
            while head != '-1':
                count += 1
                head = self.ll[head][1]
        return count

    def tail(self, head=None):
        tails = '-1'
        if head == None: head = self.head
        if head in self.ll:
            while head != '-1':
                tails = head
                head = self.ll[head][1]
        return tails

    def parition_reverse(self, head, length):
        count = 1
        precr, succr = head, self.ll[head][1]
        while succr != '-1' and count < length:
            next_reverse = self.ll[succr][1]
            self.ll[succr][1] = precr
            precr, succr = succr, next_reverse
            count += 1
        self.ll[head][1] = '-1'
        return precr

link_list = {
    '1': ['A', '2'],
    '2': ['B', '3'],
    '3': ['C', '4'],
    '4': ['D', '-1']
}

ll = LinkList(link_list, '1')
print(ll.tail())
# print(ll)


