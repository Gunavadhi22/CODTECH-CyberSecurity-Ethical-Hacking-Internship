def brute_force(password_list, correct_password):
    print("Starting brute force attack...")
    for password in password_list:
        print(f"Trying password: {password}")
        if password == correct_password:
            print("[SUCCESS] Password found:", password)
            return
    print("[FAILED] Password not found")

if __name__ == "__main__":
    passwords = ["admin", "1234", "password", "root"]
    correct_password = "password"
    brute_force(passwords, correct_password)
