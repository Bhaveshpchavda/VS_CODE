#include <stdio.h>
int main()
{
    int arry[5];
    for (int i = 0; i < 5; i++)
    {

        scanf("%d", &arry[i]);
    }
    for (int i = 0; i < 5; i++)
    {
        if (arry[i] % 3 == 0)
        {
            printf("Multiple of 3: %d ", arry[i]);
        }
        if (arry[i] % 5 == 0)
        {
            printf("Multiple of 5: %d ", arry[i]);
        }
    }
    return 0;
}