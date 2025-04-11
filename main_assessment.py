# We will use the re library to create more complex and strict rules
# to the users inputs.
import re
# We will use datetime to set real date and times in the program, as is required.
import datetime

# Define menu options as tuples because data is immutable
main_menu = ("fleet management", "shipment management", "delivery management", "quit application")
fleet_menu = ("add vehicle", "update vehicle information", "remove a vehicle", "view fleet", "quit fleet management")
shipment_menu = ("create a new shipment", "track a shipment", "view all shipments", "quit shipment management")
delivery_menu = ("record delivery for a shipment", "view delivery status for a shipment", "quit delivery management")

# Global lists to store data (in a real application, these would be in a database).
# Critical for each app section.
origins_list = [
    "123 Main St, Seattle, Wa",
    "456 Oak Ave, Portland, Or",
    "789 Pine Blvd, San Francisco, Ca"
]

destinations_list = [
    "321 Elm St, Miami, Fl",
    "654 Maple Rd, Austin, Tx",
    "987 Cedar Ln, Denver, Co"
]

weights_list = [
    "25.5",
    "12",
    "67.8"
]

# Main vehicle ID list (this is the one you already have)
vehicles_list = ["VTRUCK1", "VCAR123", "V2TRUCK"]

# Additional lists to store vehicle details
vehicle_types = ["Truck", "Car", "Truck"]
vehicle_capacities = ["5000", "500", "3500"]
vehicle_availability = [True, False, True]

shipment_ids_list = [
    "A00000123456789",
    "A00000987654321",
    "A00000555666777"
]

vehicles_selected = [
    "VTRUCK1",
    "VCAR123",
    "V2TRUCK"
]

# New lists for delivery management
delivery_status = [
    "pending",
    "pending",
    "pending"
]

# Initialize existing example delivery datetimes with fixed dates
delivery_datetime = [
    "2025-01-15 10:30:45",
    "2025-01-16 14:22:10",
    "2025-01-18 09:15:30"
]


# General structure of the program that defines how the menus are displayed and executed.

def main():
    """
    Main function that runs the program and displays the main menu.
    """
    while True:
        # Display main menu
        print("Welcome!!!\n"
              "FMS is a software that helps you to manage "
              "your shipments and deliveries.\n")
        print(" FMS ".center(70, "="))
        print("")
        # The first variable stores the index and add 1 to create a list feeling
        # The second variable iterates the tuple
        for i, m in enumerate(main_menu):
            print(f"{i + 1}.- {m.title()}")

        # Get user input
        choice = input("\nPlease select an option (1-4 or type the menu name): ").strip()

        # Validate and process user input
        if choice == "1" or choice.lower() == "fleet management":
            fleet_management_menu()
        elif choice == "2" or choice.lower() == "shipment management":
            shipment_management_menu()
        elif choice == "3" or choice.lower() == "delivery management":
            delivery_management_menu()
        elif choice == "4" or choice.lower() == "quit application" or choice.lower() == "q" \
                or choice.lower() == "Q":
            print("Thank you for using the Fleet Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


# First section of the program
  # Fleet Management System
# Global list to store fleet vehicle records
fleet_records = []
def manage_fleet():
    """Fleet management menu to handle different vehicle-related tasks."""
    while True:
        print("\n--- Fleet Management Menu ---")
        print("1. Add a Vehicle")
        print("2. Update Vehicle Information")
        print("3. Remove a Vehicle")
        print("4. View All Vehicles")
        print("5. Quit Fleet Management")
         selection = input("Select an operation (1-5): ").strip()
        if selection == "1":
            add_vehicle()
        elif selection == "2":
            update_vehicle()
        elif selection == "3":
            remove_vehicle()
        elif selection == "4":
            view_fleet()
        elif selection == "5":
            print("Exiting Fleet Management...")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")
# === Fleet Management Functions ===
def add_vehicle():
    """Add a new vehicle ensuring it has a unique identifier with more than 10,000 digits after 'V'."""
    veh_code = input("Enter Vehicle ID (must start with 'V' and have more than 10,000 digits): ").strip()
if not (veh_code.startswith("V") and veh_code[1:].isdigit() and len(veh_code[1:]) > 10000):
        print("Error: Vehicle ID must start with 'V' followed by more than 10,000 digits.")
        return
if any(veh["code"] == veh_code for veh in fleet_records):
        print("Error: Vehicle ID already exists.")
        return
     veh_type = input("Enter Vehicle Type: ").strip()
    veh_model = input("Enter Vehicle Model: ").strip()
    cap_veh = input("Enter Load Capacity (kg): ").strip()
    if not cap_veh.isdigit() or int(cap_veh) <= 0:
        print("Error: Load Capacity must be a positive number.")
        return
    fleet_records.append({
        "code": veh_code,
        "type": veh_type,
        "model": veh_model,
        "cap": int(cap_veh)
    })
   print("Vehicle successfully added.")
def update_vehicle():
    """Update an existing vehicle's information."""
    veh_code = input("Enter Vehicle ID to update: ").strip()
   for veh in fleet_records:
        if veh["code"] == veh_code:
            new_type = input("Enter new Vehicle Type: ").strip()
            new_model = input("Enter new Vehicle Model: ").strip()
            new_cap = input("Enter new Load Capacity (kg): ").strip()
     if not new_cap.isdigit() or int(new_cap) <= 0:
                print("Error: Load Capacity must be a valid positive number.")
                return
         veh["type"] = new_type
            veh["model"] = new_model
            veh["cap"] = int(new_cap)
    print("Vehicle details updated successfully.")
            return
     print("Error: No matching vehicle found.")
def remove_vehicle():
    """Remove a vehicle from the fleet."""
    veh_code = input("Enter Vehicle ID to remove: ").strip()
  for i, veh in enumerate(fleet_records):
        if veh["code"] == veh_code:
            confirm = input("Are you sure you want to delete this vehicle? (yes/no): ").strip().lower()
            if confirm == "yes":
                del fleet_records[i]
                print("Vehicle removed successfully.")
            else:
                print("Vehicle removal canceled.")
            return
print("Error: No matching vehicle found.")
def view_fleet():
    """Display a list of all vehicles in the fleet."""
    if not fleet_records:
        print("No vehicles in the fleet.")
        return
  print("\n--- Fleet Inventory ---")
    print(f"{'ID':<25} {'Type':<15} {'Model':<15} {'Capacity (kg)':<15}")
    print("-" * 75)
    for veh in fleet_records:
        print(f"{veh['code'][:22] + '...':<25} {veh['type']:<15} {veh['model']:<15} {veh['cap']:<15}")
# Second section of the program

def shipment_management_menu():
    """
    Display and handle the Shipment Management submenu.
    """
    while True:
        # Display Shipment Management submenu
        print("")
        print(" Shipment Management ".center(40, "="))
        print("")
        # The first variable stores the index and add 1 to create a list feeling
        # The second variable iterates the tuple
        for i, m in enumerate(shipment_menu):
            print(f"{i + 1}.- {m.title()}")

        # Get user input
        choice = input("\nPlease select an option (1-4 or type the submenu name): ").strip()

        # Validate and process user input
        if choice == "1" or choice.lower() == "create a new shipment":
            # If create_shipment returns True, it means we should return to main menu
            if create_shipment():
                return
        elif choice == "2" or choice.lower() == "track a shipment":
            track_shipment()
        elif choice == "3" or choice.lower() == "view all shipments":
            view_shipments()
        elif choice == "4" or choice.lower() == "quit shipment management" or choice.lower() == "q" \
                or choice.lower() == "Q":
            print("Returning to main menu...")
            return
        else:
            print("Invalid option. Please try again.")


# Third section of the program

def delivery_management_menu():
    """
    Display and handle the Delivery Management submenu.
    """
    while True:
        # Display Delivery Management submenu
        print("")
        print(" Delivery Management ".center(40, "="))
        print("")
        for i, m in enumerate(delivery_menu):
            print(f"{i + 1}.- {m.title()}")

        # Get user input
        choice = input("\nPlease select an option (1-3 or type the submenu name): ").strip()

        # Validate and process user input
        if choice == "1" or choice.lower() == "record delivery for a shipment":
            record_delivery()
        elif choice == "2" or choice.lower() == "view delivery status for a shipment":
            view_delivery_status()
        elif choice == "3" or choice.lower() == "quit delivery management" or choice.lower() == "q" \
                or choice.lower() == "Q":
            print("Returning to main menu...")
            return
        else:
            print("Invalid option. Please try again.")

# Functions nested and used in the create_shipment() function
# Function that returns and validates the origin address
def addressOriginValidation():
    while True:
        locationOrigin = input("Please enter the origin address.\n"
                               "Please use: street and number, suburb, zipcode: ").lower()

        # The pattern restrict the input of the street and number and the suburb at least should
        # be 3 characters long and the zipcode is limited to 4 to 10 characters
        # as is a conventional standard worldwide. Also validates spaces characters in the input.

        pattern = (r'^([a-zA-Z0-9][a-zA-Z0-9\s\-]{2,}),'
                   r'\s*([a-zA-Z][a-zA-Z\s-]{2,}),\s*([a-zA-Z0-9]{4,10})$')

        match = re.match(pattern, locationOrigin)
        if match:
            street, suburb, zipcode = match.groups()
            print("Thank you for providing a valid format address!")
            print(f"Street and number: {street}")
            print(f"Suburb: {suburb}")
            print(f"Zipcode: {zipcode}")
            return locationOrigin.title()
        else:
            print("Invalid address format. Please use: street and number, suburb, zipcode")
            # If an invalid address is typed will return to the Shipment Management menu
            return

# Function that returns and validate the destination address
def addressDestinationValidation():
    while True:
        locationDestination = input("Please enter the destination address: ").lower()

        # The pattern restrict the input of the street and number and the suburb at least should
        # be 3 characters long and the zipcode is limited to 4 to 10 characters
        # as is a conventional standard worldwide. Also validates spaces characters in the input.

        pattern = (r'^([a-zA-Z0-9][a-zA-Z0-9\s\-]{2,}),'
                   r'\s*([a-zA-Z][a-zA-Z\s-]{2,}),\s*([a-zA-Z0-9]{4,10})$')

        match = re.match(pattern, locationDestination)
        if match:
            street, suburb, zipcode = match.groups()
            print("Thank you for providing a valid format address!")
            print(f"Street and number: {street}")
            print(f"Suburb: {suburb}")
            print(f"Zipcode: {zipcode}")
            return locationDestination.title()
        else:
            print("Invalid address format. Please use: street and number, suburb, zipcode")
            # If an invalid address is typed will return to the Shipment Management menu
            return


# Function that returns and validates the weight of the package
def weightValidation():
    while True:
        # Removes all the spaces at the beginning and at the end of the input
        weight = input("Please enter the weight of the package in kg: ").strip()

        # This pattern validates that at least one character is typed
        # and that there are digits inputs and . if it's a float.
        pattern = r'^\S*\d+(\.\d+)?$'

        match = re.match(pattern, weight)

        # Check if it's a valid number in case of weights with decimals
        if "." in weight and match:
            print("Thank you for typing a valid number.\n"
                 f"The weight typed is: {weight} kg.")
            return str(float(weight))
        elif match:
            # It's an integer
            print("Thank you for typing a valid number.\n"
                  f"The weight typed is: {weight} kg.")
            return str(int(weight))

        # If we get here, the input was invalid
        print("This is not a valid input. Try again.\n"
              "Remember that only numbers are allowed")

        # This section with the return method without argument
        # gives control to the main function controlling this function
        # in this case the Shipment Management function

        return


# Function that returns and validates the vehicle ID
def vehicleIDValidation(vehiclesList):
    while True:
        # Display the list of vehicles, in the variable vehicles_list, with numbering
        for i, v in enumerate(vehiclesList):
            print(f"{i + 1}.- {v}")

        # Get user input
        choice = input("\nPlease select an option (enter number or vehicle ID): ").strip()

        # Try to handle numeric input
        if choice.isdigit():
            choice_num = int(choice)
            # Validates that the number entered is not bigger than the length of the list.
            if 1 <= choice_num <= len(vehiclesList):
                # Select the vehicle by index
                selected_vehicle = vehiclesList[choice_num - 1]
                print("Thank you for your selection.\n"
                      f"You chose the vehicle ID: {selected_vehicle}")
                return selected_vehicle
        # Handle text input - check if the input matches any vehicle ID
        else:
            for vehicle in vehiclesList:
                if choice.lower() == vehicle.lower():
                    print("Thank you for your selection.\n"
                          f"You chose the vehicle ID: {vehicle}")
                    return vehicle

        # If we get here, the input was invalid
        print("Invalid selection. Please try again.")

        # This section with the return method without argument
        # gives control to the main function controlling this function
        # in this case the Shipment Management function

        return


# === Shipment Management Functions ===
# Function to create a new shipment order

def create_shipment():
    """
    Create a new shipment by collecting and validating all required information.
    If any validation fails, return to this function without creating a shipment.
    If all validations pass, create a shipment ID and store all information.
    Returns True if shipment was created successfully to signal return to main menu.
    """

    # Start the shipment creation process
    print("\n===== Create New Shipment =====")

    # Get and validate origin address
    locationOrigin = addressOriginValidation()
    if not locationOrigin:
        print("Invalid origin address. Returning to shipment menu.")
        input("Press Enter to continue...")
        return False  # Return to shipment menu if validation fails

    # Get and validate destination address
    locationDestination = addressDestinationValidation()
    if not locationDestination:
        print("Invalid destination address. Returning to shipment menu.")
        input("Press Enter to continue...")
        return False  # Return to shipment menu if validation fails

    # Get and validate package weight
    weight = weightValidation()
    if not weight:
        print("Invalid weight. Returning to shipment menu.")
        input("Press Enter to continue...")
        return False  # Return to shipment menu if validation fails

    # Get and validate vehicle selection
    selected_vehicle = vehicleIDValidation(vehicles_list)
    if not selected_vehicle:
        print("Invalid vehicle selection. Returning to shipment menu.")
        input("Press Enter to continue...")
        return False  # Return to shipment menu if validation fails

    # Create a unique string by concatenating the inputs
    unique_string = f"{locationOrigin}+{locationDestination}+{weight}%23"

    # Get a simple unique number (Python's built-in hash function)
    id_number = abs(hash(unique_string))

    # Format the shipment ID to always be 15 characters long
    id_number_str = str(id_number)

    # Calculate how many zeros to add (we need 14 chars after 'A')
    zeros_needed = 14 - len(id_number_str)

    # Create the standardized shipment ID (A + zeros + number)
    shipmentID = f"A{'0' * zeros_needed}{id_number_str}"

    # If somehow the number is too long, truncate it to keep total length at 15
    if len(shipmentID) > 15:
        shipmentID = shipmentID[:15]

    # Add all information to the lists of the shipment order
    origins_list.append(locationOrigin)
    destinations_list.append(locationDestination)
    weights_list.append(weight)
    vehicles_selected.append(selected_vehicle)
    shipment_ids_list.append(shipmentID)

    # Initialize the delivery status as pending for new shipments
    delivery_status.append("pending")

    # Get the current date and time using the datetime library
    current_datetime = datetime.datetime.now()

    # Format the datetime string in YYYY-MM-DD HH:MM:SS format
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    delivery_datetime.append(formatted_datetime)

    # Display confirmation to the user before returning to the main menu
    print("\n===== Shipment Created Successfully =====")
    print(f"Shipment ID: {shipmentID}")
    print(f"Origin: {locationOrigin}")
    print(f"Destination: {locationDestination}")
    print(f"Weight: {weight} kg")
    print(f"Assigned Vehicle: {selected_vehicle}")

    # Generate initial status based on shipment ID
    status_code = sum(ord(char) for char in shipmentID) % 3
    if status_code == 0:
        status = "Processing"
    elif status_code == 1:
        status = "In Transit"
    else:  # status_code == 2
        status = "Out for Delivery"

    print(f"Status: {status}")
    print(f"Creation Date/Time: {formatted_datetime}")

    input("\nPress Enter to return to the main menu...")

    # After a successful shipment creation, return True to signal return to main menu
    return True

# Function that allows the user to verify a shipment information if shipment exists
# in shipment_list.

def track_shipment():
    while True:
        shipmentTracking = input("Please enter your Shipment ID.\n"
                                 "Remember the format: Axxxxxxxxxxxxxx: ").title()

        # Condition used to validate empty inputs and keeping the loop running if is the case.

        if not shipmentTracking:
            print("Something went wrong. Not empty inputs are allowed.")
            continue

        # Condition that generates a status for each order.

        elif shipmentTracking in shipment_ids_list and len(shipmentTracking) == 15 \
                and shipmentTracking.startswith("A"):
            # Get the index of the shipment in the list
            index = shipment_ids_list.index(shipmentTracking)

            # Check if the shipment has been marked as delivered
            if delivery_status[index] == "delivered":
                status = "Your shipment has been delivered"
                delivery_date = delivery_datetime[index]
                print(f"\nShipment Status: {status}")
                print(f"Delivery Date/Time: {delivery_date}")
            else:
                # Generate a tracking status based on the shipment ID
                # A variable string is created "randomly" by using ord() function.
                # The ord() function returns an integer representation for any character.
                # The sum() function is like creating an incrementing variable.
                # The iteration applies the ord() function to each character
                # in the shipment ID.
                # The modulus is used to return values between 0-3

                status_code = sum(ord(char) for char in shipmentTracking) % 3

                # Map the status code to a meaningful status message
                if status_code == 0:
                    status = "Your shipment is being processed"
                elif status_code == 1:
                    status = "Your shipment is in transit"
                else:  # status_code == 2
                    status = "Your shipment is out for delivery"

                print(f"\nShipment Status: {status}")
                print(f"Date/Time: {delivery_datetime[index]}")

            print(f"Tracking ID: {shipmentTracking}")
            input("\nPress Enter to return to the shipment menu...")
            return
        elif shipmentTracking not in shipment_ids_list and len(shipmentTracking) == 15 \
                and shipmentTracking.startswith("A"):
            print("The shipment ID is not in our records.")
            # If shipment is not listed will return you to the shipment management menu
            return
        print("Something went wrong. The shipment format is incorrect. Please try again.")


def view_shipments():
    print("\n===== All Shipment Details =====")

    if not shipment_ids_list:
        print("No shipments found in the system.")
        return

    for i in range(len(shipment_ids_list)):
        print(f"Shipment ID: {shipment_ids_list[i]}")
        print(f"Origin: {origins_list[i]}")
        print(f"Destination: {destinations_list[i]}")
        print(f"Weight: {weights_list[i]} kg")
        print(f"Vehicle: {vehicles_selected[i]}")

        # Check if the shipment has been marked as delivered
        if delivery_status[i] == "delivered":
            status = "Delivered"
            print(f"Status: {status}")
            print(f"Delivery Date/Time: {delivery_datetime[i]}")
        else:
            # Generate a tracking status based on the shipment ID
            status_code = sum(ord(char) for char in shipment_ids_list[i]) % 3

            if status_code == 0:
                status = "Processing"
            elif status_code == 1:
                status = "In Transit"
            else:  # status_code == 2
                status = "Out for Delivery"

            print(f"Status: {status}")
            print(f"Creation Date/Time: {delivery_datetime[i]}")

        print("-" * 40)

    input("\nPress Enter to continue...")
    return

# === Delivery Management Functions ===

def record_delivery():
    """
    Record a delivery for an existing shipment.
    Changes the status from pending to delivered and records the delivery datetime.
    """
    print("\n===== Record Shipment Delivery =====")

    # Get shipment ID from user
    shipment_id = input("Enter Shipment ID to mark as delivered: ").strip().upper()

    # Check if shipment ID exists
    if shipment_id not in shipment_ids_list:
        print("Error: Shipment ID not found. Please try again!")
        input("Press Enter to continue...")
        return False

    # Get index of the shipment
    shipment_index = shipment_ids_list.index(shipment_id)

    # Check if the shipment is already delivered
    if delivery_status[shipment_index] == "delivered":
        print(f"Shipment {shipment_id} has already been marked as delivered.")
        input("Press Enter to continue...")
        return False

    # Update the delivery status
    delivery_status[shipment_index] = "delivered"

    # Record the current datetime for the delivery
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    delivery_datetime[shipment_index] = formatted_datetime

    print(f"\nShipment {shipment_id} has been marked as delivered at {formatted_datetime}.")
    input("Press Enter to continue...")
    return True


def view_delivery_status():
    """
    View the delivery status for a specific shipment.
    """
    print("\n===== View Shipment Delivery Status =====")

    # Get shipment ID from user
    shipment_id = input("Enter Shipment ID to check delivery status: ").strip().upper()

    # Check if shipment ID exists
    if shipment_id not in shipment_ids_list:
        print("Error: Shipment ID not found. Please try again!")
        input("Press Enter to continue...")
        return False

    # Get index of the shipment
    shipment_index = shipment_ids_list.index(shipment_id)

    # Display delivery status
    status = delivery_status[shipment_index]
    datetime_str = delivery_datetime[shipment_index]

    print(f"\nShipment ID: {shipment_id}")
    print(f"Delivery Status: {status.title()}")

    if status == "delivered":
        print(f"Delivery Time: {datetime_str}")
    elif status == "pending":
        print("This shipment has not been delivered yet.")
        print("Select 'Record Delivery for a Shipment' from the menu to mark it as delivered.")

    input("Press Enter to continue...")
    return True

# Start the program by directly calling the main function
main()
