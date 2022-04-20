import re

# \w is equivelent to [a-zA-Z0-9_], any alphanumerics and underscore
print(re.search('\w', '#(.a$@&'))
print(re.search('[a-zA-Z0-9_]', '#(.a$@&'))

# \W is equivelent to [^a-zA-Z0-9_], not any alphanumerics or underscore
print(re.search('\W', 'a_1*3Qb'))
print(re.search('[^a-zA-Z0-9_]', 'a_1*3Qb'))
