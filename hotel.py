import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# TODO: Implement function to get the price of the room with a Jacuzzi
def jacuzzi_room_price():
    pass

# TODO: Implement function to find the most expensive room
def most_expensive_room():
    pass

# Helper function: Returns room data
def get_room_data():
    return {
        "R101": {"type": "Standard", "price": 100.00, "capacity": 2, "amenities": ["TV", "WiFi"]},
        "R102": {"type": "Deluxe", "price": 150.00, "capacity": 2, "amenities": ["TV", "WiFi", "Mini Bar"]},
        "R103": {"type": "Suite", "price": 250.00, "capacity": 4, "amenities": ["TV", "WiFi", "Mini Bar", "Jacuzzi"]},
        "R104": {"type": "Standard", "price": 100.00, "capacity": 2, "amenities": ["TV", "WiFi"]},
        "R105": {"type": "Deluxe", "price": 150.00, "capacity": 2, "amenities": ["TV", "WiFi", "Mini Bar"]}
    }

# Helper function: Returns booking data
def get_booking_data():
    today = datetime.now()
    return [
        {"booking_id": "B001", "room_id": "R102", "guest_name": "John Smith", "check_in": today - timedelta(days=2), "check_out": today + timedelta(days=3), "guests": 2},
        {"booking_id": "B002", "room_id": "R105", "guest_name": "Alice Johnson", "check_in": today + timedelta(days=5), "check_out": today + timedelta(days=10), "guests": 2},
        {"booking_id": "B003", "room_id": "R103", "guest_name": "Bob Williams", "check_in": today + timedelta(days=15), "check_out": today + timedelta(days=20), "guests": 3},
        {"booking_id": "B004", "room_id": "R101", "guest_name": "Emma Davis", "check_in": today + timedelta(days=7), "check_out": today + timedelta(days=9), "guests": 1},
        {"booking_id": "B005", "room_id": "R104", "guest_name": "Michael Brown", "check_in": today + timedelta(days=12), "check_out": today + timedelta(days=14), "guests": 2}
    ]

# Main Execution
def main():
    # TODO: Call functions to execute the program
    pass

if __name__ == "__main__":
    main()
