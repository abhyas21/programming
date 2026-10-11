#include<stdio.h>
void main()
{
    int buffer[10], bufsize = 10, in = 0, out = 0;
    int produce, consume, choice = 0;
    while(choice != 3)
    {
        printf("\n1. Produce 2. Consume 3. Exit");
        printf("\nEnter choice: ");
        scanf("%d", &choice);
        switch(choice)
        {
            case 1:
                if((in+1)%bufsize == out)
                    printf("Buffer Full");
                else
                {
                    printf("Enter value: ");
                    scanf("%d",&produce);
                    buffer[in]=produce;
                    in=(in+1)%bufsize;
                }
                break;
            case 2:
                if(in==out)
                    printf("Buffer Empty");
                else
                {
                    consume=buffer[out];
                    printf("Consumed=%d",consume);
                    out=(out+1)%bufsize;
                }
                break;
        }
    }
}

