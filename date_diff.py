
from django.utils.translation import ungettext, ugettext as _
from django import template
register = template.Library()

import math
import datetime

@register.filter
def fuzzy_date(d, now=None):
    return fuzzy_date_diff(d, now)


def fuzzy_date_diff(d, now=None):

    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)

    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)

    if not now:
        if d.tzinfo:
            from django.utils.tzinfo import LocalTimezone
            now = datetime.datetime.now(LocalTimezone(d))
        else:
            now = datetime.datetime.now()

    in_the_futur = d > now

    today = datetime.datetime(now.year, now.month, now.day)
    tomorrow = datetime.datetime(now.year, now.month, now.day+1)
    
    if in_the_futur:
        delta = d - now
        delta_midnight = d - tomorrow
    else:
        delta = now - d
        delta_midnight = today - d

    if delta.days == 0 and delta.seconds < 60:
        return _("just now")

    day_chunks = (
        (365.242199, lambda n: ungettext('year', 'years', n)),
        (30.4368499, lambda n: ungettext('month', 'months', n)),
        (7.0, lambda n: ungettext('week', 'weeks', n)),
        (1.0, lambda n: ungettext('day', 'days', n)),
    )
    
    second_chunks = (
        (3600, lambda n: ungettext('hour', 'hours', n)),
        (60, lambda n: ungettext('minute', 'minutes', n)),
    )

    if delta_midnight.days == 0:
        hours = delta_midnight.seconds / 3600.
        if in_the_futur:
            if hours < 12:
                return _("tomorrow morning")
            else:
                return _("tomorrow afternoon")
        else:
            if hours > 12:
                return _("yesterday morning")
            else:
                return _("yesterday afternoon")

    count = 0
    for i, (chunk, name) in enumerate(day_chunks):
        if delta.days >= chunk:
            count = round((delta_midnight.days + 1)/chunk, 0)
            break

    if not count:
        for i, (chunk, name) in enumerate(second_chunks):
            if delta.seconds >= chunk:
                count = round(delta.seconds/chunk, 0)
                break

    if in_the_futur:
        return _('in %(number)d %(type)s') % \
            {'number': count, 'type': name(count)}
    else:
        return _('%(number)d %(type)s ago') % \
            {'number': count, 'type': name(count)}

