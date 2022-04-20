# can add timezone infor with tz attribute
# more timezones than just UTC added
# uses computers inbuilt timezone library (for Windows requires tzdata package)

from datetime import datetime, timezone, timedelta
import zoneinfo
from zoneinfo import ZoneInfo

# in python 3.8

print(datetime.now())
print(datetime.now(tz=timezone.utc))

# in python 3.9

print(ZoneInfo('America/Vancouver'))
print(datetime.now(tz=ZoneInfo('Europe/Oslo')))

release_date = datetime(2020, 10, 5, 3, 9, tzinfo=ZoneInfo('America/Vancouver'))

print(release_date.astimezone(ZoneInfo('Europe/Oslo')))
print(len(zoneinfo.available_timezones()))

# special timezone, christmas islands changed which side of the date line
# they were on, 1 Jan 1995
tz_kiritimati = ZoneInfo('Pacific/Kiritimati')

nye = datetime(1994, 12, 31, 9, 0, tzinfo=ZoneInfo('UTC'))

print(nye.astimezone(tz_kiritimati))

hour = timedelta(hours=1)

print((nye + hour).astimezone(tz_kiritimati))

# answer is -10 hrs, shown as -1d +14h (= -10h)
print(tz_kiritimati.utcoffset(datetime(1994, 12, 30)))
print(tz_kiritimati.utcoffset(datetime(1995, 1, 1)))

tz = ZoneInfo('America/Vancouver')

print(tz.tzname(datetime(2020, 10, 5)))
print(tz.tzname(datetime(2020, 11, 5)))

# best practices:
# civil specified times should have a timezone approriate to location
# timestamps should be naïve, based on UTC to ignore daylight savings 
