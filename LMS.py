#!/usr/bin/env python3

"""
Logistics Management System Skeleton using OOP principles

This program provides a menu-based interface for managing a logistics operation,
including fleet, customers, shipments, and deliveries.

Data Storage: This system uses dictionaries to store and manage data, which offers
fast lookups by ID and flexible storage of varying data structures.
"""
import random
import string
import datetime
import re

# Library needed for the signature displayed at the end of the program.

from colorama import Fore, Style, init

# Initialize colorama
init()

def display_signature():
    # Define colors
    border = Fore.CYAN
    code = Fore.MAGENTA
    crafted = Fore.BLUE
    with_text = Fore.GREEN
    heart = Fore.RED
    by = Fore.YELLOW
    name = Fore.WHITE
    reset = Style.RESET_ALL

    # Text with both names
    content = f"   {code}Code{reset} {crafted}crafted{reset} {with_text}with{reset} {heart}♥{reset} {by}by{reset} {name}Jael & Patrick{reset}   "
    content_length = len("   Code crafted with ♥ by Jael & Patrick   ")

    # Create a double-line border that's proportional to the content
    top_border = f"{border}╔{'═' * (content_length + 2)}╗{reset}"
    side_border = f"{border}║{reset}"
    bottom_border = f"{border}╚{'═' * (content_length + 2)}╝{reset}"

    # Print the signature with proper spacing
    print("\n" + top_border)
    print(f"{side_border} {content} {side_border}")
    print(bottom_border + "\n")

class DataStore:
    """Base class for data storage

    This class provides a foundation for storing, retrieving, and managing data
    using dictionaries. It offers methods to add, update, remove, and find items.
    """

    def __init__(self):
        self.data = {}  # Dictionary to store items with their IDs as keys
        self.__last_id = 0  # Private attribute to track the last assigned ID (not used for random IDs)

    def add(self, item):
        """Add an item to the data store with auto-generated ID

        The ID will be randomly generated, 8 characters long, and prefixed with
        a letter indicating the type of the object (V, C, S, D, or I).
        """
        # Determine the prefix based on item type
        if isinstance(item, Vehicle):
            prefix = "V"
        elif isinstance(item, Customer):
            prefix = "C"
        elif isinstance(item, Shipment):
            prefix = "S"
        elif isinstance(item, Delivery):
            prefix = "D"
        else:
            prefix = "I"  # For any other item types

        # Generate random alphanumeric part (7 characters to make total length 8 with prefix)
        alphabet = string.ascii_uppercase + string.digits
        random_part = ''.join(random.choices(alphabet, k=7))

        # Create the full ID
        item_id = f"{prefix}{random_part}"

        # Set the ID on the item and store it
        item.id = item_id
        self.data[item_id] = item
        return item_id

    def update(self, item_id, item):
        """Update an existing item"""
        if item_id in self.data:
            self.data[item_id] = item
            return True
        return False

    def remove(self, item_id):
        """Remove an item by ID"""
        if item_id in self.data:
            del self.data[item_id]
            return True
        return False

    def find(self, item_id):
        """Find an item by ID"""
        return self.data.get(item_id)

    def find_all(self):
        """Return all items"""
        return list(self.data.values())


class Menu:
    """Base Menu class that all submenus will inherit from

    This is the foundation for all menus in the system.
    """

    def __init__(self, title):
        self.title = title
        self.options = []
        self.quit_options = ['q', 'Q', 'quit', 'Quit', '0']

    def add_option(self, option_num, description, function):
        """Add an option to the menu"""
        self.options.append({
            'number': option_num,
            'description': description,
            'function': function
        })

    def display(self):
        """Display the menu options"""
        print(f"\n===== {self.title} =====")
        for option in self.options:
            print(f"{option['number']}. {option['description']}")

    def execute(self):
        """Execute the menu and handle user input"""
        while True:
            self.display()
            choice = input("\nSelect the menu to display (You can choose either the name "
                           "or the number of the desired menu): ")

            # Check if user wants to quit
            if choice in self.quit_options:
                print(f"Exiting {self.title}...")
                break

            # Find the selected option
            selected = None
            for option in self.options:
                # Check for number match
                if choice == str(option['number']) or choice == option['number']:
                    selected = option
                    break
                # Check for text match (case insensitive)
                elif option['description'].lower() == choice.lower():
                    selected = option
                    break

            # Execute the selected function or display error
            if selected:
                selected['function']()
            else:
                print("Invalid option. Please try again.")


# Base data classes
'''
** @author Jael **
'''
class Vehicle:
    """Class representing a vehicle in the fleet.

    This class stores all information related to a vehicle in the logistics system.
    """

    def __init__(self, vehicle_id=None, type=None, capacity=None, status="Available"):
        self.id = vehicle_id  # This will be set by the DataStore when added
        self.type = type
        self.capacity = capacity
        self.status = status
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_info(self):
        """Display vehicle information."""
        print(f"Vehicle ID: {self.id}\n"
              f"Type: {self.type}\n"
              f"Capacity: {self.capacity}\n"
              f"Status: {self.status}\n"
              f"Date: {self.date}")

class Customer:
    """Class representing a customer."""

    def __init__(self, customer_id=None, name=None, birthday=None,
                 address=None, email=None, phone=None):
        self.id = customer_id  # This will be set by the DataStore when added
        self.name = name
        self.dob = birthday
        self.address = address
        self.email = email
        self.phone = phone
        self.shipment_ids = []  # Store IDs of shipments instead of objects

    def display_info(self):
        """Display customer information."""
        print(f"Customer ID: {self.id}\n"
              f"Name: {self.name}\n"
              f"Birthday: {self.dob}\n"
              f"Address: {self.address}\n"
              f"Email: {self.email}\n"
              f"Phone: {self.phone}\n")


'''
** @author Jael **
'''
class Shipment:
    """Class representing a shipment."""

    def __init__(self, shipment_id=None, customer_id=None,
                 origin=None, destination=None, weight=None, vehicle_id=None):
        self.id = shipment_id  # This will be set by the DataStore when added
        self.customer_id = customer_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.vehicle_id = vehicle_id
        self.status = "Pending"  # Initial status
        self.delivery_id = None  # Will be set when delivery is created

    def display_info(self, customer_name=None, vehicle_type=None):
        """Display shipment information."""
        print(f"Shipment ID: {self.id}")
        print(f"Customer: {customer_name if customer_name else self.customer_id}")
        print(f"Origin: {self.origin}")
        print(f"Destination: {self.destination}")
        print(f"Weight: {self.weight}")
        print(f"Vehicle: {vehicle_type if vehicle_type else self.vehicle_id}")
        print(f"Status: {self.status}")


class Delivery:
    """Class representing a delivery."""

    def __init__(self, delivery_id=None, shipment_id=None, delivery_date=None, status="Scheduled"):
        self.id = delivery_id  # This will be set by the DataStore when added
        self.shipment_id = shipment_id
        self.delivery_date = delivery_date
        self.status = status

    def display_info(self, shipment_info=None):
        """Display delivery information."""
        print(f"Delivery ID: {self.id}")
        print(f"Shipment ID: {self.shipment_id}")
        if shipment_info:
            print(f"Shipment: {shipment_info}")
        print(f"Delivery Date: {self.delivery_date}")
        print(f"Status: {self.status}")

'''
** @author Jael **
'''
# Manager classes with menu inheritance
class FleetMenu(Menu):
    """Fleet Management Menu derived from base Menu

    This menu handles all operations related to vehicle management.
    It inherits basic menu functionality from the Menu class.
    """

    def __init__(self, vehicle_store):
        super().__init__("Fleet Management")
        self.vehicle_store = vehicle_store  # Reference to the vehicle data store
        self.__status = "Available"

        # Add menu options
        self.add_option('1', 'Add a vehicle', self.add_vehicle)
        self.add_option('2', 'Update vehicle information', self.update_vehicle)
        self.add_option('3', 'Remove a vehicle', self.remove_vehicle)
        self.add_option('4', 'View all vehicles', self.view_vehicles)
        self.add_option('5', 'Quit fleet management', lambda: None)  # Just for display

    def add_vehicle(self):
        """Add a new vehicle to the fleet."""
        print("\n=== Add a New Vehicle ===")

        # Get vehicle details from user
        # Validate vehicle type
        while True:
            vehicle_type = input("Enter vehicle type: ").title()
            if (re.match(r'^[a-zA-Z][a-zA-Z\s]*$', vehicle_type)
                and len(vehicle_type) >= 3):
                break
            else:
                print(
                    "Error: The vehicle type must contain only "
                    "letters or spaces and be at least 3 characters long.")

        # Validate capacity
        while True:
            user_input = input("Enter vehicle capacity: ")
            try:
                # First try to convert to float
                capacity = float(user_input)

                # Check if the value is positive
                if capacity <= 0:
                    print("Please validate your input, no zero values are allowed.")
                    continue

                # If it's actually an integer, convert it
                if capacity.is_integer():
                    capacity = int(capacity)

                break  # Valid input, exit the loop

            except ValueError:
                print("Please validate your input. Only numbers are allowed.")
        status = self.__status

        # Create new vehicle object
        vehicle = Vehicle(type=vehicle_type, capacity=capacity, status=status)

        # Add to data store
        vehicle_id = self.vehicle_store.add(vehicle)
        print(f"Vehicle added successfully with ID: {vehicle_id}")
        print("\033[92m Code by Jael\033[00m")

    def update_vehicle(self):
        """Update an existing vehicle's information."""
        print("\n=== Update Vehicle Information ===")

        # Get vehicle ID
        vehicle_id = input("Enter vehicle ID to update: ")
        vehicle = self.vehicle_store.find(vehicle_id)

        if not vehicle:
            print(f"No vehicle found with ID: {vehicle_id}")
            return

        # Display current info
        print("Current vehicle information:")
        vehicle.display_info()

        # Get updated information
        while True:
            vehicle_type = input(f"Enter new type (or press Enter to keep '{vehicle.type}'): ").title() or vehicle.type
            if (re.match(r'^[a-zA-Z][a-zA-Z\s]*$', vehicle_type)
                and len(vehicle_type) >= 3):
                break
            else:
                print(
                    "Error: The vehicle type must contain only "
                    "letters or spaces and be at least 3 characters long.")

        # Validate capacity
        while True:
            user_input = input(f"Enter new capacity (or press Enter to keep '{vehicle.capacity}'): ") or str(vehicle.capacity)
            try:
                # First try to convert to float
                capacity = float(user_input)
                # Check if the value is positive
                if capacity <= 0:
                    print("Please validate your input, no zero values are allowed.")
                    continue
                # If it's actually an integer, convert it
                if capacity.is_integer():
                    capacity = int(capacity)
                break  # Valid input, exit the loop
            except ValueError:
                print("Please validate your input. Only numbers are allowed.")
        status = input(f"Enter new status (or press Enter to keep '{vehicle.status}'): ") or vehicle.status

        # Update vehicle object
        vehicle.type = vehicle_type
        vehicle.capacity = capacity
        vehicle.status = status

        # Update in data store
        self.vehicle_store.update(vehicle_id, vehicle)
        print("Vehicle information updated successfully.")
        print("\033[92m Code by Jael\033[00m")

    def remove_vehicle(self):
        """Remove a vehicle from the fleet."""
        print("\n=== Remove a Vehicle ===")

        # Get vehicle ID
        vehicle_id = input("Enter vehicle ID to remove: ")
        vehicle = self.vehicle_store.find(vehicle_id)

        if not vehicle:
            print(f"No vehicle found with ID: {vehicle_id}")
            return

        # Display vehicle info before removal
        print("Vehicle to be removed:")
        vehicle.display_info()


        # Confirm removal
        confirm = input("Are you sure you want to remove this vehicle? (y/n): ")
        if confirm.lower() == 'y':
            self.vehicle_store.remove(vehicle_id)
            print("Vehicle removed successfully.")
            print("\033[92m Code by Jael\033[00m")
        else:
            print("Removal cancelled.")

    def view_vehicles(self):
        """Display all vehicles in the fleet."""
        print("\n=== All Vehicles ===")

        vehicles = self.vehicle_store.find_all()
        if not vehicles:
            print("No vehicles in the fleet.")
            return

        for vehicle in vehicles:
            vehicle.display_info()
            print("-" * 30)
        print("\033[92m Code by Jael\033[00m")


class CustomerMenu(Menu):
    """Customer Management Menu derived from base Menu"""

    def __init__(self, customer_store, shipment_store):
        super().__init__("Customer Management")
        self.customer_store = customer_store  # Reference to the customer data store
        self.shipment_store = shipment_store  # Reference to the shipment data store

        # Add menu options
        self.add_option('1', 'Add a customer', self.add_customer)
        self.add_option('2', 'Update customer information', self.update_customer)
        self.add_option('3', 'Remove a customer', self.remove_customer)
        self.add_option('4', 'View all customers', self.view_customers)
        self.add_option('5', 'View a customer\'s shipments', self.view_customer_shipments)
        self.add_option('6', 'Quit customer management', lambda: None)  # Just for display

    def add_customer(self):
        """Add a new customer."""
        print("\n=== Add a New Customer ===")

        # Get customer details from user
        while True:
            name = input("Enter customer name (first and last name): ").title()
            # Check if name has at least two words
            words = name.split()
            if (re.match(r'^[a-zA-Z][a-zA-Z\s]*$', name)
                    and len(words) >= 2
                    and len(name) >= 6):
                break
            else:
                print(
                    "The customer name must contain at least two words "
                    "(first and last name), only letters or spaces, "
                    "and be at least 6 characters long.")

        while True:
            date_str = input("Enter birthday (dd-mm-yyyy): ")
            try:
                d = datetime.datetime.strptime(date_str, '%d-%m-%Y')
                today = datetime.datetime.now()

                # Check if date is in the future
                if d > today:
                    print("Birthday cannot be in the future!")
                    continue

                # Check if age is reasonable (not over 120 years)
                age = today.year - d.year - ((today.month, today.day) < (d.month, d.day))
                if age > 120:
                    print("Please enter a valid birthday (age cannot exceed 120 years).")
                    continue

                if age < 18:
                    print("You are under 18 years. You need to be over 18 years to use the program.")
                    continue

                break
            except ValueError:
                print("Invalid date format! Please use dd-mm-yyyy format.")

        while True:
            address = input("Enter Australian address: ").title().strip()

            # Define the address pattern
            address_pattern = r"""
                ^
                (?:(?:Unit|Apt|Apartment|Flat)\s*\d+[a-zA-Z]?[/\-\s]+)?  # Optional unit
                \d+[a-zA-Z]?(?:\s*-\s*\d+[a-zA-Z]?)?                     # Street number
                \s+
                (?:[A-Za-z][A-Za-z']+(?:\s+[A-Za-z][A-Za-z']+)*)         # Street name
                \s+
                (?:Street|St|Road|Rd|Avenue|Ave|Lane|Ln|Drive|Dr|Court|Ct|Place|Pl|Parade|Pde|Boulevard|Blvd|Terrace|Tce|Way|Highway|Hwy|Crescent|Cres|Circuit|Cct|Square|Sq|Close|Cl)\.?
                \s*,?\s*
                [A-Za-z][A-Za-z\s'-]+                                    # Suburb
                \s+
                (?:NSW|VIC|QLD|SA|WA|TAS|NT|ACT)                        # State
                \s+
                \d{4}                                                    # Postcode
                $
            """

            # Check if address matches the pattern
            if re.match(address_pattern, address, re.VERBOSE | re.IGNORECASE):
                # Additional checks
                parts = address.split()
                if len(parts) >= 5:  # Minimum components
                    break
            else:
                print(
                    "Please enter a valid Australian address.\n"
                    "Format: [Unit/]Number Street Name, Suburb STATE Postcode\n"
                    "Example: 123 Smith Street, Surry Hills NSW 2000\n"
                    "Example: Unit 5/123 Park Road, Melbourne VIC 3000"
                )

        # Email validation
        while True:
            email = input("Enter email address: ").strip().lower()

            # Email pattern
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            if re.match(email_pattern, email) and len(email) >= 6:
                # Additional checks
                if email.count('@') == 1 and not email.startswith('@') and not email.endswith('@'):
                    break

            print(
                "Please enter a valid email address.\n"
                "Format: username@domain.com\n"
                "Example: john.smith@email.com"
            )

        # Phone number validation (Australian format)
        while True:
            phone = input("Enter Australian phone number: ").strip()

            # Remove spaces, dashes, and parentheses for validation
            cleaned_phone = re.sub(r'[\s\-\(\)]', '', phone)

            # Australian phone patterns
            mobile_pattern = r'^(?:\+?61|0)4\d{8}$'  # Mobile: 04XX XXX XXX or +614XX XXX XXX
            landline_pattern = r'^(?:\+?61|0)[2378]\d{8}$'  # Landline: 02/03/07/08 XXXX XXXX

            if re.match(mobile_pattern, cleaned_phone) or re.match(landline_pattern, cleaned_phone):
                break

            print(
                "Please enter a valid Australian phone number.\n"
                "Mobile format: 04XX XXX XXX or +614XX XXX XXX\n"
                "Landline format: (0X) XXXX XXXX or +61X XXXX XXXX\n"
                "Examples: 0412 345 678, (02) 1234 5678, +61 412 345 678"
            )

        # Create new customer object - Format the date as string
        customer = Customer(name=name, birthday=d.strftime('%d-%m-%Y'),
                            address=address, email=email, phone=phone)

        # Add to data store
        customer_id = self.customer_store.add(customer)
        print(f"Customer added successfully with ID: {customer_id}")

    def update_customer(self):
        """Update an existing customer's information."""
        print("\n=== Update Customer Information ===")

        # Get customer ID
        customer_id = input("Enter customer ID to update: ")
        customer = self.customer_store.find(customer_id)

        if not customer:
            print(f"No customer found with ID: {customer_id}")
            return

        # Display current info
        print("\nCurrent customer information:")
        customer.display_info()
        print()

        # Name validation
        while True:
            new_name = input(f"Enter new name (or press Enter to keep '{customer.name}'): ").title()

            if not new_name:  # Keep existing name
                new_name = customer.name
                break

            # Check if name has at least two words
            words = new_name.split()
            if (re.match(r'^[a-zA-Z][a-zA-Z\s]*$', new_name)
                    and len(words) >= 2
                    and len(new_name) >= 6):
                break
            else:
                print(
                    "The customer name must contain at least two words "
                    "(first and last name), only letters or spaces, "
                    "and be at least 6 characters long.")

        # Birthday validation - USE dob attribute and format properly!
        while True:
            date_str = input(f"Enter new birthday dd-mm-yyyy (or press Enter to keep current): ")

            if not date_str:  # Keep existing birthday
                new_birthday = customer.dob  # Keep as string
                break

            try:
                d = datetime.datetime.strptime(date_str, '%d-%m-%Y')
                today = datetime.datetime.now()

                # Check if date is in the future
                if d > today:
                    print("Birthday cannot be in the future!")
                    continue

                # Check if age is reasonable (not over 120 years)
                age = today.year - d.year - ((today.month, today.day) < (d.month, d.day))
                if age > 120:
                    print("Please enter a valid birthday (age cannot exceed 120 years).")
                    continue

                if age < 18:
                    print("You are under 18 years. You need to be over 18 years to use the program.")
                    continue

                new_birthday = d.strftime('%d-%m-%Y')  # Format as dd-mm-yyyy string
                break
            except ValueError:
                print("Invalid date format! Please use dd-mm-yyyy format.")

        # Address validation
        while True:
            new_address = input(f"Enter new address (or press Enter to keep current): ").title().strip()

            if not new_address:  # Keep existing address
                new_address = customer.address
                break

            # Define the address pattern
            address_pattern = r"""
                ^
                (?:(?:Unit|Apt|Apartment|Flat)\s*\d+[a-zA-Z]?[/\-\s]+)?  # Optional unit
                \d+[a-zA-Z]?(?:\s*-\s*\d+[a-zA-Z]?)?                     # Street number
                \s+
                (?:[A-Za-z][A-Za-z']+(?:\s+[A-Za-z][A-Za-z']+)*)         # Street name
                \s+
                (?:Street|St|Road|Rd|Avenue|Ave|Lane|Ln|Drive|Dr|Court|Ct|Place|Pl|Parade|Pde|Boulevard|Blvd|Terrace|Tce|Way|Highway|Hwy|Crescent|Cres|Circuit|Cct|Square|Sq|Close|Cl)\.?
                \s*,?\s*
                [A-Za-z][A-Za-z\s'-]+                                    # Suburb
                \s+
                (?:NSW|VIC|QLD|SA|WA|TAS|NT|ACT)                        # State
                \s+
                \d{4}                                                    # Postcode
                $
            """

            # Check if address matches the pattern
            if re.match(address_pattern, new_address, re.VERBOSE | re.IGNORECASE):
                # Additional checks
                parts = new_address.split()
                if len(parts) >= 5:  # Minimum components
                    break
            else:
                print(
                    "Please enter a valid Australian address.\n"
                    "Format: [Unit/]Number Street Name, Suburb STATE Postcode\n"
                    "Example: 123 Smith Street, Surry Hills NSW 2000\n"
                    "Example: Unit 5/123 Park Road, Melbourne VIC 3000"
                )

        # Email validation
        while True:
            new_email = input(f"Enter new email (or press Enter to keep current): ").strip().lower()

            if not new_email:  # Keep existing email
                new_email = customer.email
                break

            # Email pattern
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            if re.match(email_pattern, new_email) and len(new_email) >= 6:
                # Additional checks
                if new_email.count('@') == 1 and not new_email.startswith('@') and not new_email.endswith('@'):
                    break

            print(
                "Please enter a valid email address.\n"
                "Format: username@domain.com\n"
                "Example: john.smith@email.com"
            )

        # Phone number validation (Australian format)
        while True:
            new_phone = input(f"Enter new Australian phone number (or press Enter to keep current): ").strip()

            if not new_phone:  # Keep existing phone
                new_phone = customer.phone
                break

            # Remove spaces, dashes, and parentheses for validation
            cleaned_phone = re.sub(r'[\s\-\(\)]', '', new_phone)

            # Australian phone patterns
            mobile_pattern = r'^(?:\+?61|0)4\d{8}$'  # Mobile: 04XX XXX XXX or +614XX XXX XXX
            landline_pattern = r'^(?:\+?61|0)[2378]\d{8}$'  # Landline: 02/03/07/08 XXXX XXXX

            if re.match(mobile_pattern, cleaned_phone) or re.match(landline_pattern, cleaned_phone):
                break

            print(
                "Please enter a valid Australian phone number.\n"
                "Mobile format: 04XX XXX XXX or +614XX XXX XXX\n"
                "Landline format: (0X) XXXX XXXX or +61X XXXX XXXX\n"
                "Examples: 0412 345 678, (02) 1234 5678, +61 412 345 678"
            )

        # Update customer object
        customer.name = new_name
        customer.dob = new_birthday  # Store as formatted string
        customer.address = new_address
        customer.email = new_email
        customer.phone = new_phone

        # Update in data store
        self.customer_store.update(customer_id, customer)

        print("\n✓ Customer information updated successfully!")
        print("\nUpdated information:")
        customer.display_info()

    def remove_customer(self):
        """Remove a customer."""
        print("\n=== Remove a Customer ===")

        # Get customer ID
        customer_id = input("Enter customer ID to remove: ")
        customer = self.customer_store.find(customer_id)

        if not customer:
            print(f"No customer found with ID: {customer_id}")
            return

        # Display customer info before removal
        print("Customer to be removed:")
        customer.display_info()

        # Check if customer has shipments
        if customer.shipment_ids:
            print(f"Warning: This customer has {len(customer.shipment_ids)} shipments.")
            print("Removing this customer will affect these shipments.")

        # Confirm removal
        confirm = input("Are you sure you want to remove this customer? (y/n): ")
        if confirm.lower() == 'y':
            self.customer_store.remove(customer_id)
            print("Customer removed successfully.")
        else:
            print("Removal cancelled.")

    def view_customers(self):
        """Display all customers."""
        print("\n=== All Customers ===")

        customers = self.customer_store.find_all()
        if not customers:
            print("No customers in the database.")
            return

        for customer in customers:
            customer.display_info()
            print(f"Number of shipments: {len(customer.shipment_ids)}")
            print("-" * 30)

    def view_customer_shipments(self):
        """View shipments for a specific customer."""
        print("\n=== View Customer's Shipments ===")

        # Get customer ID
        customer_id = input("Enter customer ID: ")
        customer = self.customer_store.find(customer_id)

        if not customer:
            print(f"No customer found with ID: {customer_id}")
            return

        print(f"Shipments for customer: {customer.name} (ID: {customer.id})")

        if not customer.shipment_ids:
            print("No shipments found for this customer.")
            return

        for shipment_id in customer.shipment_ids:
            shipment = self.shipment_store.find(shipment_id)
            if shipment:
                shipment.display_info(customer_name=customer.name)
                print("-" * 30)
            else:
                print(f"Warning: Shipment ID {shipment_id} not found.")

'''
** @author Jael **
'''
class ShipmentMenu(Menu):
    """Shipment Management Menu derived from base Menu"""

    def __init__(self, shipment_store, customer_store, vehicle_store, delivery_store):
        super().__init__("Shipment Management")
        self.shipment_store = shipment_store  # Reference to shipment data store
        self.customer_store = customer_store  # Reference to customer data store
        self.vehicle_store = vehicle_store  # Reference to vehicle data store
        self.delivery_store = delivery_store  # Reference to delivery data store

        # Add menu options
        self.add_option('1', 'Create a new shipment', self.create_shipment)
        self.add_option('2', 'Track a shipment', self.track_shipment)
        self.add_option('3', 'View all shipments', self.view_shipments)
        self.add_option('4', 'Quit shipment management', lambda: None)  # Just for display

    def validate_address(self, address_type):
        """Validate address format for origin or destination."""
        while True:
            address = input(f"Please enter the {address_type} address.\n"
                            "Please use: street and number, suburb, zipcode: ").lower()

            pattern = (r'^([a-zA-Z0-9][a-zA-Z0-9\s\-]{2,}),'
                       r'\s*([a-zA-Z][a-zA-Z\s-]{2,}),\s*([a-zA-Z0-9]{4,10})$')

            match = re.match(pattern, address)
            if match:
                street, suburb, zipcode = match.groups()
                print("Thank you for providing a valid format address!")
                print(f"Street and number: {street}")
                print(f"Suburb: {suburb}")
                print(f"Zipcode: {zipcode}")
                return address.title()
            else:
                print("Invalid address format. Please use: street and number, suburb, zipcode")
                retry = input("Would you like to try again? (y/n): ")
                if retry.lower() != 'y':
                    print("Returning to Shipment Management menu...")
                    return None

    def create_shipment(self):
        """Create a new shipment."""
        print("\n=== Create a New Shipment ===")

        # Get customer ID
        customer_id = input("Enter customer ID: ")
        customer = self.customer_store.find(customer_id)

        if not customer:
            print(f"No customer found with ID: {customer_id}")
            return

        # Show customer information
        print(f"\nCustomer: {customer.name}")
        print(f"Address: {customer.address}")

        # Get shipment details
        # Validate origin address with option to use customer address
        print("\n=== Origin Address ===")
        use_customer_address = input("Use customer address as origin? (y/n): ").lower()

        if use_customer_address == 'y':
            origin = customer.address
            print(f"Using customer address: {origin}")
        else:
            origin = self.validate_address("origin")
            if origin is None:  # User chose to cancel
                return

        # Validate destination address with option to use customer address
        print("\n=== Destination Address ===")
        if use_customer_address != 'y':  # Only ask if origin wasn't customer address
            use_customer_address_dest = input("Use customer address as destination? (y/n): ").lower()

            if use_customer_address_dest == 'y':
                destination = customer.address
                print(f"Using customer address: {destination}")
            else:
                destination = self.validate_address("destination")
                if destination is None:  # User chose to cancel
                    return
        else:
            destination = self.validate_address("destination")
            if destination is None:  # User chose to cancel
                return

        # Weight validation
        while True:
            weight_input = input("Please enter the weight of the package in kg: ").strip()

            if not weight_input:
                print("Weight cannot be empty. Please enter a valid weight.")
                retry = input("Would you like to try again? (y/n): ")
                if retry.lower() != 'y':
                    print("Returning to Shipment Management menu...")
                    return
                continue

            pattern = r'^\d+(\.\d+)?'
            match = re.match(pattern, weight_input)

            if match:
                weight = float(weight_input)

                if weight <= 0:
                    print("Weight must be greater than zero. Please enter a positive weight.")
                    retry = input("Would you like to try again? (y/n): ")
                    if retry.lower() != 'y':
                        print("Returning to Shipment Management menu...")
                        return
                    continue

                if weight.is_integer():
                    weight = int(weight)

                print(f"The weight typed is: {weight} kg.")
                break
            else:
                print("This is not a valid input. Try again.\n"
                      "Remember that only positive numbers are allowed")
                retry = input("Would you like to try again? (y/n): ")
                if retry.lower() != 'y':
                    print("Returning to Shipment Management menu...")
                    return

        # Get available vehicles that can carry the weight
        vehicles = self.vehicle_store.find_all()
        available_vehicles = [v for v in vehicles if v.status == "Available" and v.capacity >= weight]

        if not available_vehicles:
            print(f"No available vehicles can carry {weight} kg.")
            print("The shipment will be created without vehicle assignment.")
            vehicle_id = None
        else:
            # Display available vehicles that can handle the weight
            while True:
                print(f"\n=== Available Vehicles (can carry {weight} kg) ===")
                for i, vehicle in enumerate(available_vehicles):
                    print(f"{i + 1}.- {vehicle.id} - {vehicle.type} (Capacity: {vehicle.capacity} kg)")

                choice = input("\nPlease select a vehicle (enter number, vehicle ID, or press Enter to skip): ").strip()

                if not choice:
                    print("No vehicle assigned to this shipment.")
                    vehicle_id = None
                    break

                if choice.isdigit():
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(available_vehicles):
                        selected_vehicle = available_vehicles[choice_num - 1]
                        print(f"You chose the vehicle ID: {selected_vehicle.id}")
                        vehicle_id = selected_vehicle.id
                        break
                else:
                    vehicle_found = False
                    for vehicle in available_vehicles:
                        if choice.upper() == vehicle.id.upper():
                            print(f"You chose the vehicle ID: {vehicle.id}")
                            vehicle_id = vehicle.id
                            vehicle_found = True
                            break

                    if vehicle_found:
                        break

                print("Invalid selection. Please try again.")
                retry = input("Would you like to try again? (y/n): ")
                if retry.lower() != 'y':
                    print("No vehicle assigned to this shipment.")
                    vehicle_id = None
                    break

        # Create new shipment
        shipment = Shipment(
            customer_id=customer_id,
            origin=origin,
            destination=destination,
            weight=weight,
            vehicle_id=vehicle_id
        )

        # Add to data store
        shipment_id = self.shipment_store.add(shipment)

        # Update customer's shipment list
        customer.shipment_ids.append(shipment_id)
        self.customer_store.update(customer_id, customer)

        print(f"\nShipment created successfully with ID: {shipment_id}")
        print(f"Origin: {origin}")
        print(f"Destination: {destination}")
        print(f"Weight: {weight} kg")
        if vehicle_id:
            print(f"Assigned Vehicle: {vehicle_id}")
        else:
            print("No vehicle assigned")

    def generate_status(self, shipment_id):
        """Generate a status message based on shipment ID."""
        status_messages = {
            0: "Your shipment is being processed",
            1: "Your shipment is in transit",
            2: "Your shipment is out for delivery",
            3: "Your shipment is at the destination facility"
        }
        status_code = sum(ord(char) for char in shipment_id) % 4
        return status_messages[status_code]

    def get_customer_name(self, customer_id):
        """Get customer name by ID."""
        customer = self.customer_store.find(customer_id)
        return customer.name if customer else "Unknown"

    def get_vehicle_type(self, vehicle_id):
        """Get vehicle type by ID."""
        if not vehicle_id:
            return "Not assigned"
        vehicle = self.vehicle_store.find(vehicle_id)
        return vehicle.type if vehicle else "Not assigned"

    def get_delivery_status(self, shipment):
        """Get delivery status information for a shipment."""
        if not shipment.delivery_id:
            return None

        delivery = self.delivery_store.find(shipment.delivery_id)
        if not delivery:
            return None

        if delivery.status == "Delivered":
            return {
                "status": "Your shipment has been delivered",
                "date_type": "Delivery Date",
                "date": delivery.delivery_date
            }
        else:
            return {
                "status": delivery.status,
                "date_type": "Scheduled Date",
                "date": delivery.delivery_date
            }

    def track_shipment(self):
        """Track a shipment's status."""
        print("\n=== Track a Shipment ===")

        # Validation function
        is_valid_format = lambda sid: len(sid) == 8 and sid.startswith("S")

        while True:
            shipment_id = input("Please enter your Shipment ID (Sxxxxxxx): ").upper()

            # Validate inputs
            if not shipment_id:
                print("Error: Empty input not allowed.")
                continue

            if not is_valid_format(shipment_id):
                print("Error: Invalid format. Use S + 7 characters (e.g., S1234567)")
                if input("Try again? (y/n): ").lower() != 'y':
                    return
                continue

            # Find shipment
            shipment = self.shipment_store.find(shipment_id)
            if not shipment:
                print(f"Shipment ID {shipment_id} not found.")
                if input("Try again? (y/n): ").lower() != 'y':
                    return
                continue

            # Display information
            print(f"\n{'=' * 10} Shipment Tracking {'=' * 10}")
            print(f"ID: {shipment_id}")
            print(f"Customer: {self.get_customer_name(shipment.customer_id)}")
            print(f"Route: {shipment.origin} → {shipment.destination}")
            print(f"Weight: {shipment.weight} kg")
            print(f"Vehicle: {self.get_vehicle_type(shipment.vehicle_id)}")

            # Status display
            delivery_info = self.get_delivery_status(shipment)
            if delivery_info:
                print(f"\nStatus: {delivery_info['status']}")
                print(f"{delivery_info['date_type']}: {delivery_info['date']}")
            else:
                print(f"\nStatus: {self.generate_status(shipment_id)}")
                if shipment.status != "Pending":
                    print(f"Stage: {shipment.status}")

            input("\nPress Enter to continue...")
            return

    def calculate_simulated_delivery_date(self, shipment):
        """Calculate a simulated delivery date based on shipment properties."""
        from datetime import timedelta
        import random

        # Base date (creation date or current date)
        base_date = datetime.datetime.now()

        # Determine transit days based on various factors
        transit_days = 2  # Base transit time

        # Factor 1: Weight impact
        if shipment.weight > 100:
            transit_days += 2
        elif shipment.weight > 50:
            transit_days += 1

        # Factor 2: Vehicle type impact
        vehicle = self.vehicle_store.find(shipment.vehicle_id) if shipment.vehicle_id else None
        if vehicle:
            vehicle_delays = {
                'Motorcycle': -1,  # Faster for small packages
                'Van': 0,
                'Truck': 1,
                'Cargo Ship': 5,
                'Airplane': -2  # Fastest
            }
            transit_days += vehicle_delays.get(vehicle.type, 0)

        # Factor 3: Random delay simulation (weather, traffic, etc.)
        random_delay = random.randint(0, 2)
        transit_days += random_delay

        # Factor 4: Shipment ID based variation (consistent for same ID)
        id_factor = sum(ord(char) for char in shipment.id) % 3
        transit_days += id_factor

        # Ensure minimum 1 day transit
        transit_days = max(1, transit_days)

        # Calculate delivery date, skipping weekends
        delivery_date = base_date
        days_added = 0

        while days_added < transit_days:
            delivery_date += timedelta(days=1)
            # Skip weekends (5 = Saturday, 6 = Sunday)
            if delivery_date.weekday() < 5:
                days_added += 1

        return delivery_date.strftime('%Y-%m-%d')

    def get_simulated_delivery_info(self, shipment):
        """Get simulated delivery information for display."""
        # If there's already a delivery record, use it
        if shipment.delivery_id:
            return self.get_delivery_status(shipment)

        # Generate simulated delivery date
        estimated_date = self.calculate_simulated_delivery_date(shipment)

        # Determine status based on current date and estimated delivery
        current_date = datetime.datetime.now().date()
        delivery_date = datetime.datetime.strptime(estimated_date, '%Y-%m-%d').date()

        if current_date > delivery_date:
            # Past delivery date - mark as delivered
            return {
                "status": "Your shipment has been delivered",
                "date_type": "Delivery Date",
                "date": estimated_date
            }
        elif current_date == delivery_date:
            return {
                "status": "Out for delivery today",
                "date_type": "Expected Delivery",
                "date": estimated_date
            }
        else:
            days_until = (delivery_date - current_date).days
            if days_until == 1:
                status = "Arriving tomorrow"
            else:
                status = f"In transit - arriving in {days_until} days"

            return {
                "status": status,
                "date_type": "Estimated Delivery",
                "date": estimated_date
            }

    def view_shipments(self):
        """Display all shipments with simulated delivery dates."""
        print("\n=== All Shipments ===")

        shipments = self.shipment_store.find_all()
        if not shipments:
            print("No shipments in the database.")
            return

        for shipment in shipments:
            # Display shipment info with consistent formatting
            print(f"Shipment ID: {shipment.id}")
            print(f"Customer: {self.get_customer_name(shipment.customer_id)}")
            print(f"Origin: {shipment.origin}")
            print(f"Destination: {shipment.destination}")
            print(f"Weight: {shipment.weight} kg")
            print(f"Vehicle: {self.get_vehicle_type(shipment.vehicle_id)}")

            # Status and delivery date display
            delivery_info = self.get_simulated_delivery_info(shipment)
            if delivery_info:
                print(f"Status: {delivery_info['status']}")
                print(f"{delivery_info['date_type']}: {delivery_info['date']}")
            else:
                # Fallback to original status generation
                print(f"Status: {self.generate_status(shipment.id)}")
                if shipment.status != "Pending":
                    print(f"Stage: {shipment.status}")

            print("-" * 30)


class DeliveryMenu(Menu):
    """Delivery Management Menu derived from base Menu"""

    def __init__(self, delivery_store, shipment_store, customer_store):
        super().__init__("Delivery Management")
        self.delivery_store = delivery_store  # Reference to delivery data store
        self.shipment_store = shipment_store  # Reference to shipment data store
        self.customer_store = customer_store  # Reference to customer data store

        # Add menu options
        self.add_option('1', 'Mark Shipment delivery', self.mark_delivery)
        self.add_option('2', 'View delivery status for a shipment', self.view_delivery_status)
        self.add_option('3', 'Quit delivery management', lambda: None)  # Just for display

    def mark_delivery(self):
        """Mark a shipment as delivered."""
        print("\n=== Mark Shipment Delivery ===")

        # Validation function
        is_valid_format = lambda sid: len(sid) == 8 and sid.startswith("S")

        while True:
            shipment_id = input("Enter shipment ID to mark as delivered (or 'q' to quit): ").upper()

            if shipment_id.lower() == 'q':
                return

            # Validate format
            if not is_valid_format(shipment_id):
                print("Error: Invalid format. Use S + 7 characters (e.g., S1234567)")
                continue

            # Find shipment
            shipment = self.shipment_store.find(shipment_id)
            if not shipment:
                print(f"Error: No shipment found with ID: {shipment_id}")
                continue

            # Check if already delivered
            if shipment.delivery_id:
                delivery = self.delivery_store.find(shipment.delivery_id)
                if delivery and delivery.status == "Delivered":
                    print(f"Error: This shipment has already been delivered on {delivery.delivery_date}")
                    continue

            # Automatically capture current date and time
            current_datetime = datetime.datetime.now()
            delivery_date = current_datetime.strftime("%d/%m/%Y %H:%M")

            # Create or update delivery record
            if shipment.delivery_id:
                delivery = self.delivery_store.find(shipment.delivery_id)
                delivery.status = "Delivered"
                delivery.delivery_date = delivery_date
                self.delivery_store.update(delivery.id, delivery)
            else:
                delivery = Delivery(
                    shipment_id=shipment_id,
                    delivery_date=delivery_date,
                    status="Delivered"
                )
                delivery_id = self.delivery_store.add(delivery)
                shipment.delivery_id = delivery_id

            # Update shipment status
            shipment.status = "Delivered"
            self.shipment_store.update(shipment_id, shipment)

            # Display success message
            print("\n✓ DELIVERY CONFIRMATION")
            print("=" * 30)
            print(f"Shipment ID: {shipment_id}")
            print(f"Date: {delivery_date}")
            print(f"Status: DELIVERED")

            # Get additional info
            customer = self.customer_store.find(shipment.customer_id)
            if customer:
                print(f"Customer: {customer.name}")
                print(f"Address: {shipment.destination}")

            print("=" * 30)
            print("Delivery recorded successfully!")

            # Ask if want to mark another delivery
            another = input("\nMark another delivery? (y/n): ")
            if another.lower() != 'y':
                break

    def view_delivery_status(self):
        """View the delivery status of a shipment."""
        print("\n=== View Delivery Status ===")

        # Get shipment ID
        shipment_id = input("Enter shipment ID: ")
        shipment = self.shipment_store.find(shipment_id)

        if not shipment:
            print(f"No shipment found with ID: {shipment_id}")
            return

        # Get customer info
        customer = self.customer_store.find(shipment.customer_id)
        customer_name = customer.name if customer else "Unknown"

        print(f"Shipment ID: {shipment.id}")
        print(f"Customer: {customer_name}")
        print(f"Status: {shipment.status}")

        if shipment.delivery_id:
            delivery = self.delivery_store.find(shipment.delivery_id)
            if delivery:
                print("\nDelivery Information:")
                print(f"Delivery ID: {delivery.id}")
                print(f"Delivery Date: {delivery.delivery_date}")
                print(f"Delivery Status: {delivery.status}")
            else:
                print("Delivery record not found, but shipment references a delivery.")
        else:
            print("No delivery information available for this shipment.")


class MainMenu(Menu):
    """Main Menu class for the Logistics Management System

    This class represents the top-level menu of the system, from which users can
    access all the different management areas.
    """

    def __init__(self):
        super().__init__("Logistics Management System")

        # Initialize data stores
        self.vehicle_store = DataStore()
        self.customer_store = DataStore()
        self.shipment_store = DataStore()
        self.delivery_store = DataStore()

        # Initialize submenu instances with data stores
        self.fleet_menu = FleetMenu(self.vehicle_store)
        self.customer_menu = CustomerMenu(self.customer_store, self.shipment_store)
        self.shipment_menu = ShipmentMenu(self.shipment_store, self.customer_store,
                                          self.vehicle_store, self.delivery_store)
        self.delivery_menu = DeliveryMenu(self.delivery_store, self.shipment_store,
                                          self.customer_store)

        # Add menu options
        self.add_option('1', 'Fleet Management', self.fleet_menu.execute)
        self.add_option('2', 'Customer Management', self.customer_menu.execute)
        self.add_option('3', 'Shipment Management', self.shipment_menu.execute)
        self.add_option('4', 'Delivery Management', self.delivery_menu.execute)
        self.add_option('0', 'Quit', lambda: None)  # Just for display


def main():
    """Main function to run the logistics management system.

    This is the starting point of the program. It creates the main menu and starts
    the interaction with the user.
    """
    menu = MainMenu()
    menu.execute()
    print("Thank you for using the Logistics Management System. Goodbye!")
    display_signature()


if __name__ == "__main__":
    main()