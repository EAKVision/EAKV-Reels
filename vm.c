#include <stdio.h>
#include <stdlib.h>

#define STACK_MAX 256
#define CODE_MAX 1024

typedef enum {
    OP_PUSH,
    OP_ADD,
    OP_PRINT,
    OP_HALT
} OpCode;

typedef struct {
    int stack[STACK_MAX];
    int sp; // Stack pointer
    int pc; // Program counter
    int code[CODE_MAX];
} VirtualMachine;

void vm_init(VirtualMachine* vm, int* program, int size) {
    vm->sp = -1;
    vm->pc = 0;
    for (int i = 0; i < size; i++) {
        vm->code[i] = program[i];
    }
}

void vm_run(VirtualMachine* vm) {
    int running = 1;
    while (running) {
        int instruction = vm->code[vm->pc++];
        switch (instruction) {
            case OP_PUSH: {
                int value = vm->code[vm->pc++];
                if (vm->sp < STACK_MAX - 1) {
                    vm->stack[++vm->sp] = value;
                } else {
                    fprintf(stderr, "Stack Overflow!\n");
                    running = 0;
                }
                break;
            }
            case OP_ADD: {
                if (vm->sp >= 1) {
                    int b = vm->stack[vm->sp--];
                    int a = vm->stack[vm->sp--];
                    vm->stack[++vm->sp] = a + b;
                } else {
                    fprintf(stderr, "Stack Underflow on ADD!\n");
                    running = 0;
                }
                break;
            }
            case OP_PRINT: {
                if (vm->sp >= 0) {
                    printf("[VM Output] Top of Stack: %d\n", vm->stack[vm->sp]);
                } else {
                    fprintf(stderr, "Stack Empty on PRINT!\n");
                }
                break;
            }
            case OP_HALT:
            default:
                running = 0;
                break;
        }
    }
}

int main() {
    printf("=== Elite System: Custom Stack Bytecode VM ===\n");
    
    // Bytecode Program: Push 15, Push 25, Add them, Print result, Halt
    int program[] = {
        OP_PUSH, 15,
        OP_PUSH, 25,
        OP_ADD,
        OP_PRINT,
        OP_HALT
    };
    
    VirtualMachine vm;
    vm_init(&vm, program, sizeof(program) / sizeof(program[0]));
    vm_run(&vm);
    
    return 0;
}
