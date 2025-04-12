# We will use the re library to create more complex and strict rules
# to the users inputs.
import re
# We will use datetime to set real date and times in the program, as is required.
import datetime

import random

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

def fleet_management_menu():
    """
    Display and handle the Fleet Management submenu.
    """
    while True:
        # Display Fleet Management submenu
        print("")
        print(" Fleet Management ".center(40, "="))
        print("")
        # The first variable stores the index and add 1 to create a list feeling
        # The second variable iterates the tuple
        for i, m in enumerate(fleet_menu):
            print(f"{i + 1}.- {m.title()}")

        # Get user input
        choice = input("\nPlease select an option (1-5 or type the submenu name): ").strip()

        # Validate and process user input
        if choice == "1" or choice.lower() == "add vehicle":
            add_vehicle()
        elif choice == "2" or choice.lower() == "update vehicle information":
            update_vehicle()
        elif choice == "3" or choice.lower() == "remove a vehicle":
            remove_vehicle()
        elif choice == "4" or choice.lower() == "view fleet":
            view_fleet()
        elif choice == "5" or choice.lower() == "quit fleet management" or choice.lower() == "q" \
                or choice.lower() == "Q":
            print("Returning to main menu...")
            return
        else:
            print("Invalid option. Please try again.")


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

def add_vehicle():
    """
    Adds a new vehicle by prompting for user input and generating a unique vehicle ID.
    The function validates inputs, checks against existing vehicles, and updates global vehicle lists.

    Returns:
        dict or None: A dictionary containing the new vehicle information if successful, None otherwise
    """
    global vehicles_list, vehicle_types, vehicle_capacities, vehicle_availability

    # Valid vehicle types - match your existing data types
    VALID_VEHICLE_TYPES = ['truck', 'car', 'van', 'bus', 'motorcycle']

    # Type codes for different vehicle types
    TYPE_CODES = {
        'car': 'C',
        'truck': 'T',
        'bus': 'B',
        'van': 'V',
        'motorcycle': 'M'
    }

    # Maximum attempts for generating a unique ID
    MAX_GENERATION_ATTEMPTS = 100

    def generate_random_string(length):
        """Generate a random alphanumeric string of specified length"""
        # Omitting potentially confusing characters like I, O, 0, 1
        chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        return ''.join(random.choice(chars) for _ in range(length))

    # Prompt for vehicle information
    print("\n===== Add New Vehicle =====")

    # Get vehicle type from user
    while True:
        vehicle_type = input(f"Enter vehicle type ({', '.join(VALID_VEHICLE_TYPES)}): ").strip().lower()

        if not vehicle_type:
            print("Vehicle type cannot be empty. Please try again.")
            continue

        if vehicle_type in VALID_VEHICLE_TYPES:
            break
        else:
            print(f"Invalid vehicle type. Please use one of: {', '.join(VALID_VEHICLE_TYPES)}")

    # Get capacity from user
    while True:
        capacity_input = input("Enter vehicle capacity (weight in kg or number of passengers): ").strip()

        try:
            capacity = int(capacity_input)
            if capacity > 0 and capacity < 10000:  # Assuming max capacity is 10000 (for trucks)
                break
            else:
                print("Capacity must be a positive number less than 10000.")
        except ValueError:
            print("Invalid capacity. Please enter a numeric value.")

    # Determine capacity code based on capacity and vehicle type
    if vehicle_type == 'truck':
        if capacity <= 1000:
            capacity_code = 'S'  # Small truck
        elif capacity <= 5000:
            capacity_code = 'M'  # Medium truck
        else:
            capacity_code = 'L'  # Large truck
    else:  # For passenger vehicles
        if capacity <= 2:
            capacity_code = 'S'  # Small capacity
        elif capacity <= 5:
            capacity_code = 'M'  # Medium capacity
        elif capacity <= 15:
            capacity_code = 'L'  # Large capacity
        else:
            capacity_code = 'X'  # Extra large capacity

    # Get the type code
    type_code = TYPE_CODES.get(vehicle_type, 'X')

    # Get current year's last two digits
    year_code = str(datetime.datetime.now().year)[-2:]

    # Generate a unique ID with multiple attempts
    attempts = 0
    vehicle_id = None

    while True:
        # Create the ID format: V[TypeCode][CapacityCode][YearCode][RandomPart]
        random_part = generate_random_string(4)
        vehicle_id = f"V{type_code}{capacity_code}{year_code}{random_part}"

        attempts += 1
        # Check if the ID already exists in the vehicles_list
        if vehicle_id not in vehicles_list:
            break

        # Break the loop if we've reached maximum attempts to prevent infinite loops
        if attempts >= MAX_GENERATION_ATTEMPTS:
            print(f"Warning: Maximum attempts ({MAX_GENERATION_ATTEMPTS}) reached while generating unique vehicle ID")
            print("Returning to fleet menu...")
            input("Press Enter to continue...")
            return None

    # Set availability to True by default for new vehicles
    # It will be automatically managed when vehicles are assigned to shipments
    availability = True

    # Create vehicle object with all information
    new_vehicle = {
        'id': vehicle_id,
        'type': vehicle_type.capitalize(),  # Store with first letter capitalized to match existing data
        'capacity': str(capacity),  # Convert to string to match existing data format
        'available': availability
    }

    # Add the new vehicle to the global lists
    vehicles_list.append(vehicle_id)
    vehicle_types.append(new_vehicle['type'])
    vehicle_capacities.append(new_vehicle['capacity'])
    vehicle_availability.append(availability)

    print(f"\nVehicle added successfully with ID: {vehicle_id}")
    print(f"Type: {new_vehicle['type']}")
    print(f"Capacity: {new_vehicle['capacity']}")
    print(f"Status: Available")

    input("\nPress Enter to return to the main menu...")

    # Return to main menu
    return True  # Return True to signal returning to main menu


def update_vehicle():
    """
    Update vehicle specifications.
    Displays vehicle list for selection and allows updating type and capacity.
    """
    global vehicles_list, vehicle_types, vehicle_capacities

    # Display all vehicles with their details first
    print("\n===== Update Vehicle Information =====")

    if not vehicles_list:
        print("No vehicles have been added yet.")
        input("\nPress Enter to return to the fleet menu...")
        return

    print("\nAvailable Vehicles:")
    print(f"{'#':<3} {'Code':<15} {'Type':<15} {'Capacity (kg)':<15}")
    print("=" * 50)

    for i, v_id in enumerate(vehicles_list):
        print(f"{i + 1:<3} {v_id:<15} {vehicle_types[i]:<15} {vehicle_capacities[i]:<15}")

    # Get user selection - either by number or vehicle ID
    while True:
        selection = input("\nEnter the number or vehicle ID to update (or 'q' to return): ").strip().lower()

        if selection in ['q', 'quit', 'Q']:
            print("Update canceled. Returning to main menu...")
            return True  # Return True to signal returning to main menu

        # Handle selection by number
        if selection.isdigit():
            selection_num = int(selection)
            if 1 <= selection_num <= len(vehicles_list):
                veh_code = vehicles_list[selection_num - 1]
                index = selection_num - 1
                break
            else:
                print(f"Invalid selection. Please enter a number between 1 and {len(vehicles_list)}.")

        # Handle selection by vehicle ID
        elif selection.upper() in [v.upper() for v in vehicles_list]:
            # Find the actual vehicle ID with matching case
            for vehicle in vehicles_list:
                if vehicle.upper() == selection.upper():
                    veh_code = vehicle
                    index = vehicles_list.index(veh_code)
                    break
            break

        else:
            print("Invalid selection. Vehicle not found.")

    # Display current details of selected vehicle
    print(f"\nUpdating Vehicle: {veh_code}")
    print(f"Current Type: {vehicle_types[index]}")
    print(f"Current Capacity: {vehicle_capacities[index]} kg")

    # Valid vehicle types
    VALID_VEHICLE_TYPES = ['truck', 'car', 'van', 'bus', 'motorcycle']

    # Get updated vehicle type
    while True:
        new_type = input(
            f"\nEnter new vehicle type ({', '.join(VALID_VEHICLE_TYPES)}) or press Enter to keep current (q to quit): ").strip()

        # Check for quit command
        if new_type.lower() in ['q', 'quit']:
            print("Update canceled. Returning to main menu...")
            return True  # Return True to signal returning to main menu

        # Keep current if empty
        if not new_type:
            new_type = vehicle_types[index]
            break

        if new_type.lower() in VALID_VEHICLE_TYPES:
            new_type = new_type.capitalize()  # Capitalize to match convention
            break
        else:
            print(f"Invalid vehicle type. Please use one of: {', '.join(VALID_VEHICLE_TYPES)}")

    # Get updated capacity
    while True:
        new_cap = input(
            "Enter new capacity (kg or number of passengers) or press Enter to keep current (q to quit): ").strip()

        # Check for quit command
        if new_cap.lower() in ['q', 'quit']:
            print("Update canceled. Returning to main menu...")
            return True  # Return True to signal returning to main menu

        # Keep current if empty
        if not new_cap:
            new_cap = vehicle_capacities[index]
            break

        try:
            capacity = int(new_cap)
            if capacity > 0 and capacity < 10000:  # Assuming max capacity is 10000
                break
            else:
                print("Capacity must be a positive number less than 10000.")
        except ValueError:
            print("Invalid capacity. Please enter a numeric value.")

    # Apply modifications to the vehicle data
    vehicle_types[index] = new_type
    vehicle_capacities[index] = str(new_cap)  # Convert to string to match existing format

    # Confirmation message
    print("\n===== Vehicle Updated Successfully =====")
    print(f"Vehicle ID: {veh_code}")
    print(f"Updated Type: {new_type}")
    print(f"Updated Capacity: {new_cap}")

    input("\nPress Enter to return to the main menu...")
    return True  # Return True to signal returning to main menu

def remove_vehicle():
    """Remove a vehicle record."""
    veh_code = input("Enter Vehicle Code to delete: ")  # Identify vehicle to delete
    if veh_code in vehicles_list:
        index = vehicles_list.index(veh_code)
        confirmation = input("Confirm deletion? (yes/no): ").strip().lower()
        if confirmation == "yes":
            # Check if vehicle is assigned to any shipments
            if veh_code in vehicles_selected:
                print("Error: Cannot remove vehicle as it is assigned to shipments.")
                return

            # Remove from all vehicle lists
            vehicles_list.pop(index)
            vehicle_types.pop(index)
            vehicle_capacities.pop(index)
            vehicle_availability.pop(index)
            print("Vehicle record successfully removed.")
        else:
            print("Deletion canceled.")
        return
    print("Error: No such vehicle found.")


def view_fleet():
    """Display all registered vehicles."""
    if not vehicles_list:
        print("No vehicles have been added yet.")
    else:
        print("\nFleet Inventory:")
        print(f"{'Code':<10} {'Type':<15} {'Capacity (kg)':<15}")
        print("=" * 50)
        for i in range(len(vehicles_list)):
            print(f"{vehicles_list[i]:<10} {vehicle_types[i]:<15} {vehicle_capacities[i]:<15}")

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