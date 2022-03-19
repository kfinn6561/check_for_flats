
from check_sites import check_sites
from flats import load_flat_from_file
from general_tools import pload
import time
from config import *
from alerts import send_alerts

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
        current_flats=check_sites()
        new_flats=[]
        for flat in current_flats:
            if flat.id not in self.ids:
                new_flats.append(flat)
                self.ids.append(flat.id)
                flat.save()
        if len(new_flats)>0:
            print('%d new properties' %len(new_flats))
            self.flats+=new_flats
            send_alerts(new_flats)
        else:
            print('no new properties')