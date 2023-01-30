#include <iostream>

using namespace std;

int main()
{
    int math, phy, chem, eng, comp, sum,per;

    sum = math+phy+chem+eng+comp;
    // per = sum / 500 * 100;
    cout << "Enter the Marks of Maths:" << endl;
    cin >> math;

    cout << "Enter the Marks of Physics:" << endl;
    cin >> phy;

    cout << "Enter the Marks of Chemistry:" << endl;
    cin >> chem;

    cout << "Enter the Marks of English:" << endl;
    cin >> eng;

    cout << "Enter the Marks of Computer:" << endl;
    cin >> comp;

    cout << "the total Marks is :" << sum << endl;

    //cout << "the Percentage is :" << per << endl;

   
    for (int sum = 1; sum <= 33; )
    {
        cout<<"Grade is : F "<<sum<<endl;

        break;
    };

 
}