def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # dummy credentials
    if username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid credentials")


if __name__ == "__main__":
    login()
