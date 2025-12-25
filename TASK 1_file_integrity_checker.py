import hashlib

def calculate_hash(file_path):
    """
    This function calculates SHA-256 hash of a file
    """
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def main():
    file_path = input("Enter file name to monitor: ")

    # Calculate original hash
    original_hash = calculate_hash(file_path)
    if original_hash is None:
        print("File not found!")
        return

    print("\nOriginal Hash Value:")
    print(original_hash)

    input("\nModify the file if needed, then press Enter...")

    # Calculate new hash
    new_hash = calculate_hash(file_path)
    print("\nNew Hash Value:")
    print(new_hash)

    # Compare hash values
    if original_hash == new_hash:
        print("\nFile integrity maintained. No changes detected.")
    else:
        print("\nWarning! File integrity violated. File has been modified.")

if __name__ == "__main__":
    main()
