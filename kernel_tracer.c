#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

void log_trace(const char *phase, void *ptr, size_t bytes) {
    printf("[EAKV-TRACER] %-12s | ADDR: %p | SIZE: %zu bytes | STATUS: OK\n", phase, ptr, bytes);
}

int main() {
    printf("========================================================\n");
    printf("   EAKV REAL-TIME C MEMORY & SIGNAL TRACE MONITOR       \n");
    printf("========================================================\n");
    
    for (int i = 0; i < 5; i++) {
        size_t sz = (i + 1) * 1024 * 64;
        void *p = malloc(sz);
        if (p) {
            log_trace("MALLOC_ALLOC", p, sz);
            usleep(100000);
            free(p);
            log_trace("FREE_CLEANUP", p, 0);
        }
    }
    printf("========================================================\n");
    printf("[COMPLETE] Deterministic trace cycle finished cleanly.\n");
    return 0;
}
