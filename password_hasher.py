import hashlib

password = input("Enter password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("SHA-256 Hash:")
print(hashed_password)
