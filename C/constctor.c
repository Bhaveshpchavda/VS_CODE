#include<iostream>
#include<iomanip>

using namespace std;
class dc 
{
	public:
	int a,b;
	dc(int x,int y)
	{
		a=x;
		b=y;
		cout<<"sum of two number:"<<(a+b);
		
	}
			
};

int main()
{
	dc ob(20,50);
	
   return 0;
}