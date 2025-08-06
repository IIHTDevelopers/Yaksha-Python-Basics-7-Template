import unittest
import pandas as pd
from hotel import filter_hotels_by_rating, get_average_price
from test.TestUtils import TestUtils

class TestHotelListing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.df = pd.DataFrame({
            "Hotel ID": [1, 2, 3, 4, 5],
            "Hotel Name": ["Grand Stay", "Comfort Inn", "Luxury Palace", "Budget Lodge", "Ocean View"],
            "Rating": [4.5, 3.8, 4.9, 3.2, 4.3],
            "Price Per Night": [2500, 1800, 4000, 1200, 3200]
        })

    def test_filter_hotels_by_rating(self):
        try:
            result = filter_hotels_by_rating(self.df, 4.0)
            expected_names = ["Grand Stay", "Luxury Palace", "Ocean View"]
            actual_names = result["Hotel Name"].tolist()
            status = actual_names == expected_names
            self.test_obj.yakshaAssert("TestFilterHotelsByRating", status, "functional")
            print("TestFilterHotelsByRating =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestFilterHotelsByRating", False, "functional")
            print("TestFilterHotelsByRating = Failed due to Exception:", e)

    def test_get_average_price(self):
        try:
            result = get_average_price(self.df)
            expected = round(sum([2500, 1800, 4000, 1200, 3200]) / 5, 2)
            status = result == expected
            self.test_obj.yakshaAssert("TestAveragePrice", status, "functional")
            print("TestAveragePrice =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestAveragePrice", False, "functional")
            print("TestAveragePrice = Failed due to Exception:", e)


import unittest
import pandas as pd
from Gym import calculate_total_contribution, count_members_per_type
from test.TestUtils import TestUtils

class TestGymMembershipCore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.df = pd.DataFrame({
            "Member ID": [101, 102, 103, 104, 105],
            "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
            "Membership Type": ["Gold", "Silver", "Gold", "Bronze", "Silver"],
            "Monthly Fee": [1500, 1000, 1500, 800, 1000],
            "Months Active": [12, 8, 6, 3, 10]
        })

    def test_calculate_total_contribution(self):
        try:
            result = calculate_total_contribution(self.df, 101)  # 1500 × 12 = 18000
            expected = 18000
            status = result == expected
            self.test_obj.yakshaAssert("TestTotalContribution", status, "functional")
            print("TestTotalContribution =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalContribution", False, "functional")
            print("TestTotalContribution = Failed due to Exception:", e)

    def test_count_members_per_type(self):
        try:
            result = count_members_per_type(self.df)
            expected = {'Gold': 2, 'Silver': 2, 'Bronze': 1}
            status = result == expected
            self.test_obj.yakshaAssert("TestCountMembersPerType", status, "functional")
            print("TestCountMembersPerType =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCountMembersPerType", False, "functional")
            print("TestCountMembersPerType = Failed due to Exception:", e)

def test_is_alice_long_term(self):
        try:
            result = is_alice_long_term(self.df)
            expected = False  # Alice has 12 months, not > 12
            status = result == expected
            self.test_obj.yakshaAssert("TestIsAliceLongTerm", status, "functional")
            print("TestIsAliceLongTerm =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestIsAliceLongTerm", False, "functional")
            print("TestIsAliceLongTerm = Failed due to Exception:", e)


import unittest
import pandas as pd
from Event import get_total_people_registered, count_events_with_high_fees, count_events_in_newyork
from test.TestUtils import TestUtils

class TestEventOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.df = pd.DataFrame({
            "Event ID": [201, 202, 203, 204, 205],
            "Event Name": ["Tech Summit", "Music Fest", "Job Fair", "Food Carnival", "Book Launch"],
            "Location": ["New York", "Los Angeles", "Chicago", "New York", "Boston"],
            "Registered People": [120, 200, 75, 180, 50],
            "Entry Fee": [50, 30, 0, 20, 10]
        })

    def test_total_people_registered(self):
        try:
            result = get_total_people_registered(self.df)
            expected = 625
            status = result == expected
            self.test_obj.yakshaAssert("TestTotalPeopleRegistered", status, "functional")
            print("TestTotalPeopleRegistered =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalPeopleRegistered", False, "functional")
            print("TestTotalPeopleRegistered = Failed due to Exception:", e)

    def test_events_with_high_fees(self):
        try:
            result = count_events_with_high_fees(self.df)
            expected = 3  # 50, 30, 20
            status = result == expected
            self.test_obj.yakshaAssert("TestEventsWithHighFees", status, "functional")
            print("TestEventsWithHighFees =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestEventsWithHighFees", False, "functional")
            print("TestEventsWithHighFees = Failed due to Exception:", e)

    def test_events_in_newyork(self):
        try:
            result = count_events_in_newyork(self.df)
            expected = 2
            status = result == expected
            self.test_obj.yakshaAssert("TestEventsInNewYork", status, "functional")
            print("TestEventsInNewYork =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestEventsInNewYork", False, "functional")
            print("TestEventsInNewYork = Failed due to Exception:", e)
