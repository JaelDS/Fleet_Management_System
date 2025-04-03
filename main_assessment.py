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
              "your shipments and deliveries.\n"
              "===== FMS =====")
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
        print("\n===== Fleet Management =====")
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
        print("\n===== Shipment Management =====")
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
        print("\n===== Delivery Management =====")
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
        locationOrigin = input("Please enter the origin address: ").lower()

        if locationOrigin.count(",") == 2:
            validationStrip = locationOrigin.replace(" ", "")
            validation = validationStrip.split(",")
            alphaNum = "".join(validation)

            if len(validation) == 3 and alphaNum.isalnum():
                # Valid input, break out of the loop
                print("Thanks for entered a valid address\n"
                      f"You entered the address origin: {locationOrigin.title()}")
                return locationOrigin.title()  # Return the valid input
            else:
                return
        else:
            return


# Function that returns and validate the destination address
def addressDestinationValidation():
    while True:
        locationDestination = input("Please enter the destination address: ").lower()

        # Validate a correct format of the input

        if locationDestination.count(",") == 2:
            validationStrip = locationDestination.replace(" ", "")
            validation = validationStrip.split(",")
            alphaNum = "".join(validation)

            # If a valid input will return the value to append it to several lists that structure
            # the shipment order

            if len(validation) == 3 and alphaNum.isalnum():
                # Valid input, break out of the loop
                print("Thanks for entered a valid address\n"
                      f"You entered the address destination: {locationDestination.title()}")
                return locationDestination.title()  # Return the valid input

            # This section with the return method without argument
            # gives control to the main function controlling this function
            # in this case the Shipment Management function

            else:
                return
        else:
            return


# Function that returns and validates the weight of the package
def weightValidation():
    while True:
        weight = input("Please enter the weight of the package in kg: ").strip()

        # Check if input is empty
        if not weight:
            print("Empty input not allowed. Please enter a weight.")
            return

        # Check if it's a valid number in case of weights with decimals
        if weight.count(".") == 1:
            # It might be a float
            weightSplit = weight.split(".")
            if weightSplit[0].isdigit() and weightSplit[1].isdigit():
                print("Thank you for typing a valid number.\n"
                      f"The weight typed is: {weight} kg.")
                return weight
        elif weight.isdigit():
            # It's an integer
            print("Thank you for typing a valid number.\n"
                  f"The weight typed is: {weight} kg.")
            return weight

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

    # All validations passed, create shipment ID using the requested method
    # We'll create a unique ID similar to the suggested approach but without eval()
    # The id() function returns a unique identifier for an object
    # The hash of a string is also unique for that string

    # Create a unique string by concatenating the inputs
    # Origin and destination location and the weight of the package
    # and, we use the modulus operator to get a 14-digit number no matter the input

    unique_string = f"{locationOrigin}+{locationDestination}+{weight}%23"

    # Get a simple unique number (Python's built-in hash function)
    # Once we got a unique concatenation we use the hash built-in function
    # to get a unique integer from the unique string.
    # Finally, we use the abs built-in function to avoid using negative numbers.

    id_number = abs(hash(unique_string))

    # Format the shipment ID to always be 15 characters long
    # Convert the number to string
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

    # Create a fixed datetime for the new shipment
    # This simulates a system-generated datetime without using libraries

    # Generate fixed date/time components using simple algorithm instead of random
    # Using system-derived values based on shipment ID for deterministic but varied results

    # Calculate numeric value based on shipment ID
    id_sum = sum(ord(char) for char in shipmentID)

    # Generate fixed year
    year = "2025"

    # Generate month (1-12) based on shipment ID
    month = str(1 + (id_sum % 12)).zfill(2)

    # Generate day (1-28) based on shipment ID
    day = str(1 + ((id_sum * 3) % 28)).zfill(2)

    # Generate time components based on shipment ID
    hour = str((id_sum * 7) % 24).zfill(2)
    minute = str((id_sum * 11) % 60).zfill(2)
    second = str((id_sum * 13) % 60).zfill(2)

    # Format the datetime string in YYYY-MM-DD HH:MM:SS format
    fixed_datetime = f"{year}-{month}-{day} {hour}:{minute}:{second}"
    delivery_datetime.append(fixed_datetime)

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
    print(f"Date/Time: {fixed_datetime}")

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
            print(f"Date/Time: {delivery_datetime[i]}")

        print("-" * 40)

    input("\nPress Enter to continue...")
    return


# === Fleet Management Functions ===

# Replace the fleet management functions in the first code with these functions

def add_vehicle():
    """
    Add a new vehicle to the fleet.

    This function:
    - Gets vehicle details from user
    - Validates input format for vehicle ID (VXXXXXX)
    - Ensures vehicle ID is unique
    - Adds valid vehicle to the list
    """
    print("\n===== Add Vehicle to Fleet =====")

    # Get vehicle ID and validate format
    veh_code = input("Enter Vehicle ID (format: VXXXXXX): ").upper()

    # Check if vehicle ID follows the correct format (starts with V and has 6 characters after)
    if not veh_code.startswith("V") or len(veh_code) != 7:
        print("Error: Vehicle ID must start with 'V' followed by 6 characters.")
        input("Press Enter to continue...")
        return

    # Check if remaining characters are alphanumeric
    if not veh_code[1:].isalnum():
        print("Error: Vehicle ID must only contain letters and numbers after 'V'.")
        input("Press Enter to continue...")
        return

    # Check if vehicle ID already exists
    if veh_code in vehicles_list:
        print("Error: This Vehicle ID already exists in the system.")
        input("Press Enter to continue...")
        return

    # Get additional vehicle details
    veh_type = input("Enter Vehicle Type (e.g., Truck, Van, Car): ").strip()
    if not veh_type:
        print("Error: Vehicle type cannot be empty.")
        input("Press Enter to continue...")
        return

    veh_capacity = input("Enter Load Capacity (kg): ").strip()
    # Validate capacity is a positive number
    if not veh_capacity.isdigit() or int(veh_capacity) <= 0:
        print("Error: Capacity must be a positive number.")
        input("Press Enter to continue...")
        return

    # All validations passed, add vehicle to the list
    vehicles_list.append(veh_code)

    # In a real application, you might store additional details in another structure
    # For now, we'll just use the vehicles_list

    print(f"\nVehicle {veh_code} successfully added to the fleet!")
    input("Press Enter to continue...")


def update_vehicle():
    """
    Update vehicle information.

    This function:
    - Gets vehicle ID from user
    - Verifies vehicle exists in system
    - Updates vehicle ID, type, and capacity
    - Confirms update to user
    """
    print("\n===== Update Vehicle Information =====")

    if not vehicles_list:
        print("No vehicles in the fleet. Please add vehicles first.")
        input("Press Enter to continue...")
        return

    # Display all vehicles first
    print("Current Vehicles:")
    for i, vehicle in enumerate(vehicles_list):
        # If we have parallel lists for details, show them
        if i < len(vehicle_types) and i < len(vehicle_capacities):
            print(f"{i + 1}. {vehicle} (Type: {vehicle_types[i]}, Capacity: {vehicle_capacities[i]} kg)")
        else:
            print(f"{i + 1}. {vehicle}")

    # Get vehicle to update
    veh_code = input("\nEnter Vehicle ID to update: ").upper()

    # Check if vehicle exists
    if veh_code not in vehicles_list:
        print("Error: Vehicle ID not found in the system.")
        input("Press Enter to continue...")
        return

    # Get the index of the vehicle
    index = vehicles_list.index(veh_code)

    # Get updated information
    print(f"\nUpdating Vehicle {veh_code}")

    # 1. Optionally update the ID
    new_id = input("Enter new Vehicle ID (or press Enter to keep current): ").upper()

    # If new ID provided, validate it
    if new_id:
        # Check format
        if not new_id.startswith("V") or len(new_id) != 7:
            print("Error: Vehicle ID must start with 'V' followed by 6 characters.")
            input("Press Enter to continue...")
            return

        # Check alphanumeric
        if not new_id[1:].isalnum():
            print("Error: Vehicle ID must only contain letters and numbers after 'V'.")
            input("Press Enter to continue...")
            return

        # Check not already in use (except by current vehicle)
        if new_id in vehicles_list and new_id != veh_code:
            print("Error: This Vehicle ID is already in use.")
            input("Press Enter to continue...")
            return

    # 2. Update vehicle type
    current_type = vehicle_types[index] if index < len(vehicle_types) else "Unknown"
    print(f"Current Vehicle Type: {current_type}")
    new_type = input("Enter new Vehicle Type (or press Enter to keep current): ").strip()

    # 3. Update vehicle capacity
    current_capacity = vehicle_capacities[index] if index < len(vehicle_capacities) else "Unknown"
    print(f"Current Load Capacity: {current_capacity} kg")
    new_capacity = input("Enter new Load Capacity in kg (or press Enter to keep current): ").strip()

    # Validate capacity if provided
    if new_capacity:
        if not new_capacity.isdigit() or int(new_capacity) <= 0:
            print("Error: Capacity must be a positive number.")
            input("Press Enter to continue...")
            return

    # Apply all updates

    # Update ID if provided
    if new_id:
        vehicles_list[index] = new_id
        print(f"Vehicle ID updated from {veh_code} to {new_id}")

    # Update type if provided
    if new_type:
        # Ensure the vehicle_types list is long enough
        while len(vehicle_types) <= index:
            vehicle_types.append("Unknown")
        vehicle_types[index] = new_type
        print(f"Vehicle Type updated to: {new_type}")

    # Update capacity if provided
    if new_capacity:
        # Ensure the vehicle_capacities list is long enough
        while len(vehicle_capacities) <= index:
            vehicle_capacities.append("0")
        vehicle_capacities[index] = new_capacity
        print(f"Vehicle Capacity updated to: {new_capacity} kg")

    print("\nVehicle information updated successfully!")
    input("Press Enter to continue...")


def remove_vehicle():
    """
    Remove a vehicle from the fleet.

    This function:
    - Gets vehicle ID from user
    - Verifies vehicle exists
    - Removes vehicle from system
    """
    print("\n===== Remove Vehicle from Fleet =====")

    if not vehicles_list:
        print("No vehicles in the fleet to remove.")
        input("Press Enter to continue...")
        return

    # Display all vehicles
    print("Current Vehicles:")
    for i, vehicle in enumerate(vehicles_list):
        print(f"{i + 1}. {vehicle}")

    # Get vehicle to remove
    veh_code = input("\nEnter Vehicle ID to remove: ").upper()

    # Check if vehicle exists
    if veh_code not in vehicles_list:
        print("Error: Vehicle ID not found in the system.")
        input("Press Enter to continue...")
        return

    # Check if vehicle is assigned to any shipments
    if veh_code in vehicles_selected:
        print("Error: Cannot remove vehicle as it is assigned to one or more shipments.")
        input("Press Enter to continue...")
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to remove vehicle {veh_code}? (y/n): ").lower()
    if confirm != 'y':
        print("Vehicle removal cancelled.")
        input("Press Enter to continue...")
        return

    # Remove vehicle
    vehicles_list.remove(veh_code)
    print(f"Vehicle {veh_code} has been removed from the fleet.")
    input("Press Enter to continue...")


def view_fleet():
    """
    Display all vehicles in the fleet with complete information.
    """
    print("\n===== Fleet Vehicles =====")

    if not vehicles_list:
        print("No vehicles in the fleet.")
        input("Press Enter to continue...")
        return

    print(f"Total Vehicles: {len(vehicles_list)}")
    print("-" * 50)

    # Print header
    print(f"{'No.':<4} {'Vehicle ID':<10} {'Type':<15} {'Capacity (kg)':<15} {'Assigned':<10}")
    print("-" * 50)

    for i, vehicle in enumerate(vehicles_list):
        # Get vehicle type (if available)
        veh_type = vehicle_types[i] if i < len(vehicle_types) else "Unknown"

        # Get vehicle capacity (if available)
        veh_capacity = vehicle_capacities[i] if i < len(vehicle_capacities) else "Unknown"

        # Check if vehicle is assigned to any shipments
        assigned = "Yes" if vehicle in vehicles_selected else "No"

        # Print complete vehicle information
        print(f"{i + 1:<4} {vehicle:<10} {veh_type:<15} {veh_capacity:<15} {assigned:<10}")

    print("-" * 50)
    input("Press Enter to continue...")

# === Delivery Management Functions ===

def record_delivery():
    """
    Record a delivery for a shipment.

    This function allows marking a shipment as delivered by:
    - Getting a shipment ID from user
    - Validating the shipment ID exists
    - Marking the shipment as delivered with current date/time
    - Confirming the delivery has been recorded
    """
    print("\n===== Record Delivery for a Shipment =====")

    if not shipment_ids_list:
        print("No shipments found in the system to mark as delivered.")
        input("Press Enter to continue...")
        return

    shipment_id = input("Enter your shipment ID to mark as delivered.\n"
                        "Remember the format: Axxxxxxxxxxxxxx: ").upper()

    # Validate shipment ID format and existence
    if len(shipment_id) != 15 or not shipment_id.startswith("A"):
        print("Error: Invalid shipment ID format. Please try again!")
        input("Press Enter to continue...")
        return

    # Check if shipment exists
    if shipment_id not in shipment_ids_list:
        print("\nError: Shipment ID not found. Please try again!")
        input("Press Enter to continue...")
        return

    # Get the index of the shipment
    index = shipment_ids_list.index(shipment_id)

    # Check if already delivered
    if delivery_status[index] == "delivered":
        print(f"\nThis shipment has already been marked as delivered on {delivery_datetime[index]}.")
        input("Press Enter to continue...")
        return

    # Mark as delivered and create a simulated date/time string
    delivery_status[index] = "delivered"

    # Create a simple simulated date/time string without external libraries
    # Instead of using random, use a deterministic approach based on shipment ID

    # Generate a unique value based on shipment ID
    id_value = sum(ord(char) for char in shipment_id)

    # Generate year
    year = "2025"

    # Generate month (1-12) based on shipment ID
    month = str(1 + (id_value % 12)).zfill(2)

    # Generate day (1-28) based on shipment ID
    day = str(1 + ((id_value * 5) % 28)).zfill(2)

    # Generate time components based on shipment ID
    hour = str((id_value * 9) % 24).zfill(2)
    minute = str((id_value * 17) % 60).zfill(2)
    second = str((id_value * 23) % 60).zfill(2)

    # Create the date/time string in format: YYYY-MM-DD HH:MM:SS
    simulated_datetime = f"{year}-{month}-{day} {hour}:{minute}:{second}"
    delivery_datetime[index] = simulated_datetime

    print("\nThe delivery has been successfully marked as delivered.")
    print(f"Delivery recorded at: {simulated_datetime}")
    input("Press Enter to continue...")


def view_delivery_status():
    """
    View delivery status for a shipment.

    This function allows checking the delivery status of a shipment by:
    - Getting a shipment ID from user
    - Validating the shipment ID exists
    - Displaying the current delivery status
    - If delivered, showing the delivery date/time
    """
    print("\n===== View Delivery Status for a Shipment =====")

    if not shipment_ids_list:
        print("No shipments found in the system to check status.")
        input("Press Enter to continue...")
        return

    shipment_id = input("Enter your shipment ID to check delivery status.\n"
                        "Remember the format: Axxxxxxxxxxxxxx: ").upper()

    # Validate shipment ID format and existence
    if len(shipment_id) != 15 or not shipment_id.startswith("A"):
        print("Error: Invalid shipment ID format. Please try again!")
        input("Press Enter to continue...")
        return

    # Check if shipment exists
    if shipment_id not in shipment_ids_list:
        print("\nError: Shipment ID not found. Please try again!")
        input("Press Enter to continue...")
        return

    # Get the index of the shipment
    index = shipment_ids_list.index(shipment_id)

    # Display status information
    print(f"\nShipment ID: {shipment_id}")
    print(f"Origin: {origins_list[index]}")
    print(f"Destination: {destinations_list[index]}")
    print(f"Weight: {weights_list[index]} kg")
    print(f"Vehicle: {vehicles_selected[index]}")

    if delivery_status[index] == "delivered":
        # If the shipment has been marked as delivered
        print(f"Status: Delivered")
        print(f"Delivery Date/Time: {delivery_datetime[index]}")
    else:
        # Generate a tracking status based on the shipment ID
        status_code = sum(ord(char) for char in shipment_id) % 3

        if status_code == 0:
            status = "Processing"
        elif status_code == 1:
            status = "In Transit"
        else:  # status_code == 2
            status = "Out for Delivery"

        print(f"Status: {status}")
        print(f"Date/Time: {delivery_datetime[index]}")
        print("To mark this shipment as delivered, please select 'Record delivery for a shipment' option.")

    input("Press Enter to continue...")

# Start the program by directly calling the main function
main()