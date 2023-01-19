def theatre(row, col, a):
    x = (row // a) + 1 if row % a != 0 else (row // a)
    y = (col // a) + 1 if col % a != 0 else (col // a)
    return x * y

if __name__ == "__main__":
    n, m, a = map(int, input().split(" "))
    print(theatre(n, m, a))