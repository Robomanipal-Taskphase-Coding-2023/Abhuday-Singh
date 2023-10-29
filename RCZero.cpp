#include <iostream> 
#include <vector>
using namespace std; 
int main()
{
    int r,c,i,j,k;
    cout << "Enter rows and columns in the array: "; 
    cin >> r >> c; 
    int a[r][c];
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            cin >> a[i][j];
        }
    }
for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            if(a[i][j]==0)
            {
                for(k=0;k<r;k++)
                a[i][k]=0;
            }
        }
    }


  for (int i = 0; i < r; i++) { 

        for (int j = 0; j < c; j++) { 

            cout << a[i][j] << ' '; 

        } 

        cout << endl; 

    } 

}
