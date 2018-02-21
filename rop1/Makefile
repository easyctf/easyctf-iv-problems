all:
	gcc -fno-stack-protector -o rop1 rop1.c

	chown root:rop1 flag.txt
	chmod 0740 flag.txt

	chown root:rop1 rop1
	chmod 2555 rop1
