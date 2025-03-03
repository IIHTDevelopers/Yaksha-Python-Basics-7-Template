# PythonBasics/test/test_functional.py

import unittest
import sys
import os
from datetime import datetime, timedelta

# Adjusting the path to import TestUtils and the required modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from hotel import (
    jacuzzi_room_price,
    most_expensive_room,
    get_room_data,
    get_booking_data
)
from Gym import (
    create_membership_file,
    check_membership_status,
    count_members_by_plan
)
from Event import (
    display_upcoming_events,
    count_total_events,
    longest_event_duration
)


class TestHotelFunctionality(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # Get room and booking data for testing
        self.rooms = get_room_data()
        self.bookings = get_booking_data()

    def test_jacuzzi_room_price(self):
        """
        Test case for jacuzzi_room_price() function.
        """
        try:
            room_id, price = jacuzzi_room_price()

            # Check if a room with Jacuzzi is found
            if room_id and price:
                # Verify that the room actually has a Jacuzzi
                if "Jacuzzi" in self.rooms[room_id]["amenities"]:
                    self.test_obj.yakshaAssert("TestJacuzziRoomPrice", True, "functional")
                    print("TestJacuzziRoomPrice = Passed")
                else:
                    self.test_obj.yakshaAssert("TestJacuzziRoomPrice", False, "functional")
                    print("TestJacuzziRoomPrice = Failed")
            else:
                # If no room with Jacuzzi is found, check if that's correct
                jacuzzi_exists = any("Jacuzzi" in room["amenities"] for room in self.rooms.values())
                if not jacuzzi_exists:
                    self.test_obj.yakshaAssert("TestJacuzziRoomPrice", True, "functional")
                    print("TestJacuzziRoomPrice = Passed")
                else:
                    self.test_obj.yakshaAssert("TestJacuzziRoomPrice", False, "functional")
                    print("TestJacuzziRoomPrice = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestJacuzziRoomPrice", False, "functional")
            print(f"TestJacuzziRoomPrice = Failed")

    def test_most_expensive_room(self):
        """
        Test case for most_expensive_room() function.
        """
        try:
            room_id, price = most_expensive_room()

            # Find the most expensive room manually
            expected_room_id = max(self.rooms.items(), key=lambda x: x[1]["price"])[0]
            expected_price = self.rooms[expected_room_id]["price"]

            # Check if the result matches the expected result
            if room_id == expected_room_id and abs(price - expected_price) < 0.01:
                self.test_obj.yakshaAssert("TestMostExpensiveRoom", True, "functional")
                print("TestMostExpensiveRoom = Passed")
            else:
                self.test_obj.yakshaAssert("TestMostExpensiveRoom", False, "functional")
                print("TestMostExpensiveRoom = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestMostExpensiveRoom", False, "functional")
            print(f"TestMostExpensiveRoom = Failed | Exception: {e}")


class TestGymFunctionality(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # Create the membership file for testing
        create_membership_file()

    def test_count_members_by_plan(self):
        """
        Test case for count_members_by_plan() function.
        """
        try:
            # Call the function and get the plan counts
            plan_counts = count_members_by_plan()

            # Expected counts based on the sample data
            expected_counts = {"Gold": 2, "Silver": 2, "Platinum": 1}

            # Verify the counts match the expected values
            if (plan_counts["Gold"] == expected_counts["Gold"] and
                    plan_counts["Silver"] == expected_counts["Silver"] and
                    plan_counts["Platinum"] == expected_counts["Platinum"]):
                self.test_obj.yakshaAssert("TestCountMembersByPlan", True, "functional")
                print("TestCountMembersByPlan = Passed")
            else:
                self.test_obj.yakshaAssert("TestCountMembersByPlan", False, "functional")
                print("TestCountMembersByPlan = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCountMembersByPlan", False, "functional")
            print(f"TestCountMembersByPlan = Failed | Exception: {e}")

    def test_check_membership_status(self):
        """
        Test case for check_membership_status() function.
        """
        try:
            # Since check_membership_status doesn't return a value, we'll check if it runs without errors
            check_membership_status()

            # Verify that the function correctly identifies paid members
            with open("membership_data.txt", "r") as file:
                lines = file.readlines()
                paid_members_count = sum(1 for line in lines if "Paid" in line)

            if paid_members_count == 3:  # Based on the sample data
                self.test_obj.yakshaAssert("TestCheckMembershipStatus", True, "functional")
                print("TestCheckMembershipStatus = Passed")
            else:
                self.test_obj.yakshaAssert("TestCheckMembershipStatus", False, "functional")
                print("TestCheckMembershipStatus = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCheckMembershipStatus", False, "functional")
            print(f"TestCheckMembershipStatus = Failed | Exception: {e}")


class TestEventFunctionality(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

    def test_count_total_events(self):
        """
        Test case for count_total_events() function.
        """
        try:
            # Call the function to get the count
            result = count_total_events()
            
            # Import the events list directly to check the count
            from Event import events
            expected_count = len(events)

            # Check if the function returns the correct count
            if result == expected_count:
                self.test_obj.yakshaAssert("TestCountTotalEvents", True, "functional")
                print("TestCountTotalEvents = Passed")
            else:
                self.test_obj.yakshaAssert("TestCountTotalEvents", False, "functional")
                print("TestCountTotalEvents = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCountTotalEvents", False, "functional")
            print(f"TestCountTotalEvents = Failed | Exception: {e}")

    def test_longest_event_duration(self):
        """
        Test case for longest_event_duration() function.
        """
        try:
            # Call the function to get the longest event
            result = longest_event_duration()
            
            # Import the events list directly to calculate the longest duration manually
            from Event import events

            # Calculate the longest duration manually
            max_duration = 0
            longest_event = None

            for event in events:
                start_date = datetime.strptime(event[1], "%Y-%m-%d")
                end_date = datetime.strptime(event[2], "%Y-%m-%d")
                duration = (end_date - start_date).days

                if duration > max_duration:
                    max_duration = duration
                    longest_event = event

            # Check if the function returns the correct event name and duration
            if result and result[0] == longest_event[0] and result[1] == max_duration:
                self.test_obj.yakshaAssert("TestLongestEventDuration", True, "functional")
                print("TestLongestEventDuration = Passed")
            else:
                self.test_obj.yakshaAssert("TestLongestEventDuration", False, "functional")
                print("TestLongestEventDuration = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestLongestEventDuration", False, "functional")
            print(f"TestLongestEventDuration = Failed | Exception: {e}")

    def test_display_upcoming_events(self):
        """
        Test case for display_upcoming_events() function.
        """
        try:
            # Since display_upcoming_events should return a list of upcoming events
            result = display_upcoming_events()
            
            # Check if the function returns a non-empty list
            if result and isinstance(result, list) and len(result) > 0:
                # Verify that each item in the result is a valid event
                valid_events = all(isinstance(event, tuple) and len(event) >= 3 for event in result)
                if valid_events:
                    self.test_obj.yakshaAssert("TestDisplayUpcomingEvents", True, "functional")
                    print("TestDisplayUpcomingEvents = Passed")
                else:
                    self.test_obj.yakshaAssert("TestDisplayUpcomingEvents", False, "functional")
                    print("TestDisplayUpcomingEvents = Failed")
            else:
                self.test_obj.yakshaAssert("TestDisplayUpcomingEvents", False, "functional")
                print("TestDisplayUpcomingEvents = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestDisplayUpcomingEvents", False, "functional")
            print(f"TestDisplayUpcomingEvents = Failed | Exception: {e}")
