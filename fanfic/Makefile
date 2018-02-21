all:
	gcc -m32 -std=c99 -Wall -fno-stack-protector fanfic.c -o fanfic

	chown root:fanfic flag.txt
	chmod 0740 flag.txt

	chown root:fanfic fanfic
	chmod 2555 fanfic
