class BinaryHeap:
    # initialize heap
    def __init__(self, root_value, is_max_heap):
        self.root_value = root_value
        self.is_max_heap = is_max_heap
        self.heap_array = [root_value]

    # add value to end of heap array and restore the heap
    def push(self, value):
        self.heap_array.append(value)
        self.heapify_up()

    # return the value at the root of the heap tree
    def peek(self):
        return self.heap_array[0]

    # switch the root of the heap tree with the bottom right-most child, return the old root, delete the root, and restore the heap
    def pop(self):
        self.heap_array[0], self.heap_array[-1] = self.heap_array[-1], self.heap_array[0]
        popped_value = self.heap_array[-1]
        del self.heap_array[-1]
        self.heapify_down()
        return popped_value

    # restore the heap by working up the heap tree as necessary with the bottom rightmost child
    def heapify_up(self):
        current_index = len(self.heap_array) - 1
        while current_index > 0:
            parent_index = self.get_parent_index(current_index)
            if self.is_max_heap and self.heap_array[parent_index] < self.heap_array[current_index]:
                self.heap_array[parent_index], self.heap_array[current_index] = self.heap_array[current_index], self.heap_array[parent_index]
                current_index = parent_index
                continue
            elif not self.is_max_heap and self.heap_array[parent_index] > self.heap_array[current_index]:
                self.heap_array[parent_index], self.heap_array[current_index] = self.heap_array[current_index], self.heap_array[parent_index]
                current_index = parent_index
                continue
            break

    # restore the heap by working down the heap tree as necessary with the root value
    def heapify_down(self):
        current_index = 0
        while self.index_exists(self.get_left_child_index(current_index)):
            left_child_index = self.get_left_child_index(current_index)
            right_child_index = self.get_right_child_index(current_index)
            if not self.index_exists(right_child_index):
                right_child_index = left_child_index
            if self.is_max_heap:
                if self.heap_array[left_child_index] >= self.heap_array[right_child_index] and self.heap_array[current_index] < self.heap_array[left_child_index]:
                    self.heap_array[left_child_index], self.heap_array[current_index] = self.heap_array[current_index], self.heap_array[left_child_index]
                    current_index = left_child_index
                    continue
                elif self.heap_array[current_index] < self.heap_array[right_child_index]:
                    self.heap_array[right_child_index], self.heap_array[current_index] = self.heap_array[current_index], self.heap_array[right_child_index]
                    current_index = right_child_index
                    continue
            else:
                if self.heap_array[left_child_index] <= self.heap_array[right_child_index] and self.heap_array[current_index] > self.heap_array[left_child_index]:
                    self.heap_array[left_child_index], self.heap_array[current_index] = self.heap_array[current_index], self.heap_array[left_child_index]
                    current_index = left_child_index
                    continue
                elif self.heap_array[current_index] > self.heap_array[right_child_index]:
                    self.heap_array[right_child_index], self.heap_array[current_index] = self.heap_array[current_index], self.heap_array[right_child_index]
                    current_index = right_child_index
                    continue
            break

    # return true if the index exists in the heap_array, if it is out of index return false
    def index_exists(self, index):
        try:
            print("index exists")
            value = self.heap_array[index]
            return True
        except:
            print("Index doesn't exist")
            return False

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return (index * 2) + 1

    def get_right_child_index(self, index):
        return (index * 2) + 2

    def get_heap_array(self):
        return self.heap_array

# work with the binary heap
my_heap = BinaryHeap(5, False)
my_heap.push(7)
my_heap.push(3)
my_heap.push(10)
my_heap.push(2)
my_heap.push(-5)
my_heap.push(100)
my_heap.push(150)
my_heap.push(-10)
my_heap.push(23)
my_heap.push(58)
my_heap.push(73)
my_heap.push(-1)
my_heap.push(-3)
my_heap.push(-9)
print(my_heap.get_heap_array())
print(my_heap.pop())
print(my_heap.peek())
print(my_heap.get_heap_array())
print(my_heap.pop())
print(my_heap.get_heap_array())
print(my_heap.pop())
print(my_heap.get_heap_array())
print(my_heap.pop())
print(my_heap.get_heap_array())
print(my_heap.pop())
print(my_heap.get_heap_array())
print(my_heap.pop())
print(my_heap.get_heap_array())