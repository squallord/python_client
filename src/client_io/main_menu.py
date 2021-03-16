
def main_menu():
    print("\nMENU\n")
    print("[1] - For file and directories")
    print("[2] - For PID")
    print("[3] - Exit")
    chosen_option = int(input("\nType an option: "))

    if chosen_option == 1:
        return 1

    if chosen_option == 2:
        return 2

    if chosen_option == 3:
        return 3
