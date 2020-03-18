#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/darian/")
sys.path.insert(0,"/var/www/darian/darian/")

import logging
logging.basicConfig(stream=sys.stderr)

from darian import app as application

