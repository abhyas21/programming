#include<stdio.h>
int main()
{
    int start,len,i;
    printf("Enter start and length: ");
    scanf("%d %d",&start,&len);

    printf("Blocks allocated:\n");

    for(i=0;i<len;i++)
        printf("%d ",start+i);
}

