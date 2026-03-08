def archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit: new_discovery.txt")
    file = None
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
        ]
    try:
        file = open("new_discovery.txt", "w")
        for entry in entries:
            file.write(entry)
            file.write("\n")
        print("Storage unit created successfully...")
        print()
    except OSError:
        print("Error: Storage unit was not created")
        return
    finally:
        if file:
            file.close()
    print("Inscribing preservation data...")
    for entry in entries:
        print(entry)
    print()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    archive_creation()
