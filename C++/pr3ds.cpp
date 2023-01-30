#include<iostream>
using namespace std;

int main()
{
    int pair;
    cin >> pair;
    pair=pair*2;
    char ps[pair][6];
    for(int i=0;i<pair;i++)
    {
        cin >> ps[i];
    }
    for(int i=0;i<pair;i=i+2)
    {
        for(int j=0;j<6;j++)
        {
            if(ps[i][j]==ps[i+1][j])
            {
                cout << "Y";
            }
            else{
                cout << "N";
            }
        }
        cout << endl;
    }
    return 0;
}