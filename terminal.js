// Terminal initialization
document.addEventListener('DOMContentLoaded', function() {
    const terminal = document.getElementById('terminal');
    if (!terminal) {
        console.error('Terminal element not found');
        return;
    }

    // Create terminal
    const term = new Terminal({
        cursorBlink: true,
        theme: {
            background: '#1e1e1e',
            foreground: '#f0f0f0'
        },
        rows: 24,
        cols: 80
    });

    // Load fit addon
    const fitAddon = new FitAddon.FitAddon();
    term.loadAddon(fitAddon);
    term.open(terminal);
    fitAddon.fit();

    // Static demo display - no Python execution
    runStaticDemo(term);
});

// Function to run a static demo of the Logistics Management System
function runStaticDemo(term) {
    let currentStep = 0;
    const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

    // Demo script - pre-defined sequence of steps with longer wait times
    const demoSteps = [
        { text: "Loading Logistics Management System...\r\n", wait: 1000 },
        { text: "Initializing modules...\r\n", wait: 1000 },
        { text: "System ready!\r\n\r\n", wait: 1000 },
        { text: "Welcome to the Logistics Management System - Demo\r\n", wait: 600 },
        { text: "This is a simplified version running in your browser.\r\n", wait: 600 },
        { text: "--------------------------------------------------\r\n\r\n", wait: 600 },

        // Unlike previous version, we now handle input differently
        // The prompt and the response are separate steps
        { text: "Please enter your name: ", wait: 800 },
        { text: "Guest\r\n", wait: 800, isInput: true }, // Mark this as input
        { text: "Hello, Guest! Welcome to the logistics system.\r\n\r\n", wait: 1000 },

        // Main menu first display
        { text: "===== Logistics Management System =====\r\n", wait: 400 },
        { text: "1. Fleet Management\r\n", wait: 200 },
        { text: "2. Customer Management\r\n", wait: 200 },
        { text: "3. Shipment Management\r\n", wait: 200 },
        { text: "4. Delivery Management\r\n", wait: 200 },
        { text: "0. Quit\r\n\r\n", wait: 200 },
        { text: "Select the menu to display (You can choose either the name or the number of the desired menu): ", wait: 800 },
        { text: "1\r\n", wait: 600, isInput: true },

        // Fleet Management
        { text: "===== Fleet Management =====\r\n", wait: 400 },
        { text: "1. Add a vehicle\r\n", wait: 200 },
        { text: "2. Update vehicle information\r\n", wait: 200 },
        { text: "3. Remove a vehicle\r\n", wait: 200 },
        { text: "4. View all vehicles\r\n", wait: 200 },
        { text: "5. Quit fleet management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "1\r\n", wait: 600, isInput: true },

        // Add a vehicle
        { text: "=== Add a New Vehicle ===\r\n\r\n", wait: 400 },
        { text: "Enter vehicle type: ", wait: 800 },
        { text: "Truck\r\n", wait: 600, isInput: true },
        { text: "Enter vehicle capacity: ", wait: 800 },
        { text: "2500\r\n", wait: 600, isInput: true },
        { text: "Vehicle added successfully with ID: V8J42K7L\r\n", wait: 1000 },

        // Back to Fleet Management
        { text: "\r\n===== Fleet Management =====\r\n", wait: 400 },
        { text: "1. Add a vehicle\r\n", wait: 200 },
        { text: "2. Update vehicle information\r\n", wait: 200 },
        { text: "3. Remove a vehicle\r\n", wait: 200 },
        { text: "4. View all vehicles\r\n", wait: 200 },
        { text: "5. Quit fleet management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "4\r\n", wait: 600, isInput: true },

        // View vehicles
        { text: "=== All Vehicles ===\r\n\r\n", wait: 400 },
        { text: "Vehicle ID: V8J42K7L\r\n", wait: 200 },
        { text: "Type: Truck\r\n", wait: 200 },
        { text: "Capacity: 2500\r\n", wait: 200 },
        { text: "Status: Available\r\n", wait: 200 },
        { text: "Date: 2025-05-17 14:30:22\r\n", wait: 200 },
        { text: "------------------------------\r\n", wait: 600 },

        // Back to Fleet Management
        { text: "\r\n===== Fleet Management =====\r\n", wait: 400 },
        { text: "1. Add a vehicle\r\n", wait: 200 },
        { text: "2. Update vehicle information\r\n", wait: 200 },
        { text: "3. Remove a vehicle\r\n", wait: 200 },
        { text: "4. View all vehicles\r\n", wait: 200 },
        { text: "5. Quit fleet management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "5\r\n", wait: 200, isInput: true },
        { text: "Exiting Fleet Management...\r\n\r\n", wait: 800 },

        // Main menu again
        { text: "===== Logistics Management System =====\r\n", wait: 400 },
        { text: "1. Fleet Management\r\n", wait: 200 },
        { text: "2. Customer Management\r\n", wait: 200 },
        { text: "3. Shipment Management\r\n", wait: 200 },
        { text: "4. Delivery Management\r\n", wait: 200 },
        { text: "0. Quit\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "2\r\n", wait: 600, isInput: true },

        // Customer Management
        { text: "===== Customer Management =====\r\n", wait: 400 },
        { text: "1. Add a customer\r\n", wait: 200 },
        { text: "2. Update customer information\r\n", wait: 200 },
        { text: "3. Remove a customer\r\n", wait: 200 },
        { text: "4. View all customers\r\n", wait: 200 },
        { text: "5. View a customer's shipments\r\n", wait: 200 },
        { text: "6. Quit customer management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "1\r\n", wait: 600, isInput: true },

        // Add a customer
        { text: "=== Add a New Customer ===\r\n\r\n", wait: 400 },
        { text: "Enter customer name (first and last name): ", wait: 800 },
        { text: "John Smith\r\n", wait: 600, isInput: true },
        { text: "Enter birthday (dd-mm-yyyy): ", wait: 800 },
        { text: "15-06-1985\r\n", wait: 600, isInput: true },
        { text: "Enter Australian address: ", wait: 800 },
        { text: "123 Smith Street, Surry Hills NSW 2000\r\n", wait: 800, isInput: true },
        { text: "Enter email address: ", wait: 800 },
        { text: "john.smith@example.com\r\n", wait: 600, isInput: true },
        { text: "Enter Australian phone number: ", wait: 800 },
        { text: "0412 345 678\r\n", wait: 600, isInput: true },
        { text: "Customer added successfully with ID: C5RK39P\r\n", wait: 1000 },

        // Back to Customer Management
        { text: "\r\n===== Customer Management =====\r\n", wait: 400 },
        { text: "1. Add a customer\r\n", wait: 200 },
        { text: "2. Update customer information\r\n", wait: 200 },
        { text: "3. Remove a customer\r\n", wait: 200 },
        { text: "4. View all customers\r\n", wait: 200 },
        { text: "5. View a customer's shipments\r\n", wait: 200 },
        { text: "6. Quit customer management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "4\r\n", wait: 600, isInput: true },

        // View customers
        { text: "=== All Customers ===\r\n\r\n", wait: 400 },
        { text: "Customer ID: C5RK39P\r\n", wait: 200 },
        { text: "Name: John Smith\r\n", wait: 200 },
        { text: "Birthday: 15-06-1985\r\n", wait: 200 },
        { text: "Address: 123 Smith Street, Surry Hills NSW 2000\r\n", wait: 200 },
        { text: "Email: john.smith@example.com\r\n", wait: 200 },
        { text: "Phone: 0412 345 678\r\n", wait: 200 },
        { text: "Number of shipments: 0\r\n", wait: 200 },
        { text: "------------------------------\r\n", wait: 600 },

        // Back to Customer Management
        { text: "\r\n===== Customer Management =====\r\n", wait: 400 },
        { text: "1. Add a customer\r\n", wait: 200 },
        { text: "2. Update customer information\r\n", wait: 200 },
        { text: "3. Remove a customer\r\n", wait: 200 },
        { text: "4. View all customers\r\n", wait: 200 },
        { text: "5. View a customer's shipments\r\n", wait: 200 },
        { text: "6. Quit customer management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "6\r\n", wait: 200, isInput: true },
        { text: "Exiting Customer Management...\r\n\r\n", wait: 800 },

        // Main menu - Shipment Management
        { text: "===== Logistics Management System =====\r\n", wait: 400 },
        { text: "1. Fleet Management\r\n", wait: 200 },
        { text: "2. Customer Management\r\n", wait: 200 },
        { text: "3. Shipment Management\r\n", wait: 200 },
        { text: "4. Delivery Management\r\n", wait: 200 },
        { text: "0. Quit\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "3\r\n", wait: 600, isInput: true },

        // Shipment Management
        { text: "===== Shipment Management =====\r\n", wait: 400 },
        { text: "1. Create a new shipment\r\n", wait: 200 },
        { text: "2. Track a shipment\r\n", wait: 200 },
        { text: "3. View all shipments\r\n", wait: 200 },
        { text: "4. Quit shipment management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "1\r\n", wait: 600, isInput: true },

        // Create a shipment
        { text: "=== Create a New Shipment ===\r\n\r\n", wait: 400 },
        { text: "Enter customer ID: ", wait: 800 },
        { text: "C5RK39P\r\n", wait: 600, isInput: true },
        { text: "Enter origin: ", wait: 800 },
        { text: "Sydney, NSW\r\n", wait: 600, isInput: true },
        { text: "Enter destination: ", wait: 800 },
        { text: "Melbourne, VIC\r\n", wait: 600, isInput: true },
        { text: "Enter weight: ", wait: 800 },
        { text: "150\r\n", wait: 600, isInput: true },
        { text: "Enter vehicle ID (or press Enter to assign later): ", wait: 800 },
        { text: "V8J42K7L\r\n", wait: 600, isInput: true },
        { text: "Shipment created successfully with ID: S2TH78B\r\n", wait: 1000 },

        // Back to Shipment Management
        { text: "\r\n===== Shipment Management =====\r\n", wait: 400 },
        { text: "1. Create a new shipment\r\n", wait: 200 },
        { text: "2. Track a shipment\r\n", wait: 200 },
        { text: "3. View all shipments\r\n", wait: 200 },
        { text: "4. Quit shipment management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "2\r\n", wait: 600, isInput: true },

        // Track shipment
        { text: "=== Track a Shipment ===\r\n\r\n", wait: 400 },
        { text: "Enter shipment ID: ", wait: 800 },
        { text: "S2TH78B\r\n", wait: 600, isInput: true },
        { text: "\r\n========== Shipment Tracking ==========\r\n", wait: 300 },
        { text: "ID: S2TH78B\r\n", wait: 200 },
        { text: "Customer: John Smith\r\n", wait: 200 },
        { text: "Route: Sydney, NSW → Melbourne, VIC\r\n", wait: 200 },
        { text: "Weight: 150 kg\r\n", wait: 200 },
        { text: "Vehicle: Truck\r\n", wait: 200 },
        { text: "\r\nStatus: Your shipment is in transit\r\n", wait: 200 },
        { text: "Estimated Delivery: 2025-05-19\r\n", wait: 800 },
        { text: "\r\nPress Enter to continue...", wait: 800 },
        { text: "\r\n", wait: 600, isInput: true },

        // Back to Shipment Management
        { text: "\r\n===== Shipment Management =====\r\n", wait: 400 },
        { text: "1. Create a new shipment\r\n", wait: 200 },
        { text: "2. Track a shipment\r\n", wait: 200 },
        { text: "3. View all shipments\r\n", wait: 200 },
        { text: "4. Quit shipment management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "4\r\n", wait: 200, isInput: true },
        { text: "Exiting Shipment Management...\r\n\r\n", wait: 800 },

        // Main menu - Delivery Management
        { text: "===== Logistics Management System =====\r\n", wait: 400 },
        { text: "1. Fleet Management\r\n", wait: 200 },
        { text: "2. Customer Management\r\n", wait: 200 },
        { text: "3. Shipment Management\r\n", wait: 200 },
        { text: "4. Delivery Management\r\n", wait: 200 },
        { text: "0. Quit\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "4\r\n", wait: 600, isInput: true },

        // Delivery Management
        { text: "===== Delivery Management =====\r\n", wait: 400 },
        { text: "1. Mark Shipment delivery\r\n", wait: 200 },
        { text: "2. View delivery status for a shipment\r\n", wait: 200 },
        { text: "3. Quit delivery management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "1\r\n", wait: 600, isInput: true },

        // Mark delivery
        { text: "=== Mark Shipment Delivery ===\r\n\r\n", wait: 400 },
        { text: "Enter shipment ID to mark as delivered (or 'q' to quit): ", wait: 800 },
        { text: "S2TH78B\r\n", wait: 600, isInput: true },
        { text: "\r\n✓ DELIVERY CONFIRMATION\r\n", wait: 300 },
        { text: "==============================\r\n", wait: 200 },
        { text: "Shipment ID: S2TH78B\r\n", wait: 200 },
        { text: "Date: 17/05/2025 15:45\r\n", wait: 200 },
        { text: "Status: DELIVERED\r\n", wait: 200 },
        { text: "Customer: John Smith\r\n", wait: 200 },
        { text: "Address: Melbourne, VIC\r\n", wait: 200 },
        { text: "==============================\r\n", wait: 200 },
        { text: "Delivery recorded successfully!\r\n\r\n", wait: 800 },
        { text: "Mark another delivery? (y/n): ", wait: 800 },
        { text: "n\r\n", wait: 600, isInput: true },

        // Back to Delivery Management
        { text: "\r\n===== Delivery Management =====\r\n", wait: 400 },
        { text: "1. Mark Shipment delivery\r\n", wait: 200 },
        { text: "2. View delivery status for a shipment\r\n", wait: 200 },
        { text: "3. Quit delivery management\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "3\r\n", wait: 200, isInput: true },
        { text: "Exiting Delivery Management...\r\n\r\n", wait: 800 },

        // Main menu - Quit
        { text: "===== Logistics Management System =====\r\n", wait: 400 },
        { text: "1. Fleet Management\r\n", wait: 200 },
        { text: "2. Customer Management\r\n", wait: 200 },
        { text: "3. Shipment Management\r\n", wait: 200 },
        { text: "4. Delivery Management\r\n", wait: 200 },
        { text: "0. Quit\r\n\r\n", wait: 200 },
        { text: "Select the menu to display: ", wait: 800 },
        { text: "0\r\n", wait: 600, isInput: true },

        // Exit
        { text: "Thank you for using the Logistics Management System. Goodbye!\r\n\r\n", wait: 600 },
        { text: "╔═════════════════════════════════════════════╗\r\n", wait: 300 },
        { text: "║    Code crafted with ♥ by Jael & Patrick    ║\r\n", wait: 300 },
        { text: "╚═════════════════════════════════════════════╝\r\n\r\n", wait: 600 },
        { text: "Demo completed. Refresh the page to restart.\r\n", wait: 0 }
    ];

    // Process each step in sequence
    async function processNextStep() {
        if (currentStep >= demoSteps.length) {
            return; // Demo complete
        }

        const step = demoSteps[currentStep];

        // If this is an input step, handle typing effect
        if (step.isInput) {
            await simulateTyping(step.text);
        } else {
            // Just write the text directly
            term.write(step.text);
        }

        // Wait specified time
        await delay(step.wait);

        // Process next step
        currentStep++;
        processNextStep();
    }

    // Function to simulate typing input
    async function simulateTyping(text) {
        // Remove the trailing \r\n for typing simulation
        const inputText = text.replace(/\r\n$/, '');

        // Type each character with variable speed
        for (let i = 0; i < inputText.length; i++) {
            term.write(inputText[i]);
            // Random typing delay between 80ms and 230ms
            await delay(Math.random() * 150 + 80);
        }

        // Add the carriage return and newline at the end
        term.write('\r\n');
    }

    // Start the demo
    processNextStep();
}