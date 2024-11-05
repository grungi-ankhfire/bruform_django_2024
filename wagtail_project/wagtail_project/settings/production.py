from .base import *

DEBUG = False

try:
    from .local import *
except ImportError as exception:
    pass
