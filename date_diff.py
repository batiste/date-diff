import datetime
from django.utils.translation import ungettext, ugettext as _
import math

#@register.filter
def fuzzy_date_diff(d, now=None):
    if not d:
        return ''

    if not now:
        now = datetime.datetime.utcnow()
        
    if d > now:
        # date diff doesn't handle futur dates yet.
        return _("in the future")
    
    today = datetime.datetime(now.year, now.month, now.day)
    delta = now - d
    delta_midnight = today - d
    days = delta.days
    hours = math.floor(delta.seconds / 3600.)
    minutes = math.floor(delta.seconds / 60.)

    chunks = (
        (365.242199, lambda n: ungettext('year', 'years', n)),
        (30.4368499, lambda n: ungettext('month', 'months', n)),
        (7.0, lambda n: ungettext('week', 'weeks', n)),
        (1.0, lambda n: ungettext('day', 'days', n)),
    )

    if days == 0:
        if hours == 0:
            if minutes > 0:
                return ungettext('1 minute ago', \
                    '%(minutes)d minutes ago', minutes) % \
                    {'minutes': minutes}
            else:
                return _("just now")
        else:
            return ungettext('1 hour ago', '%(hours)d hours ago', hours) \
            % {'hours': hours}

    if delta_midnight.days == 0:
        hours = math.floor(delta_midnight.seconds / 3600.)
        if hours > 12:
            return _("yesterday morning")
        else:
            return _("yesterday afternoon")

    count = 0
    for i, (chunk, name) in enumerate(chunks):
        if days >= chunk:
            count = round((delta_midnight.days + 1)/chunk, 0)
            break

    return _('%(number)d %(type)s ago') % \
        {'number': count, 'type': name(count)}