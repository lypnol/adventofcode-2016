//C++ example code because the python one is very slow. This code is not optimized and monothread. A multi-thread version is on my todoList.
//compilation on my computer : g++ jules.c -o jules -lcrypto -L/usr/local/opt/openssl/lib -I/usr/local/opt/openssl/include

#include <stdio.h>
#include <string>
#include <openssl/md5.h>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

int main(int argc, const char *argv[])
{
    unsigned char buffer[MD5_DIGEST_LENGTH];
    string hexBuffer = "";
    string password = "";
    int index = 0;
    while(password.length() < 8){
        bool hasRightBegin = false;
        string buff = argv[1]+to_string(index);
        MD5_CTX c;
        MD5_Init(&c);
        MD5_Update(&c, buff.c_str(), buff.length());
        MD5_Final(buffer, &c);
        stringstream ss;
        for(int i = 0;i < 3;i++){
            ss << setfill('0') << setw(2) << hex << (int)buffer[i];
        }
        string result = ss.str();
        if (result.find("00000") == 0)
        {
            password = password+result[5];
        }
        index++;
    }
    cout << password << endl;
    
    return 0;
}