class Vehicle:
    def __init__(self, make, model, year, color):
        # Constructor to initialize the vehicle's attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False  # Attribute to track whether the vehicle is running

    def start(self):
        # Method to start the vehicle
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model} has started.")
        else:
            print(f"The vehicle is already running.")

    def stop(self):
        # Method to stop the vehicle
        if self.is_running:
            self.is_running = False
            print(f"The {self.year} {self.make} {self.model} has stopped.")
        else:
            print(f"The vehicle is already stopped.")

    def drive(self):
        # Method to drive the vehicle
        if self.is_running:
            print(f"Driving the {self.year} {self.make} {self.model}.")
        else:
            print("You need to start the vehicle first.")

    def __str__(self):
        # String representation of the vehicle
        return f"{self.year} {self.make} {self.model} ({self.color})"

# Example usage:
vehicle1 = Vehicle("Toyota", "Corolla", 2020, "Red")
print(vehicle1)  # Output: 2020 Toyota Corolla (Red)

vehicle1.start()  # Output: The 2020 Toyota Corolla has started.
vehicle1.drive()  # Output: Driving the 2020 Toyota Corolla.
vehicle1.stop()   # Output: The 2020 Toyota Corolla has stopped.
