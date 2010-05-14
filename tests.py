import os
from django.utils.translation import ungettext, ugettext as _
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import datetime
import unittest
from date_diff import date_diff
import math

class TestDateDiff(unittest.TestCase):

    def setUp(self):
        pass

    def test_date_diff(self):
        now = datetime.datetime.utcnow()
        self.assertEqual(date_diff(now), 'just now')

        self.assertEqual(
            date_diff(now - datetime.timedelta(seconds=29)),
            'just now')

        self.assertEqual(
            date_diff(now - datetime.timedelta(seconds=30)),
            'just now')

        self.assertEqual(
            date_diff(now - datetime.timedelta(seconds=45)),
            'just now')

        self.assertEqual(
            date_diff(now - datetime.timedelta(seconds=60)),
            '1 minute ago')

        self.assertEqual(
            date_diff(now - datetime.timedelta(seconds=90)),
            '1 minute ago')

        self.assertEqual(
            date_diff(now - datetime.timedelta(seconds=120)),
            '2 minutes ago')

        self.assertEqual(
            date_diff(now - datetime.timedelta(hours=1)),
            '1 hour ago')

        self.assertEqual(
            date_diff(now - datetime.timedelta(hours=2)),
            '2 hours ago')

        yesterday = now - datetime.timedelta(hours=24)
        self.assertEqual(
            date_diff(yesterday),
            'yesterday at %s' % yesterday.strftime("%H:%M"))

        now = datetime.datetime.utcnow()
        today = datetime.datetime(now.year, now.month, now.day)
        hours = int(math.floor((now - today).seconds/3600.))

        self.assertEqual(
            date_diff(today),
            ungettext('1 hour ago', '%(hours)d hours ago', hours) % {'hours':hours}
        )
        
        yesterday = today - datetime.timedelta(hours=23)
        self.assertEqual(
            date_diff(yesterday),
            'yesterday at %s' % yesterday.strftime("%H:%M"))

        yesterday = today - datetime.timedelta(minutes=(24*60-1))
        self.assertEqual(
            date_diff(yesterday),
            'yesterday at %s' % yesterday.strftime("%H:%M"))

        limit_2_days = today - datetime.timedelta(minutes=(24*60+1))
        self.assertEqual(
            date_diff(limit_2_days),
            '2 days ago')

        week = today - datetime.timedelta(days=7)
        self.assertEqual(
            date_diff(week),
            '1 week ago')

        week = today - datetime.timedelta(days=14)
        self.assertEqual(
            date_diff(week),
            '2 weeks ago')

        week = today - datetime.timedelta(days=21)
        self.assertEqual(
            date_diff(week),
            '3 weeks ago')

        week = today - datetime.timedelta(days=28)
        self.assertEqual(
            date_diff(week),
            '4 weeks ago')

        week = today - datetime.timedelta(days=30)
        self.assertEqual(
            date_diff(week),
            '4 weeks ago')

        week = today - datetime.timedelta(days=31)
        self.assertEqual(
            date_diff(week),
            '1 month ago')

        # a little bit weird, but correct according to
        # the values
        week = today - datetime.timedelta(days=365)
        self.assertEqual(
            date_diff(week),
            '12 months ago')

        week = today - datetime.timedelta(days=366)
        self.assertEqual(
            date_diff(week),
            '1 year ago')

        futur = datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
        self.assertEqual(
            date_diff(futur),
            'in the future')


if __name__ == '__main__':
    unittest.main()