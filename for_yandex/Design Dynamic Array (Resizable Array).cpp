class DynamicArray {

private:
    int* vec;
    int capacity;
    int size;

public:
    DynamicArray(int capacity):capacity(capacity), size(0) {
        vec = new int[capacity];
    }

    int get(int i) {
        return vec[i];
    }

    void set(int i, int n) {
        vec[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        vec[size] = n;
        ++size;
    }

    int popback() {
        if (size == 0)
            return -1;
        int el = vec[size-1];
        --size;
        return el;
    }

    void resize() {
        capacity *= 2;
        int* newArr = new int[capacity];
        for (int i=0; i<size; ++i) {
            newArr[i] = vec[i];
        }
        delete[] vec;
        vec = newArr;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};