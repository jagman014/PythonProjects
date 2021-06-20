import ctypes
import os
import time

start = time.time()

c_lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "example_loop_if"))

c_lib.main()

end = time.time()

print('\n', end - start)
# 0.017398834228515625 s
