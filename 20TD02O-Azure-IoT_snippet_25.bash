# Installere AFL
sudo apt-get install afl

# Kompilere målprogrammet med AFL
afl-gcc -o test_program test_program.c

# Kjøre AFL fuzzer
afl-fuzz -i input_dir -o output_dir ./test_program