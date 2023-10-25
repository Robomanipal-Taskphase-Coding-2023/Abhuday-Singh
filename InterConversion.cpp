#include <iostream>
#include <cmath>
using namespace std;
char hexa(int n)
{
    if(n>=0 and n<=9)
    return char(48+n);
    else return char(65+n-10);
}
int main()
{
    int num, n, i = 0, j = 0, k = 0;
    cout << "The decimal no: ";
    cin >> num;
    n = num;
    cout << "\nBinary Representation: ";
    while (n >= pow(2, i))
        i++;
    int bi[i];
    for (j = 0; j < i; j++)
        bi[j] = 0;
    while (n > 0)
    {
        while (n >= pow(2, k))
            k++;
        k--;
        bi[k] = 1;
        n -= pow(2, k);
        k = 0;
    }
    for (int z = i - 1; z >= 0; z--)
        cout << bi[z];


    cout << "\n\nOctal Representation: ";
    n = num, i = 0, j = 0, k = 0;
    while (n >= pow(8, i))
        i++;
    int oct[i];
    for (j = 0; j < i; j++)
        oct[j] = 0;
    while (n > 0)
    {
        while (n >= pow(8, k))
            k++;
        k--;
        int c = n / pow(8, k);
        oct[k] = c;
        n -= c * pow(8, k);
        k = 0;
    }
    for (int z = i - 1; z >= 0; z--)
        cout << oct[z];
    cout<<"\n\nHexadecimal Representation: ";
    n=num,i=0,j=0,k=0;
        while (n >= pow(16, i))
        i++;
    char hex[i];
    for (j = 0; j < i; j++)
        hex[j] = 0;
    while (n > 0)
    {
        while (n >= pow(16, k))
            k++;
        k--;
        int w=n/pow(16,k);
        char ch=hexa(w);
        hex[k] = ch;
        n -= w*pow(16, k);
        k = 0;
    }
    for (int z = i - 1; z >= 0; z--)
        cout << hex[z];
    cout<<endl<<endl;
}
