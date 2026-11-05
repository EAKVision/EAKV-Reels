#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>

#define BUFFER_SIZE 4096
#define TOTAL_BYTES (100 * 1024 * 1024)

void bench_posix_sys(const char *filename) {
    int fd = open(filename, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) { perror("open"); return; }

    char buffer[BUFFER_SIZE] = {1};
    clock_t start = clock();
    
    for (size_t i = 0; i < TOTAL_BYTES / BUFFER_SIZE; i++) {
        if (write(fd, buffer, BUFFER_SIZE) < 0) {
            perror("write");
            close(fd);
            return;
        }
    }

    clock_t end = clock();
    close(fd);

    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    printf("[POSIX write sys-call] 100MB Written in: %.4f seconds (%.2f MB/s)\n",
           time_spent, 100.0 / time_spent);
}

int main() {
    printf("=== AKV Systems Engine: POSIX I/O Benchmarker ===\n");
    bench_posix_sys("temp_io_test.bin");
    unlink("temp_io_test.bin");
    return 0;
}
