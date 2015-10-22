import datetime
from datetime import time
date = datetime.date.today()
now = datetime.datetime.now().time()
heure = now.replace(microsecond=0)
print("Today is %s and it is %s" % (date, heure))
