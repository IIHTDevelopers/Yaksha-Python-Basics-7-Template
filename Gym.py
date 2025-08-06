import pandas as pd

# ✅ Sample Dataset (Do Not Modify)
membership_data = pd.DataFrame({
    "Member ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Membership Type": ["Gold", "Silver", "Gold", "Bronze", "Silver"],
    "Monthly Fee": [1500, 1000, 1500, 800, 1000],
    "Months Active": [12, 8, 6, 3, 10]
})

#  Function 1: Calculate total contribution of a member
def calculate_total_contribution(df, member_id):
    """
    Return the total contribution made by a member using Monthly Fee × Months Active.

    Parameters:
        df (pd.DataFrame): Membership dataset.
        member_id (int): Member ID.

    Returns:
        int: Total contribution.
    """
    # TODO: Implement arithmetic logic to return total contribution
    pass

#  Function 2: Count members per membership type
def count_members_per_type(df):
    """
    Returns a dictionary with the count of members in each membership type using a loop.

    Parameters:
        df (pd.DataFrame): Membership dataset.

    Returns:
        dict: Count of members per membership type.
    """
    # TODO: Use loop to count each membership type
    pass

#  Function 3: Check if Alice is a long-term member
def is_alice_long_term(df):
    """
    Returns True if Alice has been active for more than 12 months.

    Parameters:
        df (pd.DataFrame): Membership dataset.

    Returns:
        bool: True if Alice > 12 months, else False.
    """
    # TODO: Implement conditional logic to check Alice's active months
    pass

#  Sample Execution
if __name__ == "__main__":
    print("Total Contribution by Member 101:", calculate_total_contribution(membership_data, 101))
    print("Count of Members Per Type:", count_members_per_type(membership_data))
    print("Is Alice a long-term member (>12 months)?", is_alice_long_term(membership_data))
