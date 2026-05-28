#include <iostream>

using namespace std;

int main() {

    double num1, num2;
    char operation;

    cout << "Simple Calculator" << endl;

    // Input numbers
    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    // Choose operation
    cout << "Choose operation (+, -, *, /): ";
    cin >> operation;

    // Perform calculation
    if (operation == '+') {
        cout << "Result = " << num1 + num2 << endl;
    }
    else if (operation == '-') {
        cout << "Result = " << num1 - num2 << endl;
    }
    else if (operation == '*') {
        cout << "Result = " << num1 * num2 << endl;
    }
    else if (operation == '/') {

        if (num2 == 0) {
            cout << "Division by zero is not possible." << endl;
        }
        else {
            cout << "Result = " << num1 / num2 << endl;
        }
    }
    else {
        cout << "Invalid operation." << endl;
    }

    return 0;
}