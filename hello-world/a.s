.text
    output: .asciz "Hello World!\n"
.global _start
_start:
    pushq   %rbp
    movq    %rsp, %rbp
    movq    $1, %rax
    movq    $1, %rdi
    movq    $output, %rsi
    movq    $13, %rdx
    syscall
    movq    $60, %rax
    xorq    %rdi, %rdi
    syscall
