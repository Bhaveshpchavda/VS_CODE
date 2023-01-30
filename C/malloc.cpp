#include <iostream>
#include <stdlib.h>

using namespace std;
int main()
{
 int n;
 char *text;
 
 cout<<"Enter limit of this text : ";
 cin>>n;
 text=(char*)malloc(n*sizeof(char));
 
 cout<<"Enter text is;"<<text;
 
 free(text);

    return 0;
}