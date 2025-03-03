import os

# Dataset: Membership details stored in a text file
FILENAME = "membership_data.txt"


def create_membership_file():
    """
    TODO: Create a sample membership data file.
    Each record includes: Name, Plan, Start Date, End Date, Payment Status.
    """
    data = """John, Gold, 2024-01-15, 2025-01-15, Paid
Alice, Silver, 2024-02-01, 2025-02-01, Unpaid
Bob, Platinum, 2024-03-10, 2025-03-10, Paid
Emma, Gold, 2024-04-20, 2025-04-20, Paid
Mike, Silver, 2024-05-05, 2025-05-05, Unpaid"""

    pass  # Replace with file-writing logic


def check_membership_status():
    """
    TODO: Read the file and check active members (those who have 'Paid' status).
    Store active members in a dictionary with details (Plan, End Date).
    Display the list of active members.
    """
    active_members = {}  # Dictionary to store active members

    pass  # Replace with file-reading logic


def count_members_by_plan():
    """
    TODO: Count how many members are in each plan (Gold, Silver, Platinum).
    Display the distribution of members across different membership plans.
    """
    plan_counts = {"Gold": 0, "Silver": 0, "Platinum": 0}

    pass  # Replace with logic to count members per plan

    return plan_counts


def main():
    """
    TODO: Execute all functions and display results.
    - Create membership file (if not exists)
    - Check and display active memberships
    - Count and display members by plan
    """
    pass  # Replace with function calls


if __name__ == "__main__":
    main()
