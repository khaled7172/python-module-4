def recover_ancient_fragments() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    file = None
    try:
        file = open("ancient_fragment.txt", "r")
        content = file.read()
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        print(content)
        print()
    except FileNotFoundError:
        print("Error: Storage vault not found.")
        return
    finally:
        if file:
            file.close()
    print("Data Recovery complete. Storage unit disconnected")


if __name__ == "__main__":
    recover_ancient_fragments()
