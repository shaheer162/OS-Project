#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int size;
int *Array;
int frame_size;
int max_range;

void Input(int Algo_type) {
    cout << "Enter Size of Data: ";
    cin >> size;
    Array = new int[size];
    
    if (Algo_type == 1) {
        cout << "Enter Maximum Range of Reference String: ";
        cin >> max_range;
        srand(time(0));
        cout << "Reference String is: ";
        for (int i = 0; i < size; i++) {
            Array[i] = rand() % (max_range + 1);
            cout << Array[i] << " ";
        }
        cout << endl;
    } else if (Algo_type == 2) {
        cout << "Enter Data You Want (Reference String): ";
        for (int i = 0; i < size; i++) {
            cin >> Array[i];
        }
    }

    cout << "Enter Frame Size: ";
    cin >> frame_size;
    cout << "\nAlgorithm\tPageFaults\tHitCount\tPage_Fault-Ratio\tHit-Ratio\n";
}

class BitArray {
public:
    int data;
    bool bit;
    BitArray(int value = -1, bool bol = false) : data(value), bit(bol) {}
};

class Node {
public:
    int data;
    Node *next;
    Node(int value = -1, Node *nood = nullptr) : data(value), next(nood) {}
};

class Queue {
    Node *head;
public:
    Queue() : head(nullptr) {}

    void Enqueue(int value) {
        Node *newNode = new Node(value);
        if (!head) {
            head = newNode;
        } else {
            Node *temp = head;
            while (temp->next) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }

    void Dequeue() {
        if (!head) return;
        Node *temp = head;
        head = head->next;
        delete temp;
    }

    bool Check(int value) {
        Node *temp = head;
        while (temp) {
            if (temp->data == value) return true;
            temp = temp->next;
        }
        return false;
    }

    int Size() {
        int count = 0;
        Node *temp = head;
        while (temp) {
            count++;
            temp = temp->next;
        }
        return count;
    }

    bool IsEmpty() {
        return head == nullptr;
    }

    void Remove(int value) {
        if (!head) return;
        if (head->data == value) {
            Dequeue();
            return;
        }
        Node *temp = head;
        while (temp->next && temp->next->data != value) {
            temp = temp->next;
        }
        if (temp->next) {
            Node *toDelete = temp->next;
            temp->next = toDelete->next;
            delete toDelete;
        }
    }

    void Traverse() {
        Node *temp = head;
        while (temp) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    ~Queue() {
        while (!IsEmpty()) {
            Dequeue();
        }
    }
};

// Add similar corrections for `Stack`, `FIFO`, `LRU`, and `SCA` classes.

void End() {
    cout << "\n\nThank you for using this system!\n";
    exit(0);
}

int choice(int x) {
    int choise;
    cout << "\nEnter your choice: ";
    cin >> choise;
    while (choise < 1 || choise > x) {
        cout << "Invalid choice! Try again: ";
        cin >> choise;
    }
    return choise;
}

int Menu() {
    cout << "\n1-> Enter Data Automatically\n";
    cout << "2-> Enter Data Manually\n";
    cout << "3-> Exit\n";
    int x = choice(3);
    return x;
}

int main() {
    int x = Menu();
    if (x == 1 || x == 2) {
        Input(x);
        // Call algorithms here (FIFO, LRU, SCA).
        delete[] Array;
        main(); // Recursive for testing, replace with loop in production.
    } else {
        End();
    }
}
