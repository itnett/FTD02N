all: myapp

myapp: main.o util.o
	gcc -o myapp main.o util.o

main.o: main.c
	gcc -c main.c

util.o: util.c
	gcc -c util.c

clean:
	rm -f myapp *.o