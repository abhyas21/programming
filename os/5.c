#include<stdio.h>
void main()
{
    int ms, ps, np, nop, i, j, rem;
    int s[10], fno[10][20];
    printf("Enter memory size: ");
    scanf("%d",&ms);

    printf("Enter page size: ");
    scanf("%d",&ps);

    nop = ms/ps;
    printf("Pages available: %d\n",nop);

    printf("Enter no of processes: ");
    scanf("%d",&np);

    rem=nop;
    for(i=1;i<=np;i++)
    {
        printf("Pages required for P%d: ",i);
        scanf("%d",&s[i]);
        if(s[i]>rem)
        {
            printf("Memory Full\n");
            break;
        }
        rem-=s[i];
        printf("Enter page table: ");
        for(j=0;j<s[i];j++)
            scanf("%d",&fno[i][j]);
    }
}

