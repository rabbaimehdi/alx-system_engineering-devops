#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>

#define DELIM " \n"
#define MAX_ALIASES 100

typedef struct
{
	char *name;
	char *value;
} aliast;


ssize_t getline(char **lineptr, size_t *n, FILE *stream);
void execmd(char **argv);
char *get_location(char *command);
char **tokenize(char *linep, char *linep_copy);
void prompt(void);
char *cmd(char *lineptr);
void exec_fork(char **argv);
void freemem(char *mem1, char *mem2, char **mem3);
int exec_builtin(char **args);
char *strn_cat(char *file_path, size_t file_path_len, char path_token, size_t path_token_len, char command);
char *loc(char *path, char *command);


void print_aliases(void);
void handle_alias_command(char **argv);
void print_alias(char *name);
void set_alias(char *name, char *value);
#endif /*End of File*/
