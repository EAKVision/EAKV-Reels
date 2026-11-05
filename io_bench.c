#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
#include <string.h>

#define FILE_SIZE_MB 50
#define BUFFER_SIZE 4096 // 4 KB buffer

double get_time_sec(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
}

void bench_stdio() {
    printf("[1] Benchmarking C stdio (fwrite)...\n");
    char buffer[BUFFER_SIZE];
    memset(buffer, 'A', BUFFER_SIZE);
    
    FILE* fp = fopen("stdio_test.bin", "wb");
    if (!fp) { perror("fopen failed"); return; }
    
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);
    
    size_t total_bytes = (size_t)FILE_SIZE_MB * 1024 * 1024;
    size_t iterations = total_bytes / BUFFER_SIZE;
    
    for (size_t i = 0; i < iterations; i++) {
        fwrite(buffer, 1, BUFFER_SIZE, fp);
    }
    
    fclose(fp);
    clock_gettime(CLOCK_MONOTONIC, &end);
    
    double elapsed = get_time_sec(start, end);
    printf("    Wrote %d MB in %.4f seconds (%.2f MB/s)\n\n", 
           FILE_SIZE_MB, elapsed, FILE_SIZE_MB / elapsed);
    
    unlink("stdio_test.bin");
}

void bench_posix_sys() {
    printf("[2] Benchmarking POSIX Direct System Calls (write)...\n");
    char buffer[BUFFER_SIZE];
    memset(buffer, 'B', BUFFER_SIZE);
    
    int fd = open("posix_test.bin", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) { perror("open failed"); return; }
    
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);
    
    size_t total_bytes = (size_t)FILE_SIZE_MB * 1024 * 1024;
    size_t iterations = total_bytes / BUFFER_SIZE;
    
    for (size_t i = 0; i < iterations; i++) {
        write(fd, buffer, BUFFER_SIZE);
    }
    
    close(fd);
    clock_gettime(CLOCK_MONOTONIC, &end);
    
    double elapsed = get_time_sec(start, end);
    printf("    Wrote %d MB in %.4f seconds (%.2f MB/s)\n\n", 
           FILE_SIZE_MB, elapsed, FILE_SIZE_MB / elapsed);
    
    unlink("posix_test.bin");
}

int main() {
    printf("=== POSIX vs C Standard Library I/O Benchmarker ===\n");
    printf("Test Dataset Size: %d MB | Buffer Size: %d Bytes\n\n", FILE_SIZE_MB, BUFFER_SIZE);
    
    bench_stdio();
    bench_posix_sys();
    
    return 0;
}
