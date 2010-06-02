import os
from django.utils.translation import ungettext, ugettext as _
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import datetime
import unittest
from date_diff import fuzzy_date_diff
import math

class TestDateDiff(unittest.TestCase):

    def setUp(self):
        pass

    def test_fuzzy_date_diff(self):
        
        now = datetime.datetime.now()
        
        self.assertEqual(fuzzy_date_diff(now), 'just now')

        self.assertEqual(
            fuzzy_date_diff(now - datetime.timedelta(seconds=29)),
            'just now')

        self.assertEqual(
            fuzzy_date_diff(now - datetime.timedelta(seconds=30)),
            'just now')

        self.assertEqual(
            fuzzy_date_diff(now - datetime.timedelta(seconds=45)),
            'just now')

        self.assertEqual(
            fuzzy_date_diff(now - datetime.timedelta(seconds=60)),
            '1 minute ago')

        self.assertEqual(
            fuzzy_date_diff(now - datetime.timedelta(seconds=90)),
            '1 minute ago')

        self.assertEqual(
            fuzzy_date_diff(now - datetime.timedelta(seconds=120)),
            '2 minutes ago')

        self.assertEqual(
            fuzzy_date_diff(now - datetime.timedelta(hours=1)),
            '1 hour ago')

        self.assertEqual(
            fuzzy_date_diff(now - datetime.timedelta(hours=2)),
            '2 hours ago')

        yesterday = now - datetime.timedelta(hours=24)
        self.assertEqual(
            fuzzy_date_diff(yesterday),
            'yesterday morning')

        now = datetime.datetime(year=2010, month=5, day=25, hour=20, minute=12, second=24)
        today = datetime.datetime(now.year, now.month, now.day)
        hours = int(math.floor((now - today).seconds/3600.))

        self.assertEqual(
            fuzzy_date_diff(today + datetime.timedelta(seconds=1), now),
            ungettext('1 hour ago', '%(hours)d hours ago', hours) % {'hours':hours}
        )
        
        yesterday = today - datetime.timedelta(hours=23)
        self.assertEqual(
            fuzzy_date_diff(yesterday, now),
            'yesterday morning')

        yesterday = today - datetime.timedelta(minutes=(24*60-1))
        self.assertEqual(
            fuzzy_date_diff(yesterday, now),
            'yesterday morning')

        yesterday = today - datetime.timedelta(hours=5)
        self.assertEqual(
            fuzzy_date_diff(yesterday, now),
            'yesterday afternoon')

        limit_2_days = today - datetime.timedelta(minutes=(24*60+1))
        self.assertEqual(
            fuzzy_date_diff(limit_2_days, now),
            '2 days ago')

        week = today - datetime.timedelta(days=7)
        self.assertEqual(
            fuzzy_date_diff(week, now),
            '1 week ago')

        weeks_2 = today - datetime.timedelta(days=14)
        self.assertEqual(
            fuzzy_date_diff(weeks_2, now),
            '2 weeks ago')

        weeks_3 = today - datetime.timedelta(days=21)
        self.assertEqual(
            fuzzy_date_diff(weeks_3, now),
            '3 weeks ago')

        weeks_4 = today - datetime.timedelta(days=28)
        self.assertEqual(
            fuzzy_date_diff(weeks_4, now),
            '4 weeks ago')

        weeks_4 = today - datetime.timedelta(days=30)
        self.assertEqual(
            fuzzy_date_diff(weeks_4, now),
            '4 weeks ago')

        month_1 = today - datetime.timedelta(days=31)
        self.assertEqual(
            fuzzy_date_diff(month_1, now),
            '1 month ago')

        # a little bit weird, but correct according to
        # the values
        month_12 = today - datetime.timedelta(days=365)
        self.assertEqual(
            fuzzy_date_diff(month_12, now),
            '12 months ago')

        year_1 = today - datetime.timedelta(days=366)
        self.assertEqual(
            fuzzy_date_diff(year_1, now),
            '1 year ago')

        # futur testing
        futur = now + datetime.timedelta(seconds=5)
        self.assertEqual(
            fuzzy_date_diff(futur, now),
            'just now')

        futur = now + datetime.timedelta(seconds=100)
        self.assertEqual(
            fuzzy_date_diff(futur, now),
            'in 1 minute')

        futur = now + datetime.timedelta(minutes=60)
        self.assertEqual(
            fuzzy_date_diff(futur, now),
            'in 1 hour')

        futur = now + datetime.timedelta(hours=5)
        self.assertEqual(
            fuzzy_date_diff(futur, now),
            'tomorrow morning')

        futur = now + datetime.timedelta(hours=23)
        self.assertEqual(
            fuzzy_date_diff(futur, now),
            'tomorrow afternoon')

        futur = now + datetime.timedelta(hours=48)
        self.assertEqual(
            fuzzy_date_diff(futur, now),
            'in 2 days')

        futur = now + datetime.timedelta(days=30)
        self.assertEqual(
            fuzzy_date_diff(futur, now),
            'in 4 weeks')

        futur = now + datetime.timedelta(days=32)
        self.assertEqual(
            fuzzy_date_diff(futur, now),
            'in 1 month')


if __name__ == '__main__':
    unittest.main()