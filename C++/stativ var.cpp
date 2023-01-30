
//1st

#include <iostream>
using namespace std;

class abc
{
    int a;
    static int b;

public:
    abc(int x, int y)
    {
        a = x;
        b = y;
    }
    void show()
    {
        cout << a << " " << b;
    }
    static void display()
    {
        cout << b;
    }
};
int abc::b = 0;
int main()
{
    abc obj(10, 20);
    obj.display();
    abc::display();
    return 0;
}


//2nd 


// #include<iostream>
// using namespace std;
// class StaticFunction
// {
//  int code;
//  static int count;
//  int number;
//  public:
//  void setCode(void)
//  {
//   code=++count;
//  }
//  void showCode(void)
//  {
//   cout<<"Object number:"<<code<<"\n";
//  }
//  static void showcount(void)
//  {
//   cout<<"Count:"<<count<<"\n";
//  }
// };

// int StaticFunction :: count;
// int main()
// {
//    StaticFunction obj1,obj2;
//    obj1.setCode();
//    obj2.setCode();
//    StaticFunction::showcount();
//    StaticFunction obj3;
//    obj3.setCode();
//    StaticFunction::showcount();
//    obj1.showCode();
//    obj2.showCode();
//    obj3.showCode();
//    return 0;
// }



// next 

// #include<iostream>
// using namespace std;
// class A
// {
//     public:
//     int a,b,c;
//     void getdata[]
//     {
//         cout<<"\n Enter two numbers";
//         cin>>a>>b;
//         c=a+b;
//         cout<<"\n THe sum of two number"<<c;
//     }
// };
// class B public A
// {
//     pulic:
//     void product ()
//     {
//         cout<<"\n Enter two Number";
//         cin>>a>>b;
//         c=a+b;
//         cout<<"\n the sum is "<<c;
        
//     }
// };
// class C public A
// {
//     public:
//     void null()
//     {
//         cout<<"\n Enter two number";
//         cin>>a>>b;
//         c=a+b;
//         cout<<"\n the sum is"<<c;
//     }
    
// };
// int main()
// {
//     B obj;
//     C obj2;
    
    
    
// }