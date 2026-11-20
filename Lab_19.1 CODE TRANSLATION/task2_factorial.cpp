// Task 2 (Source): Recursive C++ factorial function
#include <iostream>
using namespace std;

long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    for (int v : {0, 1, 5, 7}) {
        cout << "factorial(" << v << ") = " << factorial(v) << endl;
    }
    return 0;
}
