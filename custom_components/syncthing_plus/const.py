"""Constants for the syncthing integration."""

from datetime import timedelta

DOMAIN = "syncthing_plus"

DEFAULT_VERIFY_SSL = True
DEFAULT_URL = "http://127.0.0.1:8384"

SCAN_INTERVAL = timedelta(seconds=120)
