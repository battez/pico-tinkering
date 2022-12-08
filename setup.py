import network
import secrets as s
import time
print(s.secrets['ssid'])

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(s.secrets['ssid'], s.secrets['password'])

print("connected ", wlan.isconnected())
time.sleep(2)
print("seconds later...connected ", wlan.isconnected())