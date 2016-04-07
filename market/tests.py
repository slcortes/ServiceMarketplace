from django.test import TestCase
from django.utils import timezone
from .models import Service
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import datetime


class SerivceModelTests(TestCase):

    def test_field_mapping_and_defaults_on_create(self):
        final_time = datetime.datetime.now()
        final_time += datetime.timedelta(weeks=1, days=2, hours=7)

        service = Service(
            title="I want someone to paint my house.",
            description="I have a to story house that needs a new coat of \
                         paint. I will buy the paint and tools, but I need \
                         someone to do the painting, preferably during the \
                         weekend when I can be home as well.",
            bid=134.56,
            final_time=final_time,
            location="Pomona, CA"
        )

        self.assertEqual(service.title, "I want someone to paint my house.")
        self.assertEqual(service.description,
                         "I have a to story house that needs a new coat of \
                         paint. I will buy the paint and tools, but I need \
                         someone to do the painting, preferably during the \
                         weekend when I can be home as well.")
        self.assertEqual(service.bid, 134.56)
        self.assertEqual(service.final_time, final_time)
        self.assertEqual(service.location, "Pomona, CA")
        self.assertEqual(service.is_open, True)

    def test_loggedin_user_is_client(self):
        user = User.objects.create_user(username='john',
                                        email='lennon@thebeatles.com',
                                        password='johnpassword')
        user.save()
        user = authenticate(username='john', password='johnpassword')

        service = Service(
            title="I want someone to paint my house.",
            description="I have a to story house that needs a new coat of \
                         paint. I will buy the paint and tools, but I need \
                         someone to do the painting, preferably during the \
                         weekend when I can be home as well.",
            bid=134.56,
            final_time=timezone.now(),
            location="Pomona, CA"
        )
        service.client = user
        service.save()
        self.assertEqual(service.client, user)

    def test_max_lengths(self):
        service = Service(
            title="I want someone to paint my house.",
            description="I",
            location="IwanttogotothemoviesandwatchwhateverIwantwheneverIwant",
            final_time=timezone.now()
        )
        with self.assertRaises(Exception):
            service.full_clean()

        service = Service(
            title="I have a to story house that needs a new coat of \
                   paint. I will buy the paint and tools, but I need",
            description="I",
            final_time=timezone.now()
        )
        with self.assertRaises(Exception):
            service.full_clean()

        service = Service(
            title="I want someone to paint my house",
            description="I",
            bid=9230293.129301,
            final_time=timezone.now()
        )
        with self.assertRaises(Exception):
            service.full_clean()

    def test_created_date(self):
        time = timezone.now()
        service = Service(created_date=time)
        self.assertEqual(service.created_date, time)
