python
with open("test.txt", "r+") as f:
    f.seek(10)  # Flytter filpekeren til byte 10
    print(f.read(5))  # Leser 5 byte fra posisjon 10