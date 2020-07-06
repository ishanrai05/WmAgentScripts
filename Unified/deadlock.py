from utils import cacheInfo
from utils import moduleLock
from utils import UnifiedLock
import glob
import os
import socket

print("cleaning unified locks")
UL = UnifiedLock(acquire=False)
UL.deadlock()

print("cleaning module locks")
# get rid of deadlock in mongodb
mlock = moduleLock(component='deadlock')
mlock.check()

print("purging cache info")
cache = cacheInfo()
cache.purge()
