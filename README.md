# Bluetooth Light Controller

This repository is a Python Flask server that's used to control a bluetooth light strip. 

It expects a `.env` file with three parameters set:
1. `MAC_ADDRESS` - the MAC address of the light strip
2. `PORT` - the port for the Flask server
3. `HOST` - the host address for the Flash server