#!/usr/bin/env python3

"""
Logistics Management System Skeleton using OOP principles

This program provides a menu-based interface for managing a logistics operation,
including fleet, customers, shipments, and deliveries.

Data Storage: This system uses dictionaries to store and manage data, which offers
fast lookups by ID and flexible storage of varying data structures.
"""


class DataStore:
    """Base class for data storage

    This class provides a foundation for storing, retrieving, and managing data
    using dictionaries. It offers methods to add, update, remove, and find items.
    """

    def __init__(self):
        self.data = {}  # Dictionary to store items with their IDs as keys
        self.last_id = 0  # Track the last assigned ID for auto-incrementing

    def add(self, item):
        """Add an item to the data store with auto-generated ID"""
        self.last_id += 1
        item_id = str(self.last_id)
        item.id = item_id  # Set the ID on the item
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
        print(f"\n=== {self.title} ===")
        for option in self.options:
            print(f"{option['number']}. {option['description']}")

    def execute(self):
        """Execute the menu and handle user input"""
        while True:
            self.display()
            choice = input("\nEnter your choice: ")

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
                print("Invalid choice. Please try again.")


# Base data classes
class Vehicle:
    """Class representing a vehicle in the fleet.

    This class stores all information related to a vehicle in the logistics system.
    """

    def __init__(self, vehicle_id=None, type=None, capacity=None, status="Available"):
        self.id = vehicle_id  # This will be set by the DataStore when added
        self.type = type
        self.capacity = capacity
        self.status = status

    def display_info(self):
        """Display vehicle information."""
        print(f"Vehicle ID: {self.id}")
        print(f"Type: {self.type}")
        print(f"Capacity: {self.capacity}")
        print(f"Status: {self.status}")


class Customer:
    """Class representing a customer."""

    def __init__(self, customer_id=None, name=None, contact=None, address=None):
        self.id = customer_id  # This will be set by the DataStore when added
        self.name = name
        self.contact = contact
        self.address = address
        self.shipment_ids = []  # Store IDs of shipments instead of objects

    def display_info(self):
        """Display customer information."""
        print(f"Customer ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Address: {self.address}")


class Shipment:
    """Class representing a shipment."""

    def __init__(self, shipment_id=None, customer_id=None, origin=None, destination=None,
                 contents=None, weight=None, vehicle_id=None):
        self.id = shipment_id  # This will be set by the DataStore when added
        self.customer_id = customer_id
        self.origin = origin
        self.destination = destination
        self.contents = contents
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
        print(f"Contents: {self.contents}")
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


# Manager classes with menu inheritance
class FleetMenu(Menu):
    """Fleet Management Menu derived from base Menu

    This menu handles all operations related to vehicle management.
    It inherits basic menu functionality from the Menu class.
    """

    def __init__(self, vehicle_store):
        super().__init__("Fleet Management")
        self.vehicle_store = vehicle_store  # Reference to the vehicle data store

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
        vehicle_type = input("Enter vehicle type: ")
        capacity = input("Enter vehicle capacity: ")
        status = input("Enter vehicle status (or press Enter for 'Available'): ") or "Available"

        # Create new vehicle object
        vehicle = Vehicle(type=vehicle_type, capacity=capacity, status=status)

        # Add to data store
        vehicle_id = self.vehicle_store.add(vehicle)
        print(f"Vehicle added successfully with ID: {vehicle_id}")

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
        vehicle_type = input(f"Enter new type (or press Enter to keep '{vehicle.type}'): ") or vehicle.type
        capacity = input(f"Enter new capacity (or press Enter to keep '{vehicle.capacity}'): ") or vehicle.capacity
        status = input(f"Enter new status (or press Enter to keep '{vehicle.status}'): ") or vehicle.status

        # Update vehicle object
        vehicle.type = vehicle_type
        vehicle.capacity = capacity
        vehicle.status = status

        # Update in data store
        self.vehicle_store.update(vehicle_id, vehicle)
        print("Vehicle information updated successfully.")

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
        name = input("Enter customer name: ")
        contact = input("Enter customer contact information: ")
        address = input("Enter customer address: ")

        # Create new customer object
        customer = Customer(name=name, contact=contact, address=address)

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
        print("Current customer information:")
        customer.display_info()

        # Get updated information
        name = input(f"Enter new name (or press Enter to keep '{customer.name}'): ") or customer.name
        contact = input(f"Enter new contact (or press Enter to keep '{customer.contact}'): ") or customer.contact
        address = input(f"Enter new address (or press Enter to keep '{customer.address}'): ") or customer.address

        # Update customer object
        customer.name = name
        customer.contact = contact
        customer.address = address

        # Update in data store
        self.customer_store.update(customer_id, customer)
        print("Customer information updated successfully.")

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


class ShipmentMenu(Menu):
    """Shipment Management Menu derived from base Menu"""

    def __init__(self, shipment_store, customer_store, vehicle_store):
        super().__init__("Shipment Management")
        self.shipment_store = shipment_store  # Reference to shipment data store
        self.customer_store = customer_store  # Reference to customer data store
        self.vehicle_store = vehicle_store  # Reference to vehicle data store

        # Add menu options
        self.add_option('1', 'Create a new shipment', self.create_shipment)
        self.add_option('2', 'Track a shipment', self.track_shipment)
        self.add_option('3', 'View all shipments', self.view_shipments)
        self.add_option('4', 'Quit shipment management', lambda: None)  # Just for display

    def create_shipment(self):
        """Create a new shipment."""
        print("\n=== Create a New Shipment ===")

        # Get customer ID
        customer_id = input("Enter customer ID: ")
        customer = self.customer_store.find(customer_id)

        if not customer:
            print(f"No customer found with ID: {customer_id}")
            return

        # Get shipment details
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        contents = input("Enter contents: ")
        weight = input("Enter weight: ")

        # Get vehicle ID (optional)
        vehicle_id = input("Enter vehicle ID (or press Enter to assign later): ")
        if vehicle_id:
            vehicle = self.vehicle_store.find(vehicle_id)
            if not vehicle:
                print(f"Warning: No vehicle found with ID: {vehicle_id}")
                vehicle_id = None

        # Create new shipment
        shipment = Shipment(
            customer_id=customer_id,
            origin=origin,
            destination=destination,
            contents=contents,
            weight=weight,
            vehicle_id=vehicle_id
        )

        # Add to data store
        shipment_id = self.shipment_store.add(shipment)

        # Update customer's shipment list
        customer.shipment_ids.append(shipment_id)
        self.customer_store.update(customer_id, customer)

        print(f"Shipment created successfully with ID: {shipment_id}")

    def track_shipment(self):
        """Track a shipment's status."""
        print("\n=== Track a Shipment ===")

        # Get shipment ID
        shipment_id = input("Enter shipment ID: ")
        shipment = self.shipment_store.find(shipment_id)

        if not shipment:
            print(f"No shipment found with ID: {shipment_id}")
            return

        # Get related objects for display
        customer = self.customer_store.find(shipment.customer_id)
        customer_name = customer.name if customer else "Unknown"

        vehicle = self.vehicle_store.find(shipment.vehicle_id) if shipment.vehicle_id else None
        vehicle_type = vehicle.type if vehicle else "Not assigned"

        # Display shipment info
        print("Shipment Information:")
        shipment.display_info(customer_name=customer_name, vehicle_type=vehicle_type)

    def view_shipments(self):
        """Display all shipments."""
        print("\n=== All Shipments ===")

        shipments = self.shipment_store.find_all()
        if not shipments:
            print("No shipments in the database.")
            return

        for shipment in shipments:
            # Get customer name if available
            customer = self.customer_store.find(shipment.customer_id)
            customer_name = customer.name if customer else "Unknown"

            # Get vehicle type if available
            vehicle = self.vehicle_store.find(shipment.vehicle_id) if shipment.vehicle_id else None
            vehicle_type = vehicle.type if vehicle else "Not assigned"

            shipment.display_info(customer_name=customer_name, vehicle_type=vehicle_type)
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

        # Get shipment ID
        shipment_id = input("Enter shipment ID: ")
        shipment = self.shipment_store.find(shipment_id)

        if not shipment:
            print(f"No shipment found with ID: {shipment_id}")
            return

        # Check if delivery already exists for this shipment
        if shipment.delivery_id:
            delivery = self.delivery_store.find(shipment.delivery_id)
            if delivery:
                print(f"This shipment already has a delivery record (ID: {delivery.id}, Status: {delivery.status})")
                update = input("Do you want to update the delivery status? (y/n): ")
                if update.lower() != 'y':
                    return

                # Update existing delivery
                status = input("Enter new delivery status: ")
                delivery_date = input("Enter delivery date: ")

                delivery.status = status
                delivery.delivery_date = delivery_date

                self.delivery_store.update(delivery.id, delivery)
                print("Delivery status updated successfully.")
                return

        # Create new delivery
        delivery_date = input("Enter delivery date: ")
        status = input("Enter delivery status (or press Enter for 'Delivered'): ") or "Delivered"

        delivery = Delivery(
            shipment_id=shipment_id,
            delivery_date=delivery_date,
            status=status
        )

        # Add to data store
        delivery_id = self.delivery_store.add(delivery)

        # Update shipment with delivery info
        shipment.delivery_id = delivery_id
        shipment.status = status  # Update shipment status
        self.shipment_store.update(shipment_id, shipment)

        print(f"Delivery marked successfully with ID: {delivery_id}")

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
        self.shipment_menu = ShipmentMenu(self.shipment_store, self.customer_store, self.vehicle_store)
        self.delivery_menu = DeliveryMenu(self.delivery_store, self.shipment_store, self.customer_store)

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


if __name__ == "__main__":
    main()