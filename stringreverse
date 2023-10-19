#include <iostream>
int main()
{
    std::string input{};
    std::cin >> input;

    int size = input.length(); // takes length of string
    for (int i = 1; i < size; i++) { //size specifies number of iterations to be made
        for (int j = 0; j < size - i; j++) { 
            if (input[j] > input[j + 1]) { 
                std::swap(input[j], input[j + 1]); //swaps letters to make alphabetical
            }
        }
    }
    std::cout << input;
}
