#include<stdio.h>

int main()
{
    int b[10], f[10], i, j, nb, nf;
    printf("Enter blocks: ");
    scanf("%d",&nb);
    printf("Enter files: ");
    scanf("%d",&nf);
    for(i=0;i<nb;i++)
        scanf("%d",&b[i]);
    for(i=0;i<nf;i++)
        scanf("%d",&f[i]);
    for(i=0;i<nf;i++)
    {
        for(j=0;j<nb;j++)
        {
            if(b[j]>=f[i])
            {
                printf("File %d -> Block %d\n",i+1,j+1);
                b[j]-=f[i];
                break;
            }
        }
    }
}

