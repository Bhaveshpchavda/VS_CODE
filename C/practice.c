#include <stdio.h>
#include <math.h>

int main()
{
    int sal, work_hours;
    char emp;  
    printf("c-clark\n t-teacher\n p-principle\n enter employee initial:");
    scanf("%c", &emp);

    printf("enter number of working hours:");
    scanf("%d", &work_hours);

    if (emp == 'c')  
    {
        if (work_hours >= 50)
        {
            sal = (44 * 100) + (6 * 200);
            printf("clark salary=%d", sal);
        }
        else if (44 <= work_hours && work_hours < 50)  
        {
            sal = (44 * 100) + (work_hours - 44) * 200;
            printf("clark salary=%d", sal);
        }
        else if (work_hours < 44)
        {
            sal = work_hours * 100;
            printf("clark salary=%d", sal);
        }
    }
    else if (emp == 't')  
    {
        if (work_hours >= 50)
        {
            sal = (44 * 200) + (6 * 200);
            printf("teacher salary=%d", sal);
        }
        else if (44 <= work_hours && work_hours < 50)  
        {
            sal = (44 * 200) + (work_hours - 44) * 400;
            printf("teacher salary=%d", sal);
        }
        else if (work_hours < 44)
        {
            sal = work_hours * 200;
            printf("teacher salary=%d", sal);
        }
    }
    else if (emp == 'p')  
    {
        if (work_hours >= 50)
        {
            sal = (44 * 400) + (6 * 800);
            printf("principle salary=%d", sal);
        }
        else if (44 <= work_hours && work_hours < 50)  
        {
            sal = (44 * 400) + (work_hours - 44) * 800;
            printf("principle salary=%d", sal);
        }
        else if (work_hours < 44)
        {
            sal = work_hours * 400;
            printf("principle salary=%d", sal);
        }
    }

    return 0;
}
