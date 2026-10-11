#include<stdio.h>

int main()
{
    int fr[3], page[12]={2,3,2,1,5,2,4,5,3,2,5,2};
    int i,j,pf=0,top=0;

    for(i=0;i<3;i++)
        fr[i]=-1;

    for(j=0;j<12;j++)
    {
        int found=0;
        for(i=0;i<3;i++)
            if(fr[i]==page[j])
                found=1;

        if(!found)
        {
            fr[top]=page[j];
            top=(top+1)%3;
            pf++;
        }
    }

    printf("Page Faults=%d",pf);
}

