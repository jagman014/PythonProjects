# introdices 2 new operators for merging dicts and dict-like objects
from collections import defaultdict

# python 3.8 method
pycon = {
    2016: 'Portland',
    2018: 'Cleveland'
}

europython = {
    2017: 'Rimini',
    2018: 'Edinburgh',
    2019: 'Basel'
}

# 3.8 method doesn't edit original dicts
merged = {**pycon, **europython}

print(merged)

# alterante 3.8 method
merged_1 = pycon.copy()

for key, value in europython.items():
    merged_1[key] = value

print(merged_1)

# another alternate 3.8 method, but overwrites existing dict
pycon.update(europython)

print(pycon)

# can combine previous methods using the walrus operator
# need walrus as .update operates in-place
pycon = {
    2016: 'Portland',
    2018: 'Cleveland'
}

(merged_2 := pycon.copy()).update(europython)

print(merged_2)

# 3.9 introduces the pipe '|' operator to make cleaner code
print(pycon | europython)

# '|' acts as a merge without editing the original
# whereas '|=' acts as an update, altering the original dict
pycon |= europython

print(pycon)

# also works on dict-like objects
# lambda used to return nothing given a KeyError
europe = defaultdict(
    lambda: "",
    {
        'Norway': 'Oslo',
        'Spain': 'Madrid'
    }
)

africa = defaultdict(
    lambda: '',
    {
        'Egypt': 'Cairo',
        'Zimbabwe': 'Harare'
    }
)

# previous methods also work, but returns a standard dict
print({**europe, **africa})

# the 3.9 method returns the same object type
print(europe | africa)

# can also merge with other data types, resulting in an updated dict
libraries = {
    'collections': 'Container datatypes',
    'math': 'Maths functions'
}

libraries |= [('graphlib', 'Topological sort tools')]

print(libraries)

# as always order of operation is important
asia = {
    'Georgia': 'Tbilisi',
    'Japan': 'Tokyo'
}

usa = {
    'Missouri': 'Jefferson City',
    'Georgia': 'Atlanta'
}

# the second dict overwrites the first
print(asia | usa)

print(usa | asia)

# dunder functions of __or__ -> |, __ior__ -> |=
