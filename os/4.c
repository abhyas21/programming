#include<stdio.h>
#include<unistd.h>
int main()
{
    int fd[2];
    pipe(fd);

    if(fork()==0)
    {
        char msg[]="Hello";
        write(fd[1],msg,sizeof(msg));
    }
    else
    {
        char buf[20];
        read(fd[0],buf,sizeof(buf));
        printf("Received: %s",buf);
    }
}

