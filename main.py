from config import *
from check_sites import check_sites
from flats import load_flat_from_file
from general_tools import pload
import time







class FlatChecker():
    def __init__(self) -> None:
        self.flats=[]
        self.ids=[]

    def update_from_file(self):
        print(time.ctime()+': Updating from file')
        self.ids=pload(ID_FILE)
        for id in self.ids:
            self.flats.append(load_flat_from_file(FLAT_DIR+'/'+id+'.pkl'))

    def update_from_web(self):
        print(time.ctime()+': Updating from web')
        new=0
        new_flats=check_sites()
        for flat in new_flats:
            if flat.id not in self.ids:
                self.flats.append(flat)
                self.ids.append(flat.id)
                flat.send_alert()
                flat.save()
                new+=1
        print('%d new properties' %new)


if __name__ == "__main__":
    time.sleep(DELAY_TIME)
    fc=FlatChecker()
    fc.update_from_file()
    while True:
        fc.update_from_web()
        time.sleep(SLEEP_TIME)
