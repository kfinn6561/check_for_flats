from config import *
from pickle import UnpicklingError
from general_tools import pload,pdump,remove_excess_whitespace
from send_emails import send_email
from sms import send_sms
import webbrowser

class Flat():
    def __init__(self,id,description,link) -> None:
        self.id=id
        self.description=remove_excess_whitespace(description).encode('utf-8').decode('ascii','ignore')
        self.link=link
        self.fname=FLAT_DIR+'/'+self.id+'.pkl'

    def save(self):
        try:
            ids=pload(ID_FILE)
        except (UnpicklingError,FileNotFoundError):
            ids=[]
        if self.id not in ids:
            ids.append(self.id)
        pdump(ids,ID_FILE)
        pdump([self.id,self.description,self.link],self.fname)

    def send_alert(self):
        print('SENDING ALERT')
        alert=self.description+'\n'+self.link
        print(alert)
        if SOUND_ALERTS:
            print('\a')
        if SEND_EMAILS:
            send_email(alert)
        if SEND_SMS:
            send_sms(alert)
        if OPEN_WEBBROWSER:
            webbrowser.open(self.link)

def load_flat_from_file(fname):
    id,description,link=pload(fname)
    return Flat(id,description,link)