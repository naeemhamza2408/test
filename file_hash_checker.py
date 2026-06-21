import hashlib

file_path = input("Enter file path: ")

try:
    with open(file_path, "rb") as file:
        sha256 = hashlib.sha256()

        while chunk := file.read(4096):
            sha256.update(chunk)

    print("SHA-256:")
    print(sha256.hexdigest())

except FileNotFoundError:
    print("File not found.")
