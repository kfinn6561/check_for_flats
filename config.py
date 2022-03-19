import os
from general_tools import pdump

ID_FILE='property_ids.pkl'
FLAT_DIR='saved_flats'


RIGHTMOVE_PLACEHOLDER_FNAME='rightmove_placeholder.pkl'
SLATERHOGG_PLACEHOLDER_FNAME='slaterhogg_placeholder.pkl'

DELAY_TIME=0    #3600*9
SLEEP_TIME=60

SEND_SMS=True
SEND_EMAILS=True
SOUND_ALERTS=True
OPEN_WEBBROWSER=False

SMS_TO_NUMBERS=['+447582534955','+447530308152']
EMAIL_ADDRESSES=['kieran.finn@hotmail.com','annasains@gmail.com']

if not os.path.isfile(ID_FILE):
    pdump([],ID_FILE)
if not os.path.isdir(FLAT_DIR):
    os.mkdir(FLAT_DIR)