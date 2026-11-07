#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>

void handle_signal(int sig) {
    if (sig == SIGUSR1) {
        printf("\n[DAEMON] Received SIGUSR1: Triggering automated matrix audit & sync...\n");
        system("python3 track_reel_performance.py");
    }
}

int main() {
    printf("==================================================\n");
    printf("     EAKV BARE-METAL POSIX BACKGROUND DAEMON      \n");
    printf("==================================================\n");
    printf("[INFO] Daemon running with PID: %d\n", getpid());
    
    // Register signal handler
    signal(SIGUSR1, handle_signal);
    
    // Background idle loop waiting for system signals
    while (1) {
        sleep(10);
    }
    
    return 0;
}
