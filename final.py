import tkinter as tk
from tkinter import messagebox
import pickle

class EventManagementGUI:
    def __init__(self, root):
        # Initialize the GUI window
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("400x400")  # Set window size

        # Label for company name
        company_label = tk.Label(root, text="The Best Events Company", font=("Arial", 14, "bold"))
        company_label.pack(pady=10)

        # Load existing data or initialize empty data dictionary
        self.load_data()

        # Main Menu Buttons for managing different entities
        self.manage_employees_button = tk.Button(root, text="Manage Employees", command=self.manage_employees)
        self.manage_employees_button.pack(pady=10)  # 4.a. Add/Delete/Modify/Display details of employees

        self.manage_events_button = tk.Button(root, text="Manage Events", command=self.manage_events)
        self.manage_events_button.pack(pady=10)  # 4.a. Add/Delete/Modify/Display details of events

        self.manage_clients_button = tk.Button(root, text="Manage Clients", command=self.manage_clients)
        self.manage_clients_button.pack(pady=10)  # 4.a. Add/Delete/Modify/Display details of clients

        self.manage_guests_button = tk.Button(root, text="Manage Guests", command=self.manage_guests)
        self.manage_guests_button.pack(pady=10)  # 4.a. Add/Delete/Modify/Display details of guests

        self.manage_suppliers_button = tk.Button(root, text="Manage Suppliers", command=self.manage_suppliers)
        self.manage_suppliers_button.pack(pady=10)  # 4.a. Add/Delete/Modify/Display details of suppliers

        self.manage_venues_button = tk.Button(root, text="Manage Venues", command=self.manage_venues)
        self.manage_venues_button.pack(pady=10)  # 4.a. Add/Delete/Modify/Display details of venues

        # View All Data Button to display all entries for all entities
        self.view_all_data_button = tk.Button(root, text="View All Data", command=self.view_all_data)
        self.view_all_data_button.pack(pady=10)  # 4.a. Display all details of employees, events, clients, guests, and suppliers

    def load_data(self):
        # Load existing data from file if available, otherwise initialize empty data dictionary
        try:
            with open("data.pkl", "rb") as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            self.data = {"employees": {}, "events": {}, "clients": {}, "guests": {}, "suppliers": {}, "venues": {}}

    def save_data(self):
        # Save data dictionary to file
        with open("data.pkl", "wb") as f:
            pickle.dump(self.data, f)

    # Methods for managing different entities
    def manage_employees(self):
        self.manage_entity_window("Employees", "Employee")

    def manage_events(self):
        self.manage_entity_window("Events", "Event")

    def manage_clients(self):
        self.manage_entity_window("Clients", "Client")

    def manage_guests(self):
        self.manage_entity_window("Guests", "Guest")

    def manage_suppliers(self):
        self.manage_entity_window("Suppliers", "Supplier")

    def manage_venues(self):
        self.manage_entity_window("Venues", "Venue")

    def manage_entity_window(self, title, entity):
        # Create a new window to manage the selected entity
        self.entity_window = tk.Toplevel(self.root)
        self.entity_window.title(f"Manage {title}")

        # Entry fields for entity ID and name
        tk.Label(self.entity_window, text=f"{entity} ID:").grid(row=0, column=0)
        self.entity_id_entry = tk.Entry(self.entity_window)
        self.entity_id_entry.grid(row=0, column=1)

        tk.Label(self.entity_window, text="Name:").grid(row=1, column=0)
        self.name_entry = tk.Entry(self.entity_window)
        self.name_entry.grid(row=1, column=1)

        # Buttons for adding, displaying, modifying, and deleting entity
        tk.Button(self.entity_window, text=f"Add {entity}", command=lambda: self.add_entity(entity)).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.entity_window, text=f"Display All {entity}s", command=lambda: self.display_entity(entity)).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.entity_window, text=f"Modify {entity}", command=lambda: self.modify_entity(entity)).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.entity_window, text=f"Delete {entity}", command=lambda: self.delete_entity(entity)).grid(row=5, column=0, columnspan=2, pady=10)

    def add_entity(self, entity):
        # Method to add a new entity
        entity_id = self.entity_id_entry.get()
        name = self.name_entry.get()

        if entity_id and name:
            if entity_id not in self.data[entity.lower() + 's']:
                self.data[entity.lower() + 's'][entity_id] = {"Name": name}
                messagebox.showinfo("Success", f"{entity} added successfully.")
                self.save_data()
            else:
                messagebox.showerror("Error", f"{entity} ID already exists.")
        else:
            messagebox.showerror("Error", f"Please enter {entity} ID and name.")

    def display_entity(self, entity):
        # Method to display all details of a specific entity
        details = ""
        for key, value in self.data[entity.lower() + 's'].items():
            details += f"{entity} ID: {key}\n"
            for attribute, attribute_value in value.items():
                details += f"{attribute}: {attribute_value}\n"
            details += "\n"
        messagebox.showinfo(f"All {entity} Details", details)

    def modify_entity(self, entity):
        # Method to modify details of a specific entity
        entity_id = self.entity_id_entry.get()

        if entity_id in self.data[entity.lower() + 's']:
            new_name = self.name_entry.get()

            self.data[entity.lower() + 's'][entity_id]["Name"] = new_name

            messagebox.showinfo("Success", f"{entity} details updated successfully.")
            self.save_data()
        else:
            messagebox.showerror("Error", f"{entity} not found.")

    def delete_entity(self, entity):
        # Method to delete a specific entity
        entity_id = self.entity_id_entry.get()

        if entity_id in self.data[entity.lower() + 's']:
            del self.data[entity.lower() + 's'][entity_id]
            messagebox.showinfo("Success", f"{entity} deleted successfully.")
            self.save_data()
        else:
            messagebox.showerror("Error", f"{entity} not found.")

    def view_all_data(self):
        # Method to display all data for all entities
        details = ""
        for entity, data_dict in self.data.items():
            details += f"{entity.capitalize()}:\n\n"
            for key, value in data_dict.items():
                details += f"{entity} ID: {key}\n"
                for attribute, attribute_value in value.items():
                    details += f"{attribute}: {attribute_value}\n"
                details += "\n"
            details += "\n"
        messagebox.showinfo("All Data", details)

# Main function to create and run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementGUI(root)
    root.mainloop()