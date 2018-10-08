section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!
		
		;rdi = char *str
		;rsi = char val
		;rdx = int strl
		;rcx = i
	
		mov rcx, 0
		
		jmp my_memset_cmp
				
my_memset_loop: 
		mov byte [rdi+rcx*1], sil ; 1 byte of rsi
		inc rcx
				
my_memset_cmp:
		cmp rcx, rdx ; rcx - rdx
		jl my_memset_loop


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;
		;rdi = char *dst
		;rsi = char *src
		;rdx = int len
		;rcx = i
	
		mov rcx, 0
		
		jmp my_strncpy_cmp
				
my_strncpy_loop: 
		mov r8b, [rsi+rcx*1]
		mov [rdi+rcx*1], r8b ; 1 byte of r8
		inc rcx
				
my_strncpy_cmp:
		cmp rcx, rdx ; rcx - rdx
		jl my_strncpy_loop

		
		

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
