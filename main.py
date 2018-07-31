"""
A brief loading bar class to allow a threaded display to display for a desired amount of code. Message is optional.
Personal use.
"""
import threading
import itertools
import sys
import time

class LoadBar(object):
    def __init__(self,message = " "):
        self.m = message
        
    def loading(self):
        self.completed = False
        t = threading.Thread(target=self.cycle)
        t.start()
        
    def cycle(self):
        print("\n\n")
        for i,c in enumerate(itertools.cycle(['|', '/', '-', '\\'])):
            if self.completed:
                break
            display = list(self.m)
            display[i%len(self.m)] = " "
            sys.stdout.write('\r'+c+' loading ' +"".join(display)+' '+c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'\rDone with {self.m}         \n\n')
        
    def done(self):
        self.completed = True