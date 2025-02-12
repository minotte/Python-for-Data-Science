#!/usr/bin/env python3

import time
from datetime import date, timedelta

today = date.today()
now = time.time()

print(f"Seconds since January 1, 1970: {now[1]},{now[2 : 6]}, or {format(now,'.2e')} in scientific notation")
print(today.strftime("%d %B %Y"))
