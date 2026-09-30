import logging
import os
#DEBUG,INFO,ERROR,WARNING,CRITICAL
logging.basicConfig(
    level=logging.DEBUG,
    format = "[Artists]:%(asctime)s:%(levelname)s:%(message)s"
)
def db_checkfile(dbfile):
   if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
      logging.debug("{a} found and not zero size".format(a=dbfile))
   else:
      logging.error("{a} not found or zero size".format(a=dbfile))

def db_connect(dbfile):
   con = sqlite3.connect(dbfile)
   logging.debug("DB Connected".format())
   return con