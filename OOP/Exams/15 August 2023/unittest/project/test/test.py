import unittest

from project.trip import Trip


class TestTrip(unittest.TestCase):
    def setUp(self):
        self.trip = Trip(1000, 2, False)
        self.trip2 = Trip(100000, 5, True)

    def test_init(self):
        self.assertEqual(self.trip.budget, 1000)
        self.assertEqual(self.trip.travelers, 2)
        self.assertEqual(self.trip.is_family, False)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})

    def test_traveller_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.trip.travelers = 0

        self.assertEqual(str(ex.exception), 'At least one traveler is required!')

    def test_family_setter(self):
        self.assertEqual(self.trip.is_family, False)

        self.trip.travelers = 1

        self.trip.is_family = True
        self.assertEqual(self.trip.is_family, False)

    def test_book_a_trip_destination_not_in_offer(self):
        result = self.trip.book_a_trip('Test')
        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_budget_not_enough(self):
        self.trip.budget = 100
        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual(result, 'Your budget is not enough!')

    def test_book_a_trip_successfully_booked(self):
        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual(result, 'Successfully booked destination Bulgaria! Your budget left is 0.00')

        self.assertEqual(self.trip.booked_destinations_paid_amounts, {'Bulgaria': 1000})
        self.assertEqual(self.trip.budget, 0)

        result = self.trip2.book_a_trip('Australia')
        self.assertEqual(result, 'Successfully booked destination Australia! Your budget left is 74350.00')

    def test_booking_status_no_bookings(self):
        result = self.trip.booking_status()
        self.assertEqual(result, 'No bookings yet. Budget: 1000.00')

        result = self.trip2.booking_status()
        self.assertEqual(result, 'No bookings yet. Budget: 100000.00')

    def test_booking_status(self):
        self.trip2.book_a_trip('Bulgaria')
        self.trip2.book_a_trip('Bulgaria')
        result = self.trip2.booking_status()
        self.assertEqual(
            result,
            """Booked Destination: Bulgaria
Paid Amount: 2250.00
Number of Travelers: 5
Budget Left: 95500.00""")


if __name__ == '__main__':
    unittest.main()
