#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define ALIGNMENT 8
#define ALIGN(size) (((size) + (ALIGNMENT-1)) & ~(ALIGNMENT-1))

typedef struct BlockHeader {
    size_t size;
    int is_free;
    struct BlockHeader* next;
} BlockHeader;

#define HEADER_SIZE sizeof(BlockHeader)

static BlockHeader* free_list_head = NULL;

BlockHeader* find_free_block(size_t size) {
    BlockHeader* current = free_list_head;
    while (current) {
        if (current->is_free && current->size >= size) {
            return current;
        }
        current = current->next;
    }
    return NULL;
}

void* my_malloc(size_t size) {
    if (size == 0) return NULL;
    
    size_t total_size = ALIGN(size) + HEADER_SIZE;
    BlockHeader* block = find_free_block(ALIGN(size));
    
    if (block) {
        block->is_free = 0;
        return (void*)(block + 1);
    }
    
    void* request = sbrk(total_size);
    if (request == (void*)-1) {
        return NULL; // Out of memory
    }
    
    block = (BlockHeader*)request;
    block->size = ALIGN(size);
    block->is_free = 0;
    block->next = free_list_head;
    free_list_head = block;
    
    return (void*)(block + 1);
}

void my_free(void* ptr) {
    if (!ptr) return;
    BlockHeader* block = (BlockHeader*)ptr - 1;
    block->is_free = 1;
}

void print_heap_status() {
    printf("\n--- Heap Memory Layout ---\n");
    BlockHeader* curr = free_list_head;
    while (curr) {
        printf("[Block @ %p] Size: %zu bytes | Status: %s\n", 
               (void*)curr, curr->size, curr->is_free ? "FREE" : "ALLOCATED");
        curr = curr->next;
    }
    printf("---------------------------\n");
}

int main() {
    printf("=== Custom Memory Allocator Demo ===\n");
    
    int* numbers = (int*)my_malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) numbers[i] = (i + 1) * 10;
    
    char* str = (char*)my_malloc(32 * sizeof(char));
    strcpy(str, "Custom Heap Allocation");
    
    print_heap_status();
    
    printf("\nFreeing integer array...\n");
    my_free(numbers);
    
    print_heap_status();
    
    void* new_block = my_malloc(16);
    printf("\nAllocating 16 bytes (should reuse freed block):\n");
    print_heap_status();
    
    return 0;
}
