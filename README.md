# Syncthing-Plus
An addon to the existing Syncthing integration to home assistant  that adds a binary sensor to report the connection status of devices.
This intergration is heavily based upon the existing Syncthing intergration by [@Zhulik](https://github.com/zhulik). 

This intergration connects to a Syncthing server using the API key found in the Syncthing GUI, which then reports the device conneciton status on a 2 minute interval. The conneciton status is reported under a binary sensor.
You can utilize this intergration to see if a server's connected clients are online or offline, and using additional HA templates you can determine if a sensor has been offline for a prolonged status indicating that there is a problem. 
