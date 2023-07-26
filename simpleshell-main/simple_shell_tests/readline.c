#include<stdio.h>
#include<stdlib.h>

/*
 *main : program that prints "$ ", wait for the user to enter a command, prints it on the next line.
 *
 *
 *
 *
 */


int main(void){
	char* prompt;
	size_t bufsize = 0;

	printf("$ ");
    	getline(&prompt, &bufsize, stdin);
	printf("%s",prompt);
	free(prompt);
	
	return 0;
}
