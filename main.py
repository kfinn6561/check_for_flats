from config import *
import time
from flatchecker import FlatChecker

if __name__ == "__main__":
    time.sleep(DELAY_TIME)
    fc=FlatChecker()
    fc.update_from_file()
    while True:
        fc.update_from_web()
        time.sleep(SLEEP_TIME)
