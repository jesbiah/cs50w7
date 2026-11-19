from django.test import TestCase

from .models import Airport, Flight, Passenger

# Create your tests here.
class FLightTestCase(TestCase):

    def setUp(self):

        # Create airports
        a1 = Airport.objects.create(code='AAA', city='City A')
        a2 = Airport.objects.create(code='BBB', city='City B')

        # Create flights
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)

        # Make sure our departures and arrivals fields work correctly 
        # by attempting to count the number of departures (which we know should be 3) 
        # and arrivals (which should be 1) from airport AAA
    def test_departures_count(self):
        a = Airport.objects.get(code='AAA')
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code='AAA')
        self.assertEqual(a.arrivals.count(), 1)

    # Test the is_valid_flight function we added to our Flight model
    def test_valid_flight(self):
        a1 = Airport.objects.get(code='AAA')
        a2 = Airport.objects.get(code='BBB')
        f = Flight.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1 = Airport.objects.get(code='AAA')
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code='AAA')
        a2 = Airport.objects.get(code='BBB')
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())