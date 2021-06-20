from contextlib import contextmanager
# 'with' statement and context managers

with open('hello.txt', 'w') as f:
    f.write('hello world')
# automatically closes file after with statement

# Manually:
# f = open('hello.txt', 'w')
# try:
#     f.write('hello world')
# finally:
#     f.close()


# context manager
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# with call both the __enter__ and __exit__ methods
with ManagedFile('hello_1.txt') as f:
    f.write('hello world!')


# contextlib example
@contextmanager
def managed_file(name):
    try:
        this_file = open(name, 'w')
        yield this_file
    finally:
        this_file.close()


with managed_file('hello_2.txt') as f:
    f.write('hello_world')
    f.write('\nbye')
