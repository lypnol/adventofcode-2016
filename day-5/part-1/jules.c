//C example code because the python one is very slow. This code is not optimized and monothread. A multi-thread version is maybe on my todoList.
//compilation on my computer : gcc jules.c -o julesC -lcrypto -L/usr/local/opt/openssl/lib -I/usr/local/opt/openssl/include

#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

int main(int argc, const char *argv[])
{

    unsigned char buffer[MD5_DIGEST_LENGTH];
    char password[9];
    int index = 0;
    int actualChar = 0;

    while(actualChar < 8){
        char buff[19];
        strncpy(buff,argv[1],9);
        char entier[9];
        sprintf(entier, "%d", index);
        strncat(buff,entier,9);
        char result[7];
        MD5_CTX c;
        MD5_Init(&c);
        MD5_Update(&c, buff, strlen(buff));
        MD5_Final(buffer, &c);
        for(int i = 0;i < 3;i++){
            sprintf(&(result[2*i]),"%02x", buffer[i]);
        }
        if(strncmp(result, "00000", 5) == 0)
        {
            password[actualChar] = result[5];
            actualChar++;
        }
        index++;
    }
    password[8] = 0;
    printf("%s\n",password);
    
    return 0;
}