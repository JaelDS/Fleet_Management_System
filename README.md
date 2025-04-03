# Fleet Management System (FMS)

## Overview

The Fleet Management System (FMS) is a comprehensive software solution designed to streamline the management of vehicle fleets, shipments, and deliveries. This user-friendly application allows businesses to efficiently track vehicles, manage shipments, and monitor delivery statuses through an intuitive command-line interface.

```
    _______           _                   
   |  _____|         | |                  
   | |_     _ __ ___ | |     ___  ___ ___ 
   |  _|   | '_ ` _ \| |    / _ \/ __/ __| 
   | |     | | | | | | |___| (_) \__ \__ \
   |_|     |_| |_| |_|______\___/|___/___/
                                         
   Fleet Management System in Python
```

## Features

The system is organized into three main modules:

### 1. Fleet Management
- **Add Vehicle**: Register new vehicles with unique IDs, types, and capacities
- **Update Vehicle Information**: Modify existing vehicle details
- **Remove Vehicle**: Delete vehicles no longer in service (with safety checks to prevent removing vehicles assigned to active shipments)
- **View Fleet**: Display comprehensive information about all vehicles in the fleet

### 2. Shipment Management
- **Create a New Shipment**: Generate shipments with origin, destination, weight, and assigned vehicle
- **Track a Shipment**: Monitor the current status of any shipment using its unique ID
- **View All Shipments**: Get a complete overview of all shipments in the system

### 3. Delivery Management
- **Record Delivery**: Mark shipments as delivered with automatically generated timestamps
- **View Delivery Status**: Check detailed delivery information for any shipment

## Getting Started

### Prerequisites
- Python 3.6 or later

### Installation
1. Clone or download the repository to your local machine
2. Navigate to the project directory
3. Run the program using Python:
   ```
   python fms.py
   ```

## User Guide

### Navigation
The FMS uses a menu-driven interface. Navigate through the system by entering the option number or typing the option name.

### Vehicle Management

#### Adding a Vehicle
1. Select "Fleet Management" from the main menu
2. Choose "Add Vehicle"
3. Enter the vehicle details:
   - Vehicle ID (format: VXXXXXX, e.g., VTRUCK1)
   - Vehicle Type (e.g., Truck, Van, Car)
   - Load Capacity in kilograms

#### Updating Vehicle Information
1. Select "Fleet Management" from the main menu
2. Choose "Update Vehicle Information"
3. Enter the Vehicle ID to update
4. Provide new details (or press Enter to keep current values):
   - New Vehicle ID (optional)
   - New Vehicle Type (optional)
   - New Load Capacity (optional)

#### Viewing Fleet Information
1. Select "Fleet Management" from the main menu
2. Choose "View Fleet"
3. Review the tabular display of all vehicles with their details

### Shipment Management

#### Creating a Shipment
1. Select "Shipment Management" from the main menu
2. Choose "Create a New Shipment"
3. Enter shipment details:
   - Origin address (format: Street, City, State)
   - Destination address (format: Street, City, State)
   - Package weight in kilograms
   - Select a vehicle from the fleet

#### Tracking a Shipment
1. Select "Shipment Management" from the main menu
2. Choose "Track a Shipment"
3. Enter the Shipment ID (format: AXXXXXXXXXXXXXX)
4. View the current status, location, and estimated delivery information

### Delivery Management

#### Recording a Delivery
1. Select "Delivery Management" from the main menu
2. Choose "Record Delivery for a Shipment"
3. Enter the Shipment ID to mark as delivered
4. The system will generate a delivery timestamp and update the status

#### Checking Delivery Status
1. Select "Delivery Management" from the main menu
2. Choose "View Delivery Status for a Shipment"
3. Enter the Shipment ID to check
4. View comprehensive delivery information

## Technical Details

### Data Structures

The FMS uses several synchronized lists to store information:

#### Fleet Management
- `vehicles_list`: Stores unique vehicle IDs
- `vehicle_types`: Stores the type of each vehicle (parallel to vehicles_list)
- `vehicle_capacities`: Stores the capacity of each vehicle in kg (parallel to vehicles_list)
- `vehicle_availability`: Tracks whether each vehicle is available for assignment

#### Shipment Management
- `origins_list`: Stores shipment origin addresses
- `destinations_list`: Stores shipment destination addresses
- `weights_list`: Stores package weights
- `vehicles_selected`: Stores the vehicle assigned to each shipment
- `shipment_ids_list`: Stores unique shipment IDs

#### Delivery Management
- `delivery_status`: Tracks whether each shipment is "pending" or "delivered"
- `delivery_datetime`: Stores the delivery timestamp for each shipment

### ID Generation

- **Vehicle IDs**: Follow the format VXXXXXX (V followed by 6 alphanumeric characters)
- **Shipment IDs**: Generated using a deterministic algorithm that creates a unique 15-character ID starting with "A"

### Input Validation

The system includes comprehensive validation for all user inputs:
- Address validation ensures proper format (Street, City, State)
- Weight validation ensures numeric values
- Vehicle ID validation ensures proper format and uniqueness
- Shipment ID validation ensures proper format and existence

### Timestamp Generation

The system generates timestamps for shipments and deliveries using a deterministic algorithm based on the shipment ID, ensuring consistency without relying on external libraries.

## Limitations and Future Improvements

- **Database Integration**: Currently, data is stored in memory and lost when the program ends. Future versions will include database integration for persistent storage.
- **User Authentication**: A login system will be added to manage user access and permissions.
- **Graphical User Interface**: A GUI will be developed to enhance user experience.
- **Reporting Capabilities**: Advanced reporting features will be added to generate statistics and insights.
- **Real-time Tracking**: Integration with GPS systems for real-time vehicle and shipment tracking.

## Contributing

Contributions to the Fleet Management System are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under Torrens University Australia - see [Torrens University Australia](https://www.torrens.edu.au/) for more information.

<p align="center">
  <img src="img_python/love_torrens.jpg" height="60" alt="Torrens University"/>
</p>

## Acknowledgments

- Developed by Torrens students [José Antonio Escalante López. Michael Gomez Paucar and Abrar Quadri Shaik]
- All information is simulated and "randomly" created.
