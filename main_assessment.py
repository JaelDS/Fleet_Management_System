'''
# Function for validating input
def validate_choice(user_input, items):
    if user_input.isdigit():
        idx = int(user_input)
        if 1 <= idx <= len(items):
            return idx - 1
    elif user_input.capitalize() in items:
        return items.index(user_input.capitalize())
    return None
'''


# Fleet Management System
# This program provides a menu-driven interface for managing a fleet,
# shipments, and deliveries.

def main():
    """
    Main function that runs the program and displays the main menu.
    """
    while True:
        # Display main menu
        print("\n===== Fleet Management System =====")
        print("1. Fleet Management")
        print("2. Shipment Management")
        print("3. Delivery Management")
        print("4. Quit Application")

        # Get user input
        choice = input("\nPlease select an option (1-4 or type the menu name): ").strip()

        # Validate and process user input
        if choice == "1" or choice.lower() == "fleet management":
            fleet_management_menu()
        elif choice == "2" or choice.lower() == "shipment management":
            shipment_management_menu()
        elif choice == "3" or choice.lower() == "delivery management":
            delivery_management_menu()
        elif choice == "4" or choice.lower() == "quit application":
            print("Thank you for using the Fleet Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def fleet_management_menu():
    """
    Display and handle the Fleet Management submenu.
    """
    while True:
        # Display Fleet Management submenu
        print("\n----- Fleet Management -----")
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. View Fleet")
        print("4. Return to Main Menu")

        # Get user input
        choice = input("\nPlease select an option (1-4 or type the submenu name): ").strip()

        # Validate and process user input
        if choice == "1" or choice.lower() == "add vehicle":
            add_vehicle()
        elif choice == "2" or choice.lower() == "remove vehicle":
            remove_vehicle()
        elif choice == "3" or choice.lower() == "view fleet":
            view_fleet()
        elif choice == "4" or choice.lower() == "return to main menu":
            return
        else:
            print("Invalid option. Please try again.")


def shipment_management_menu():
    """
    Display and handle the Shipment Management submenu.
    """
    while True:
        # Display Shipment Management submenu
        print("\n----- Shipment Management -----")
        print("1. Create Shipment")
        print("2. Update Shipment")
        print("3. Track Shipment")
        print("4. Return to Main Menu")

        # Get user input
        choice = input("\nPlease select an option (1-4 or type the submenu name): ").strip()

        # Validate and process user input
        if choice == "1" or choice.lower() == "create shipment":
            create_shipment()
        elif choice == "2" or choice.lower() == "update shipment":
            update_shipment()
        elif choice == "3" or choice.lower() == "track shipment":
            track_shipment()
        elif choice == "4" or choice.lower() == "return to main menu":
            return
        else:
            print("Invalid option. Please try again.")


def delivery_management_menu():
    """
    Display and handle the Delivery Management submenu.
    """
    while True:
        # Display Delivery Management submenu
        print("\n----- Delivery Management -----")
        print("1. Schedule Delivery")
        print("2. Update Delivery Status")
        print("3. View Deliveries")
        print("4. Return to Main Menu")

        # Get user input
        choice = input("\nPlease select an option (1-4 or type the submenu name): ").strip()

        # Validate and process user input
        if choice == "1" or choice.lower() == "schedule delivery":
            schedule_delivery()
        elif choice == "2" or choice.lower() == "update delivery status":
            update_delivery_status()
        elif choice == "3" or choice.lower() == "view deliveries":
            view_deliveries()
        elif choice == "4" or choice.lower() == "return to main menu":
            return
        else:
            print("Invalid option. Please try again.")


# === Fleet Management Functions ===

def add_vehicle():
    """
    Add a new vehicle to the fleet.

    YOUR CODE GOES HERE:
    - Get vehicle details from user
    - Validate input
    - Add vehicle to database/list
    - Confirm addition to user
    """
    print("\nAdding a vehicle to the fleet...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


def remove_vehicle():
    """
    Remove a vehicle from the fleet.

    YOUR CODE GOES HERE:
    - Get vehicle ID or details from user
    - Validate input
    - Remove vehicle from database/list
    - Confirm removal to user
    """
    print("\nRemoving a vehicle from the fleet...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


def view_fleet():
    """
    Display all vehicles in the fleet.

    YOUR CODE GOES HERE:
    - Retrieve all vehicles from database/list
    - Format and display vehicle information
    - Provide filtering or sorting options if needed
    """
    print("\nViewing all vehicles in the fleet...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


# === Shipment Management Functions ===

def create_shipment():
    """
    Create a new shipment.

    YOUR CODE GOES HERE:
    - Get shipment details from user
    - Validate input
    - Create new shipment in database/list
    - Confirm creation to user
    """
    print("\nCreating a new shipment...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


def update_shipment():
    """
    Update an existing shipment.

    YOUR CODE GOES HERE:
    - Get shipment ID from user
    - Validate input
    - Get updated information
    - Update shipment in database/list
    - Confirm update to user
    """
    print("\nUpdating an existing shipment...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


def track_shipment():
    """
    Track the status of a shipment.

    YOUR CODE GOES HERE:
    - Get shipment ID from user
    - Validate input
    - Retrieve shipment status
    - Display status information to user
    """
    print("\nTracking a shipment...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


# === Delivery Management Functions ===

def schedule_delivery():
    """
    Schedule a new delivery.

    YOUR CODE GOES HERE:
    - Get delivery details from user
    - Validate input
    - Schedule delivery in database/list
    - Confirm scheduling to user
    """
    print("\nScheduling a new delivery...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


def update_delivery_status():
    """
    Update the status of a delivery.

    YOUR CODE GOES HERE:
    - Get delivery ID from user
    - Validate input
    - Get updated status
    - Update delivery in database/list
    - Confirm update to user
    """
    print("\nUpdating delivery status...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


def view_deliveries():
    """
    View all scheduled deliveries.

    YOUR CODE GOES HERE:
    - Retrieve all deliveries from database/list
    - Format and display delivery information
    - Provide filtering or sorting options if needed
    """
    print("\nViewing all deliveries...")
    # YOUR CODE IMPLEMENTATION HERE
    input("Press Enter to continue...")


# Start the program by directly calling the main function
main()