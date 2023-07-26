#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World! How are you doing,?";
    char delimiters[] = " ,!";
    char* token;

    token = strtok(str, delimiters);  

    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, delimiters); 
    }

    return 0;
}
