n = int(input())

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(str(n) + "\n")
    for i in range(n):
        f.write(str(4 + 2 * i) + "\n")