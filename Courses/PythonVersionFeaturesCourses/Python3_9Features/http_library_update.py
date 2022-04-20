# new http status codes added
from http import HTTPStatus

print(repr(HTTPStatus.OK))
print(HTTPStatus.OK.description)

# new addittion 103 and 425, and 418 (I'm a teapot)
print(repr(HTTPStatus.EARLY_HINTS))
print(HTTPStatus.EARLY_HINTS.value)
print(HTTPStatus(425).phrase)
