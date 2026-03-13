def double(x):
    result = x * 2
    return result

def compute(n):
    doubled = double(n)
    final = doubled + 1
    return final

def main():
    number = 3
    answer = compute(number)
    print(answer)

if __name__ == "__main__":
    main()