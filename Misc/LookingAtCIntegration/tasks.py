import os
import invoke
import shutil
import glob


@invoke.task
def clean(c):
    """ Remove any built objects """
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib"
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)
    for dir_pattern in "Release":
        for dir in glob.glob(dir_pattern):
            shutil.rmtree(dir)


@invoke.task()
def build_example(c):
    """Building Library"""
    path = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Auxiliary\\Build\\'
    path = f'"{path}vcvars32.bat" x64 && cd "{os.getcwd()}" && cl /LD example_loop_if.c'
    c.run(path)


@invoke.task()
def test_example(c):
    """Testing Library"""
    c.run("python test_example.py")


@invoke.task(clean, build_example, test_example)
def all(c):
    pass
