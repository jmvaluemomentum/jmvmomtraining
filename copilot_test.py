#!/usr/bin/env python3

import time
from datetime import timedelta

try:
    import psutil
except ImportError:
    print("This script requires the 'psutil' package.")
    print("Install it with: pip install psutil")
    exit(1)

boot_time = psutil.boot_time()
uptime_seconds = time.time() - boot_time

print(f"System Uptime: {timedelta(seconds=int(uptime_seconds))}")
