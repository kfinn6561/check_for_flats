from config import *
from general_tools import pload,pdump

ids=pload(ID_FILE)
ids=ids[:-1]
pdump(ids,ID_FILE)