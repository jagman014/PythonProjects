# file encodeing depends on operating system
# add "encoding=" kwarg to open operators
# add warning at runtime "-X warn_default_encoding"

# context manager syntax
# before for multiple
with read_path.open(mode='r', encoding='utf-8') as read_file, \
        write_path.open(mode='w', encoding='utf-8') as write_file:
    # do stuff
    ...

# now
with (
    read_path.open(mode='r', encoding='utf-8') as read_file,
    write_path.open(mode='w', encoding='utf-8') as write_file,
):
    # do stuff
    ...

# python uses OpenSSL
# require OpenSSL 1.1.1 or greater on linux

# sys module
import sys

print(len(sys.modules))
print(sorted(sys.modules)[-5:])

print(len(sys.stdlib_module_names))
print(sorted(sys.stdlib_module_names)[-5:])

import aiofiles

print(len(sys.modules))
print(len(sys.stdlib_module_names))

print(set(mod for mod in sys.modules if '.' not in mod) - sys.stdlib_module_names)

# arv
print("argv:", sys.argv) # python arguments
print('orig_argv:', sys.orig_argv) # console arguments

# version detection
# sys.version < '3.6' -> '3.6' > '3.10' string comparison is bad
# sys.version_info < (3, 6) -> (3, 6) < (3, 10) tuple comparison is good
