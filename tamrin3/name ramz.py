def main():
    items = input().split()
    items.sort(key=lambda x: int(x[1:]))
    result = ''.join(item[0] for item in items)
    print(result)

if __name__ == "__main__":
    main()
