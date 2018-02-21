#define _GNU_SOURCE
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void get_flag()
{
        system("/bin/cat flag.txt");
}

void get_input()
{
        char inp[64];
        gets(inp);
        printf("You said: %s\n", inp);
}

int main(int argc, char** argv)
{
        gid_t gid = getegid();
        setresgid(gid,gid,gid);
        get_input();
        return 0;
}
