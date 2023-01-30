#include <stdio.h>

int main()
{
    int arr[5], a, i, o;
    scanf("%d", &a);
    for (i = 0; i < a; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (i = 0; i < a; i++)
    {
        printf("%d ", arr[i]);
    }
    scanf("%d", &o);
    arr[a] = o;
    printf("\n");
    for (i = 0; i <= a; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}