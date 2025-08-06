import pandas as pd

# ✅ Sample Event Dataset (Do Not Modify)
event_data = pd.DataFrame({
    "Event ID": [201, 202, 203, 204, 205],
    "Event Name": ["Tech Summit", "Music Fest", "Job Fair", "Food Carnival", "Book Launch"],
    "Location": ["New York", "Los Angeles", "Chicago", "New York", "Boston"],
    "Registered People": [120, 200, 75, 180, 50],
    "Entry Fee": [50, 30, 0, 20, 10]
})

# ✅ Function 1 - Total number of people
def get_total_people_registered(df):
    """
    Returns the total number of registered people for all events.

    Parameters:
        df (pd.DataFrame): Event dataset.

    Returns:
        int: Total number of people registered.
    """
    # TODO: Sum 'Registered People' column
    pass

# ✅ Function 2 - Number of events with Entry Fee > 10
def count_events_with_high_fees(df):
    """
    Returns the number of events where the entry fee is greater than 10.

    Parameters:
        df (pd.DataFrame): Event dataset.

    Returns:
        int: Count of events with entry fee > 10.
    """
    # TODO: Filter and count events with 'Entry Fee' > 10
    pass

# ✅ Function 3 - Count events in New York
def count_events_in_newyork(df):
    """
    Returns the number of events that are happening in New York.

    Parameters:
        df (pd.DataFrame): Event dataset.

    Returns:
        int: Count of events happening in New York.
    """
    # TODO: Filter DataFrame where Location == 'New York'
    pass

# ✅ Sample Execution Block
if __name__ == "__main__":
    print("Total Registered People:", get_total_people_registered(event_data))
    print("Events with Entry Fee > 10:", count_events_with_high_fees(event_data))
    print("Events in New York:", count_events_in_newyork(event_data))
