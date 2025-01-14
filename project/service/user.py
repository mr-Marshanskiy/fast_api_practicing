from datetime import timedelta, datetime
import os
from jose import jwt


if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as data
else:
    from data import user as data

from passlib.context import CryptContext