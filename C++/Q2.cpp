#include <iostream>

using namespace std;
struct ans
{
    string name;
    int id;
} candidates[5];
int max(int arr[])
{
    int m = 0;
    for (int i = 0; i < 5; i++)
    {
        if (arr[i] > m)
        {
            m = arr[i];
        }
    }
    return m;
}
int main()
{
    int h1, h2, h3, h4, h5, total = 0, votes[5], maxm;
    for (int i = 0; i < 5; i++)
    {
        cin >> candidates[i].name;
        cin >> candidates[i].id;
    }
    for (int i = 0; i < 5; i++)
    {
        total = total + candidates[i].id;
    }
    for (int i = 0; i < 5; i++)
    {
        votes[i] = candidates[i].id;
    }
    maxm = max(votes);
    for (int i = 0; i < 5; i++)
    {
        cout << candidates[i].name;
        cout << candidates[i].id;
        cout << "Percentage of total votes = " << ((candidates[i].id / total) * 100) << endl;
    }
    for (int i = 0; i < 5; i++)
    {
        if (candidates[i].id == maxm)
        {
            cout << "The winner is " << candidates[i].name << endl;
            break;
        }                                                                                    `                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    }
    return 0;
}