.data
    target:     .ascii "hello WOrld IM gaY"
    .equ TARGET_LEN, 18 

    temp:       .fill 64, 1, 0
    
    sleep_time: 
        .quad 0         
        .quad 10000000 

.text
.global _start

_start:
    mov x19, 0

outer_loop:
    cmp x19, #TARGET_LEN
    b.ge exit

    mov w20, 32

inner_loop:
    mov x0, 1
    ldr x1, =temp
    mov x2, x19
    mov x8, 64
    svc 0

    sub sp, sp, 16
    strb w20, [sp]
    mov x0, 1
    mov x1, sp
    mov x2, 1
    mov x8, 64
    svc 0

    mov w21, 10
    strb w21, [sp]
    mov x0, 1
    mov x1, sp
    mov x2, 1
    mov x8, 64
    svc 0
    add sp, sp, 16

    ldr x22, =target
    ldrb w23, [x22, x19]
    cmp w20, w23
    b.eq match_found

    ldr x0, =sleep_time
    mov x1, 0
    mov x8, 101
    svc 0

    add w20, w20, 1
    cmp w20, #127
    b.lt inner_loop
    
    b match_found

match_found:
    ldr x1, =temp
    strb w20, [x1, x19]
    add x19, x19, 1
    b outer_loop

exit:
    mov x0, 0
    mov x8, 93
    svc 0