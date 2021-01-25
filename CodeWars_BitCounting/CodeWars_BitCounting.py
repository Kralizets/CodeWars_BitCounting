def GetNumber(n):
    result = 0
    while (n > 1):
        if (n % 2 == 1):
            result += 1
        n //= 2

    if (n == 1):
        result += 1
    return result

def main():
    n = 1234
    result = GetNumber(1234)
    print(result)

if __name__ == '__main__':
     main()
