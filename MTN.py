def display_menu(menu):
    for key, value in menu.items():
        print(f"{key}. {value['title']}")
    print("0. Exit")

def main():
    menu = {
        "1": {"title": "Send Money", "submenu": {
            "1": {"title": "To MTN Mobile Money"},
            "2": {"title": "To Other Networks"},
            "3": {"title": "To Bank Account"}
        }},
        "2": {"title": "Withdraw Money", "submenu": {
            "1": {"title": "From Agent"},
            "2": {"title": "From ATM"}
        }},
        "3": {"title": "Buy Airtime", "submenu": {
            "1": {"title": "For My Number"},
            "2": {"title": "For Other Number"}
        }},
        "4": {"title": "Pay Bills", "submenu": {
            "1": {"title": "Electricity"},
            "2": {"title": "Water"},
            "3": {"title": "TV Subscription"}
        }},
        "6": {"title": "Insurance", "submenu": {
            "1": {"title": "SWISCO"},
            "2": {"title": "Jubilee"},
            "3": {"title": "Prudential"},
        }},
        "7": {"title": "Check Account", "submenu": {
            "1": {"title": "Check balance"},
            "2": {"title": "Fees calculator"},
            "3": {"title": "Change Pin"},
            "4": {"title": "Pin reset"},
        }},
    }

    current_menu = menu
    while True:
        display_menu(current_menu)
        choice = input("Select an option: ")
        if choice == "0":
            print("Exiting...")
            break
        elif choice in current_menu:
            if 'submenu' in current_menu[choice]:
                current_menu = current_menu[choice]['submenu']
            else:
                print(f"Selected: {current_menu[choice]['title']}")
                current_menu = menu
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
