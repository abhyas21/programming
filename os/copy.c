#include<stdio.h>
#include<fcntl.h>
#include<sys/types.h>
#include<unistd.h>
int main(int argc, char *argv[])
{
    int f1, f2, n;
    char buf[50];
    if(argc != 3)
    {
        printf("Usage: %s source destination\n", argv[0]);
        return 1;
    }
    f1 = open(argv[1], O_RDONLY);
    f2 = open(argv[2], O_WRONLY | O_CREAT, 0777);
    while((n = read(f1, buf, 50)) > 0)
        write(f2, buf, n);
    close(f1);
    close(f2);
    printf("File Copied Successfully\n");
}

