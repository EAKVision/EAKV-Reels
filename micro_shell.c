#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

#define MAX_INPUT 1024
#define MAX_ARGS 64

void sigint_handler(int sig) {
    printf("\n[micro-shell] Use 'exit' to quit.\nmicro-shell> ");
    fflush(stdout);
}

int main() {
    char input[MAX_INPUT];
    char* args[MAX_ARGS];
    
    signal(SIGINT, sigint_handler);
    
    while (1) {
        printf("micro-shell> ");
        fflush(stdout);
        
        if (!fgets(input, sizeof(input), stdin)) break;
        
        // Remove trailing newline
        input[strcspn(input, "\n")] = '\0';
        
        if (strlen(input) == 0) continue;
        
        // Parse input string into argument tokens
        int arg_count = 0;
        char* token = strtok(input, " ");
        while (token && arg_count < MAX_ARGS - 1) {
            args[arg_count++] = token;
            token = strtok(NULL, " ");
        }
        args[arg_count] = NULL;
        
        // Handle Built-in Commands
        if (strcmp(args[0], "exit") == 0) {
            printf("Exiting micro-shell. Goodbye!\n");
            break;
        }
        if (strcmp(args[0], "cd") == 0) {
            if (args[1] == NULL) {
                chdir(getenv("HOME"));
            } else if (chdir(args[1]) != 0) {
                perror("micro-shell: cd failed");
            }
            continue;
        }
        
        // Fork and Execute Process
        pid_t pid = fork();
        if (pid == 0) {
            // Child process
            if (execvp(args[0], args) == -1) {
                perror("micro-shell execution error");
            }
            exit(EXIT_FAILURE);
        } else if (pid > 0) {
            // Parent process
            int status;
            waitpid(pid, &status, 0);
        } else {
            perror("Fork failed");
        }
    }
    
    return 0;
}
