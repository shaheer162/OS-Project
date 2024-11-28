import random

class PageReplacement:
    def __init__(self):
        self.size = 0
        self.frame_size = 0
        self.array = []

    def input_data(self, algo_type):
        self.size = int(input("Enter Size of Data: "))
        if algo_type == 1:
            max_range = int(input("Enter Maximum Range of Reference String: "))
            self.array = [random.randint(0, max_range) for _ in range(self.size)]
            print("Reference String is: ", self.array)
        elif algo_type == 2:
            self.array = list(map(int, input("Enter Reference String (space-separated): ").split()))
        
        self.frame_size = int(input("Enter Frame Size: "))
        print("\nAlgorithm\tPage Faults\tHit Count\tPage Fault Ratio\tHit Ratio")

class FIFO:
    def __init__(self, size, frame_size, array):
        self.size = size
        self.frame_size = frame_size
        self.array = array
        self.queue = []
        self.page_faults = 0
        self.hits = 0

    def run(self):
        for page in self.array:
            if page not in self.queue:
                if len(self.queue) < self.frame_size:
                    self.queue.append(page)
                else:
                    self.queue.pop(0)
                    self.queue.append(page)
                self.page_faults += 1
            else:
                self.hits += 1
        
        self.print_results("FIFO")

    def print_results(self, algo_name):
        fault_ratio = (self.page_faults / self.size) * 100
        hit_ratio = (self.hits / self.size) * 100
        print(f"{algo_name}\t\t{self.page_faults}\t\t{self.hits}\t\t{fault_ratio:.2f}%\t\t{hit_ratio:.2f}%")

class LRU:
    def __init__(self, size, frame_size, array):
        self.size = size
        self.frame_size = frame_size
        self.array = array
        self.queue = []
        self.page_faults = 0
        self.hits = 0

    def run(self):
        for page in self.array:
            if page not in self.queue:
                if len(self.queue) < self.frame_size:
                    self.queue.append(page)
                else:
                    # Evict the least recently used (front of queue)
                    self.queue.pop(0)
                    self.queue.append(page)
                self.page_faults += 1
            else:
                # Move accessed page to the most recently used position
                self.queue.remove(page)
                self.queue.append(page)
                self.hits += 1
        
        self.print_results("LRU")

    def print_results(self, algo_name):
        fault_ratio = (self.page_faults / self.size) * 100
        hit_ratio = (self.hits / self.size) * 100
        print(f"{algo_name}\t\t{self.page_faults}\t\t{self.hits}\t\t{fault_ratio:.2f}%\t\t{hit_ratio:.2f}%")

class SCA:
    def __init__(self, size, frame_size, array):
        self.size = size
        self.frame_size = frame_size
        self.array = array
        self.stack = []
        self.bits = []
        self.page_faults = 0
        self.hits = 0

    def run(self):
        for page in self.array:
            if page not in self.stack:
                if len(self.stack) < self.frame_size:
                    self.stack.append(page)
                    self.bits.append(0)
                else:
                    while True:
                        if self.bits[0] == 0:
                            self.stack.pop(0)
                            self.bits.pop(0)
                            self.stack.append(page)
                            self.bits.append(0)
                            break
                        else:
                            self.bits.pop(0)
                            self.bits.append(0)
                            self.stack.append(self.stack.pop(0))
                self.page_faults += 1
            else:
                idx = self.stack.index(page)
                self.bits[idx] = 1
                self.hits += 1

        self.print_results("SCA")

    def print_results(self, algo_name):
        fault_ratio = (self.page_faults / self.size) * 100
        hit_ratio = (self.hits / self.size) * 100
        print(f"{algo_name}\t\t{self.page_faults}\t\t{self.hits}\t\t{fault_ratio:.2f}%\t\t{hit_ratio:.2f}%")

def menu():
    print("\n1-> Enter Data Automatically")
    print("2-> Enter Data Manually")
    print("3-> Exit")

    choice = int(input("\nEnter your choice: "))
    if choice in [1, 2]:
        page_replacement = PageReplacement()
        page_replacement.input_data(choice)

        fifo = FIFO(page_replacement.size, page_replacement.frame_size, page_replacement.array)
        lru = LRU(page_replacement.size, page_replacement.frame_size, page_replacement.array)
        sca = SCA(page_replacement.size, page_replacement.frame_size, page_replacement.array)

        fifo.run()
        lru.run()
        sca.run()
    elif choice == 3:
        print("\nThank you for using the system!")
        exit()
    else:
        print("Invalid choice! Try again.")
        menu()

if __name__ == "__main__":
    menu()
