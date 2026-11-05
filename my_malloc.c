#include <stdio.h>
#include <stddef.h>
#include <unistd.h>

typedef struct BlockHeader {
    size_t size;
    int is_free;
    struct BlockHeader* next;
} BlockHeader;

#define HEADER_SIZE sizeof(BlockHeader)
static BlockHeader* head = NULL;

BlockHeader* find_free_block(BlockHeader** last, size_t size) {
    BlockHeader* current = head;
    while (current && !(current->is_free && current->size >= size)) {
        *last = current;
        current = current->next;
    }
    return current;
}

BlockHeader* request_space(BlockHeader* last, size_t size) {
    BlockHeader* block = sbrk(0);
    void* request = sbrk(size + HEADER_SIZE);
    if (request == (void*)-1) return NULL;

    if (last) last->next = block;
    block->size = size;
    block->is_free = 0;
    block->next = NULL;
    return block;
}

void* my_malloc(size_t size) {
    if (size <= 0) return NULL;

    BlockHeader* block;
    if (!head) {
        block = request_space(NULL, size);
        if (!block) return NULL;
        head = block;
    } else {
        BlockHeader* last = head;
        block = find_free_block(&last, size);
        if (!block) {
            block = request_space(last, size);
            if (!block) return NULL;
        } else {
            block->is_free = 0;
        }
    }
    return (void*)(block + 1);
}

void my_free(void* ptr) {
    if (!ptr) return;
    BlockHeader* block = (BlockHeader*)ptr - 1;
    block->is_free = 1;
}

int main() {
    printf("=== AKV Systems Engine: Custom Malloc Allocator ===\n");
    int* data = (int*)my_malloc(10 * sizeof(int));
    if (data) {
        for (int i = 0; i < 10; i++) data[i] = i * 100;
        printf("Allocated array index 5: %d\n", data[5]);
        my_free(data);
        printf("[✓] Memory allocated and freed successfully via sbrk()\n");
    }
    
    void* new_block = my_malloc(16);
    if (new_block) {
        printf("[✓] Second allocation verified at %p\n", new_block);
        my_free(new_block);
    }
    
    return 0;
}
