import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    archivist_id = input("Input Stream active. Enter archivist archivist_id: ")
    report = input("Input Stream active. Enter status report: ")
    print()
    sys.stdout.write(f"[STANDARD] Archive status from {archivist_id}:"
                     f"{report}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels"
                     "verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()
    print("Three-channel communication test successful.")
