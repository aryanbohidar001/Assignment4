try:
    with open("sample.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            print(f"line{i}: {line.strip()}")
except FileNotFoundError:
    print("Error:The file 'sample.txt' was not found.")
