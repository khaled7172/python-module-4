if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as file:
            content = file.read()
            print("Vault connection established with failsafe protocols")
            print()
            print("SECURE EXTRACTION:")
            print(content)
            print()
    except FileNotFoundError:
        print("Vault connection could not be established with "
              "failsafe protocols")
    print("SECURE PRESERVATION:")
    vault_content = ""
    try:
        with open("security_protocols.txt", "r") as file:
            vault_content = file.read()
    except OSError:
        print("Secure read failed")
    try:
        with open("classified_data2.txt", "w+") as file:
            file.write(vault_content)
            file.seek(0)
            print(file.read())
            print("Vault automatically sealed upon completion")
    except OSError:
        print("Secure vault operation failed")
    print()
    print("All vault operations completed with maximum security.")
