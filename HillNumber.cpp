#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n,d,flag=0,a,b;
	cout << "Enter the Number to be Checked" <<endl;
	cin >> n;
	int c=0,dig=0; int x=n;
    while(x>0)
	{
		x =x/10;
		dig++;
	}
	while(n>0)
	{
        d=n%10;
		n=n/10;
		if(d<n%10 && flag==0)
		{
		c++;
		b=1;
		}
		else if (d>n%10)
		{
		flag=1;
		c=c+1;
		a=1;
	}
		
	}
	if (c==dig && a==1 && b==1)
	cout << "Hill Number" <<endl;
	else
	{
	cout << "Nuh" <<endl;
	}
	
}

