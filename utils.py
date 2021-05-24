import os
import threading
import contextlib

@contextlib.contextmanager
def chdir_temp(new_dir):
    """ 
    Like os.chdir(), but always restores the old working directory

    use like this:

        with chdir_temp('dir'):
            do_some_stuff()
    """
    old_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(old_dir)


def get_file_directory():
    """Return an absolute path to the current file directory"""
    return os.path.dirname(os.path.realpath(__file__))



class SubshellThread(threading.Thread):
    def __init__(self, command):
        threading.Thread.__init__(self)
        self.command = command
    
    def run(self):
        try:
            os.system(self.command)
        except Exception as e:
            print(str(e))