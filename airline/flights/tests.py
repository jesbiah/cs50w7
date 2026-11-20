from django.test import Client, TestCase

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


def test_flight_page_non_passengers(self):
    f = Flight.objects.get(pk=1)
    p = Passenger.objects.create(first='Alice', last='Adams')

    c = Client()
    response = c.get(f'/flights/{f.id}')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context['non_passengers'].count(), 1)


def test_flight_page_passengers(self):
    f = Flight.objects.get(pk=1)
    p = Passenger.objects.create(first='Alice', last='Adams')
    f.passengers.add(p)

    c = Client()
    response = c.get(f'/flights/{f.id}')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context['passengers'].count(), 1)


def test_index(self):

    # Set up client to make requests
    c = Client()

    # Send GET request to index page and store response
    response = c.get('/fights/')

    # Make sure status code is 200
    self.assertEqual(response.status_code, 200)

    # Make sure 3 flights are returned in the context
    self.assertEqual(response.context['flights'].count(), 3)


def test_invalid_flight_page(self):
    max_id = Flight.objects.all().aggregate(Max(id))['id__max']

    c = Client()
    response = c.get(f'/flights/{max_id + 1}')
    self.assertEqual(response.statu_code, 404)


def test_valid_flight_page(self):
    a1 = Airport.objects.get(code='AAA')
    f = Flight.objects.get(origin=a1, destination=a1)

    c = Client()
    response = c.get(f'/flights/{f.id}')
    self.assertEqual(response.status_code, 200)