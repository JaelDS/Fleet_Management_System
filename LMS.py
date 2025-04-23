#!/usr/bin/env python3

"""
Logistics Management System Skeleton using OOP principles

This program provides a menu-based interface for managing a logistics operation,
including fleet, customers, shipments, and deliveries.
"""

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
    def __init__(self, vehicle_id=None, type=None, capacity=None, status=None):
        self.vehicle_id = vehicle_id
        self.type = type
        self.capacity = capacity
        self.status = status

    def display_info(self):
        """Display vehicle information."""
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Type: {self.type}")
        print(f"Capacity: {self.capacity}")
        print(f"Status: {self.status}")


class Customer:
    """Class representing a customer."""
    def __init__(self, customer_id=None, name=None, contact=None, address=None):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact
        self.address = address
        self.shipments = []  # List to store shipments associated with this customer

    def display_info(self):
        """Display customer information."""
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Address: {self.address}")

    def display_shipments(self):
        """Display all shipments associated with this customer."""
        if not self.shipments:
            print("No shipments found for this customer.")
            return

        print(f"Shipments for {self.name}:")
        for shipment in self.shipments:
            print(f"Shipment ID: {shipment.shipment_id}, Status: {shipment.status}")


class Shipment:
    """Class representing a shipment."""
    def __init__(self, shipment_id=None, customer=None, origin=None, destination=None,
                 contents=None, weight=None, vehicle=None):
        self.shipment_id = shipment_id
        self.customer = customer
        self.origin = origin
        self.destination = destination
        self.contents = contents
        self.weight = weight
        self.vehicle = vehicle
        self.status = "Pending"  # Initial status

    def display_info(self):
        """Display shipment information."""
        print(f"Shipment ID: {self.shipment_id}")
        print(f"Customer: {self.customer.name if self.customer else 'N/A'}")
        print(f"Origin: {self.origin}")
        print(f"Destination: {self.destination}")
        print(f"Contents: {self.contents}")
        print(f"Weight: {self.weight}")
        print(f"Vehicle ID: {self.vehicle.vehicle_id if self.vehicle else 'Not assigned'}")
        print(f"Status: {self.status}")


class Delivery:
    """Class representing a delivery."""
    def __init__(self, delivery_id=None, shipment=None, delivery_date=None, status=None):
        self.delivery_id = delivery_id
        self.shipment = shipment
        self.delivery_date = delivery_date
        self.status = status

    def display_info(self):
        """Display delivery information."""
        print(f"Delivery ID: {self.delivery_id}")
        print(f"Shipment ID: {self.shipment.shipment_id if self.shipment else 'N/A'}")
        print(f"Delivery Date: {self.delivery_date}")
        print(f"Status: {self.status}")


# Manager classes with menu inheritance
class FleetMenu(Menu):
    """Fleet Management Menu derived from base Menu

    This menu handles all operations related to vehicle management.
    It inherits basic menu functionality from the Menu class.
    """
    def __init__(self):
        super().__init__("Fleet Management")
        self.vehicles = []  # List to store vehicles

        # Add menu options
        self.add_option('1', 'Add a vehicle', self.add_vehicle)
        self.add_option('2', 'Update vehicle information', self.update_vehicle)
        self.add_option('3', 'Remove a vehicle', self.remove_vehicle)
        self.add_option('4', 'View all vehicles', self.view_vehicles)
        self.add_option('5', 'Quit fleet management', lambda: None)  # Just for display

    def add_vehicle(self):
        """Add a new vehicle to the fleet."""
        print("\n=== Add a New Vehicle ===")
        # Placeholder for vehicle addition logic
        print("Vehicle addition functionality will be implemented here.")

    def update_vehicle(self):
        """Update an existing vehicle's information."""
        print("\n=== Update Vehicle Information ===")
        # Placeholder for vehicle update logic
        print("Vehicle update functionality will be implemented here.")

    def remove_vehicle(self):
        """Remove a vehicle from the fleet."""
        print("\n=== Remove a Vehicle ===")
        # Placeholder for vehicle removal logic
        print("Vehicle removal functionality will be implemented here.")

    def view_vehicles(self):
        """Display all vehicles in the fleet."""
        print("\n=== All Vehicles ===")
        # Placeholder for displaying vehicles
        print("Vehicle display functionality will be implemented here.")


class CustomerMenu(Menu):
    """Customer Management Menu derived from base Menu"""
    def __init__(self):
        super().__init__("Customer Management")
        self.customers = []  # List to store customers

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
        # Placeholder for customer addition logic
        print("Customer addition functionality will be implemented here.")

    def update_customer(self):
        """Update an existing customer's information."""
        print("\n=== Update Customer Information ===")
        # Placeholder for customer update logic
        print("Customer update functionality will be implemented here.")

    def remove_customer(self):
        """Remove a customer."""
        print("\n=== Remove a Customer ===")
        # Placeholder for customer removal logic
        print("Customer removal functionality will be implemented here.")

    def view_customers(self):
        """Display all customers."""
        print("\n=== All Customers ===")
        # Placeholder for displaying customers
        print("Customer display functionality will be implemented here.")

    def view_customer_shipments(self):
        """View shipments for a specific customer."""
        print("\n=== View Customer's Shipments ===")
        # Placeholder for viewing customer shipments
        print("Customer shipments display functionality will be implemented here.")


class ShipmentMenu(Menu):
    """Shipment Management Menu derived from base Menu"""
    def __init__(self, customer_menu, fleet_menu):
        super().__init__("Shipment Management")
        self.shipments = []  # List to store shipments
        self.customer_menu = customer_menu  # Reference to customer menu
        self.fleet_menu = fleet_menu  # Reference to fleet menu

        # Add menu options
        self.add_option('1', 'Create a new shipment', self.create_shipment)
        self.add_option('2', 'Track a shipment', self.track_shipment)
        self.add_option('3', 'View all shipments', self.view_shipments)
        self.add_option('4', 'Quit shipment management', lambda: None)  # Just for display

    def create_shipment(self):
        """Create a new shipment."""
        print("\n=== Create a New Shipment ===")
        # Placeholder for shipment creation logic
        print("Shipment creation functionality will be implemented here.")

    def track_shipment(self):
        """Track a shipment's status."""
        print("\n=== Track a Shipment ===")
        # Placeholder for shipment tracking logic
        print("Shipment tracking functionality will be implemented here.")

    def view_shipments(self):
        """Display all shipments."""
        print("\n=== All Shipments ===")
        # Placeholder for displaying shipments
        print("Shipment display functionality will be implemented here.")


class DeliveryMenu(Menu):
    """Delivery Management Menu derived from base Menu"""
    def __init__(self, shipment_menu):
        super().__init__("Delivery Management")
        self.deliveries = []  # List to store deliveries
        self.shipment_menu = shipment_menu  # Reference to shipment menu

        # Add menu options
        self.add_option('1', 'Mark Shipment delivery', self.mark_delivery)
        self.add_option('2', 'View delivery status for a shipment', self.view_delivery_status)
        self.add_option('3', 'Quit delivery management', lambda: None)  # Just for display

    def mark_delivery(self):
        """Mark a shipment as delivered."""
        print("\n=== Mark Shipment Delivery ===")
        # Placeholder for marking delivery logic
        print("Delivery marking functionality will be implemented here.")

    def view_delivery_status(self):
        """View the delivery status of a shipment."""
        print("\n=== View Delivery Status ===")
        # Placeholder for viewing delivery status
        print("Delivery status display functionality will be implemented here.")


class MainMenu(Menu):
    """Main Menu class for the Logistics Management System

    This class represents the top-level menu of the system, from which users can
    access all the different management areas.
    """
    def __init__(self):
        super().__init__("Logistics Management System")

        # Initialize submenu instances
        self.fleet_menu = FleetMenu()
        self.customer_menu = CustomerMenu()
        self.shipment_menu = ShipmentMenu(self.customer_menu, self.fleet_menu)
        self.delivery_menu = DeliveryMenu(self.shipment_menu)

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