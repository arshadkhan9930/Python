import speedtest

wifi = speedtest.Speedtest()

print("Wifi Download Speed is ", wifi.download())
print("Wifi Download Speed is ", wifi.upload())
