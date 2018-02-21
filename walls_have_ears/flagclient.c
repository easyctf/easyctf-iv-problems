#define _GNU_SOURCE
#include <netdb.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define SERVER "c1.easyctf.com"
#define PORT 12488

void read_password(char *buf) {
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    FILE *f = fopen("password.txt", "r");
    fgets(buf, 31, f);
    fclose(f);
}

void generate_key(char *password, int seed, char *client_key) {
    int i = 0;
    for (char *c = password; *c; ++c, ++i) {
        unsigned char b = (seed >> (8 * (i % 4))) & (char)0xff;
        client_key[i] = *c ^ b;
    }
    client_key[i] = 0;
}

// credit: https://www.tutorialspoint.com/unix_sockets/socket_client_example.htm
void retrieve_flag(char *client_key) {
    int fd;
    struct sockaddr_in addr;
    struct hostent *server;

    if ((fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("couldn't open socket");
        exit(1);
    }
    if ((server = gethostbyname(SERVER)) == 0) {
        perror("couldn't find server");
        exit(1);
    }

    bzero((char *)&addr, sizeof(struct sockaddr_in));
    addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&addr.sin_addr.s_addr,
          server->h_length);
    addr.sin_port = htons(PORT);

    if (connect(fd, (struct sockaddr *)&addr, sizeof(struct sockaddr_in)) < 0) {
        perror("couldn't connect");
        exit(1);
    }
    // read and ignore the intro message
    char buf[1024];
    read(fd, buf, 1024);

    // now send the password
    write(fd, client_key, strlen(client_key));
    write(fd, "\n", 1);
}

int main() {
    printf("Tell me your player key, and I'll get your flag for you!\n");
    printf("Enter your key: ");

    unsigned int key;
    scanf("%u", &key);
    char password[32];
    read_password(password);
    printf("\n");

    char client_key[32];
    generate_key(password, key, client_key);
    printf("Ok, we've generated a key for you.\n");
    printf("The last 4 characters are: ");
    int L = strlen(client_key);
    for (int i = L - 4; i < L; ++i) {
        printf("%02x ", client_key[i] & 0xff);
    }
    printf("\n\n");

    printf("We'll automatically retrieve the flag now...");
    retrieve_flag(client_key);
    printf("Done!\n\n");
    printf("Here you g.. Oh wait, you haven't paid the Usage Fee.\n");
    printf("Please pay the fee first.\n");
    exit(0);
}