# Fleet Management System (FMS) - Evolution to Logistics Management System (LMS)

## Overview

The Logistics Management System (LMS) represents a significant evolution from the original Fleet Management System (FMS). This document outlines the transformation from a basic procedural program to a sophisticated object-oriented application that provides enhanced functionality, better data management, and improved user experience.

```
 _      __  __  ____  
| |    |  \/  |/ ___| 
| |    | |\/| | \___ \
| |___ | |  | |  ___) |
|_____||_|  |_||____/ 
                      
Logistics Management System in Python
```
  
   Logistics Management System in Python

## Evolution from FMS to LMS: Key Transformations

### 1. Programming Paradigm Shift

#### **Before (FMS - main_assessment.py)**
- **Procedural Programming**: The original system used a linear, function-based approach
- **Global Lists**: Data was stored in global lists (vehicles_list, shipment_ids_list, etc.)
- **Limited Structure**: Functions operated directly on global data

```python
# Example from FMS
vehicles_list = ["VTRUCK1", "VCAR123", "V2TRUCK"]
vehicle_types = ["Truck", "Car", "Truck"]
vehicle_capacities = ["5000", "500", "3500"]
```

#### **After (LMS - LMS.py)**
- **Object-Oriented Programming (OOP)**: Complete redesign using classes and objects
- **Encapsulation**: Data is encapsulated within objects with dedicated methods
- **Enhanced Organization**: Clear separation of concerns with class hierarchies

```python
# Example from LMS
class Vehicle:
    def __init__(self, vehicle_id=None, type=None, capacity=None, status="Available"):
        self.id = vehicle_id
        self.type = type
        self.capacity = capacity
        self.status = status
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

### 2. Data Management Revolution

#### **Before (FMS)**
- **Parallel Lists**: Related data stored in separate lists
- **Index-based Relationships**: Data connected by matching indices
- **Limited Data Integrity**: Prone to synchronization errors

#### **After (LMS)**
- **Centralized DataStore**: Professional data management system
- **Dictionary-based Storage**: Fast lookups and reliable data access
- **Automatic ID Generation**: Unique identifiers generated automatically

```python
class DataStore:
    def __init__(self):
        self.data = {}  # Dictionary for efficient storage
        
    def add(self, item):
        # Automatic ID generation based on object type
        if isinstance(item, Vehicle):
            prefix = "V"
        elif isinstance(item, Customer):
            prefix = "C"
        # ... more type checks
        
        item_id = f"{prefix}{random_part}"
        self.data[item_id] = item
        return item_id
```

### 3. User Experience Enhancements

#### **Before (FMS)**
- **Basic Text Interface**: Simple menu with numbered options
- **Limited Error Handling**: Basic validation with minimal feedback
- **No Visual Appeal**: Plain text output

#### **After (LMS)**
- **Professional Interface**: Color-coded menus using Colorama
- **Comprehensive Validation**: Detailed error messages and recovery options
- **Enhanced Visuals**: Formatted output with colors and borders

```python
# LMS includes beautiful output formatting
def display_signature():
    border = Fore.CYAN
    code = Fore.MAGENTA
    # ... more color definitions
    
    print(f"{border}╔{'═' * (content_length + 2)}╗{reset}")
    print(f"{side_border} {content} {side_border}")
    print(f"{border}╚{'═' * (content_length + 2)}╝{reset}")
```

### 4. Customer Management System (New in LMS)

#### **Added Features**
- **Complete Customer Profiles**: Name, birthday, address, email, phone
- **Australian Address Validation**: Specific format for Australian addresses
- **Age Verification**: Ensures customers are 18 or older
- **Email and Phone Validation**: Professional contact information verification

```python
# Advanced validation example
address_pattern = r"""
    ^
    (?:(?:Unit|Apt|Apartment|Flat)\s*\d+[a-zA-Z]?[/\-\s]+)?  # Optional unit
    \d+[a-zA-Z]?(?:\s*-\s*\d+[a-zA-Z]?)?                     # Street number
    \s+
    (?:[A-Za-z][A-Za-z']+(?:\s+[A-Za-z][A-Za-z']+)*)         # Street name
    \s+
    (?:Street|St|Road|Rd|Avenue|Ave|...)                      # Street type
    \s*,?\s*
    [A-Za-z][A-Za-z\s'-]+                                    # Suburb
    \s+
    (?:NSW|VIC|QLD|SA|WA|TAS|NT|ACT)                        # State
    \s+
    \d{4}                                                    # Postcode
    $
"""
```

### 5. Advanced Shipment Management

#### **Before (FMS)**
- **Basic Tracking**: Simple status generation
- **Limited Information**: Minimal shipment details
- **No Delivery Prediction**: No estimated delivery dates

#### **After (LMS)**
- **Smart Tracking**: Status based on multiple factors
- **Delivery Predictions**: Simulated delivery dates based on weight, vehicle, and distance
- **Customer Integration**: Links shipments to customer profiles
- **Vehicle Capacity Check**: Only shows vehicles that can handle shipment weight

```python
def calculate_simulated_delivery_date(self, shipment):
    # Intelligent delivery date calculation
    transit_days = 2  # Base transit time
    
    # Factor 1: Weight impact
    if shipment.weight > 100:
        transit_days += 2
        
    # Factor 2: Vehicle type impact
    vehicle_delays = {
        'Motorcycle': -1,  # Faster
        'Van': 0,
        'Truck': 1,
        'Cargo Ship': 5,
        'Airplane': -2  # Fastest
    }
    # ... more calculations
```

### 6. Professional Fleet Management

#### **Improvements**
- **Vehicle Status Tracking**: Available, On Delivery, Maintenance
- **Capacity Management**: Validates vehicle can carry shipment weight
- **Enhanced Validation**: Stricter input validation for vehicle data
- **Date Tracking**: Records when vehicles are added to the system

### 7. Modern Delivery System

#### **New Features**
- **Automatic Timestamps**: Records exact delivery time
- **Status Updates**: Real-time delivery status tracking
- **Delivery Confirmation**: Professional delivery confirmation screen
- **Integrated Tracking**: Links with shipment and customer data

### 8. Technical Architecture Improvements

#### **Code Structure**
- **Modular Design**: Each component is self-contained
- **Inheritance**: Menu classes inherit from base Menu class
- **Code Reusability**: Common functions shared across modules
- **Error Recovery**: Better error handling and recovery options

```python
class Menu:
    """Base Menu class that all submenus inherit from"""
    def __init__(self, title):
        self.title = title
        self.options = []
        
    def execute(self):
        """Execute the menu and handle user input"""
        # Standardized menu execution logic
```

## Benefits for Non-Technical Users

### 1. **Easier to Use**
- Color-coded menus make navigation intuitive
- Better error messages guide users to correct inputs
- Professional formatting improves readability

### 2. **More Reliable**
- Data is stored more securely
- Automatic ID generation prevents duplicates
- Better validation reduces errors

### 3. **More Features**
- Complete customer management
- Smart delivery predictions
- Professional tracking system
- Enhanced reporting capabilities

### 4. **Future-Ready**
- Object-oriented design allows easy expansion
- Can easily add database support
- Ready for web interface integration
- Scalable to handle more data

## Getting Started

### Prerequisites
- Python 3.6 or later
- colorama library (for colored output)

### Installation
1. Clone or download the repository to your local machine
2. Install required dependencies:
   ```
   pip install colorama
   ```
3. Navigate to the project directory
4. Run the program using Python:
   ```
   python LMS.py
   ```

## Features Overview

### Customer Management (New in LMS)
- **Add Customer**: Register new customers with complete profiles
- **Update Customer Information**: Modify existing customer details
- **Remove Customer**: Delete customer records (with safety checks)
- **View All Customers**: Display comprehensive customer information
- **View Customer Shipments**: See all shipments for a specific customer

### Fleet Management (Enhanced)
- **Add Vehicle**: Register vehicles with enhanced validation
- **Update Vehicle Information**: Modify vehicle details with better controls
- **Remove Vehicle**: Delete vehicles with shipment safety checks
- **View Fleet**: Display fleet information with improved formatting

### Shipment Management (Enhanced)
- **Create New Shipment**: Generate shipments with customer integration
- **Track Shipment**: Enhanced tracking with delivery predictions
- **View All Shipments**: Comprehensive shipment overview with status

### Delivery Management (Enhanced)
- **Record Delivery**: Mark shipments as delivered with automatic timestamps
- **View Delivery Status**: Check detailed delivery information

## Technical Comparison Table

| Feature | FMS (Original) | LMS (Enhanced) |
|---------|----------------|----------------|
| Programming Paradigm | Procedural | Object-Oriented |
| Data Storage | Global Lists | DataStore with Dictionaries |
| ID Generation | Manual Input | Automatic Random IDs |
| Customer Management | None | Full Customer Profiles |
| Validation | Basic | Comprehensive Regex Patterns |
| User Interface | Plain Text | Color-coded with Formatting |
| Error Handling | Basic | Advanced with Recovery |
| Delivery Prediction | None | Smart Algorithm |
| Code Structure | Linear Functions | Modular Classes |
| Extensibility | Limited | Highly Extensible |

## Conclusion

The evolution from FMS to LMS represents a complete transformation from a basic procedural program to a professional, object-oriented logistics management system. The new system is more reliable, user-friendly, and feature-rich, providing a solid foundation for future enhancements and business growth.

The LMS demonstrates best practices in software development, including:
- Object-oriented design principles
- Professional data management
- Enhanced user experience
- Comprehensive input validation
- Modular, maintainable code structure

This transformation makes the system not just more powerful, but also more accessible to users of all technical levels while maintaining the flexibility needed for future growth.

## License

This project is licensed under Torrens University Australia - see [Torrens University Australia](https://www.torrens.edu.au/) for more information.

<p align="center">
  <img src="img_python/love_torrens.jpg" height="60" alt="Torrens University"/>
</p>

## Acknowledgments

- Original FMS developed by Torrens students [José Antonio Escalante López, Michael Gomez Paucar, and Abrar Quadri Shaik]
- Enhanced LMS developed by Jose Antonio Escalante Lopez and Michael Gomez Paucar with object-oriented principles and professional software engineering practices
- All information is simulated for educational purposes

---

<!-- README.md -->
# Logistic Management System

<!-- For GitHub's dark mode -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=00FF41&center=true&vCenter=true&width=650&lines=Code+crafted+by+@JaelDS+%26+@PatrickGP23;Creating+practical+solutions;Since+2025">
  <img alt="Typing SVG" src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=2F9C5A&center=true&vCenter=true&width=650&lines=Code+crafted+by+@JaelDS+%26+@PatrickGP23;Creating+practical+solutions;Since+2025">
</picture>

<div align="center">
  
  <!-- All badges standardized to flat-square style -->
  <img src="https://img.shields.io/badge/Made%20with-🖤-lightgrey?style=flat-square&logo=github" alt="Made with Love" />
  <img src="https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python" alt="Made with Python" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" alt="Status Active" />
  
</div>
