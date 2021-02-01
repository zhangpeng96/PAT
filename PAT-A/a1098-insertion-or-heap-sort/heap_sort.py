
class Heap():
    def __init__(self, array):
        self.arr = [None] + array
        self.length = len(array)
        self.build_max_heap()

    def __repr__(self):
        return str(self.arr[1:])

    def adjust_down(self, low, high):
        root, child = low, low*2
        while child <= high:
            if child+1 <= high and self.arr[child] < self.arr[child+1]:
                child += 1
            if self.arr[root] >= self.arr[child]:
                break
            else:
                self.arr[root], self.arr[child] = self.arr[child], self.arr[root]
            root = child
            child = root*2

    def build_max_heap(self):
        parent = self.length//2
        while parent:
            self.adjust_down(parent, self.length)
            parent -= 1
        # print(self.arr)

    def heap_sort(self):
        i = self.length
        while i > 1:
            self.arr[1], self.arr[i] = self.arr[i], self.arr[1]
            self.adjust_down(1, i-1)
            i -= 1


seq = [53, 17, 78, 9, 45, 65, 87, 32]
heap = Heap(seq)
print(heap)
heap.heap_sort()
print(heap)
