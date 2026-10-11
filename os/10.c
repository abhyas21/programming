#include<stdio.h>

int main()
{
    int req[20],n,head,i,j,temp;
    printf("Enter no of requests: ");
    scanf("%d",&n);

    for(i=0;i<n;i++)
        scanf("%d",&req[i]);

    printf("Enter head: ");
    scanf("%d",&head);

    for(i=0;i<n;i++)
        for(j=i+1;j<n;j++)
            if(req[i]>req[j])
            {
                temp=req[i];
                req[i]=req[j];
                req[j]=temp;
            }

    printf("SCAN order:\n");

    for(i=0;i<n;i++)
        if(req[i]>=head)
            printf("%d ",req[i]);

    for(i=n-1;i>=0;i--)
        if(req[i]<head)
            printf("%d ",req[i]);
}

