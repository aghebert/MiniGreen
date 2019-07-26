#Possibly useful later
from datetime import date
import random

start_dt = date.today().replace(day=1, month=1).toordinal()
end_dt = date.today().toordinal()
random_day = date.fromordinal(random.randint(start_dt, end_dt))
print(random_day)
