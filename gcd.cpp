
#include <iostream>
using namespace std;
int fGCD(int a, int b) {
    while (b != 0) {
        int c;
        c = b;
        b = a % b;
        a = c;
    }
    return a;
}
int main() {
    int num1, num2, gcd;

    cout << "Enter the first number: ";
    cin >> num1;

    cout << "Enter the second number: ";
    cin >> num2;

    gcd = fGCD(num1, num2);

    cout << "The GCD is " << gcd;
}
