
import sys
import httplib, urllib #https/http request
import time
import Adafruit_DHT
class rq:
    sleep = 60 # how many seconds to sleep between posts to the channel
    key = 'Q7C4A7DWEM3ERA57'  # Thingspeak channel to update

    #Report Raspberry Pi internal temperature to Thingspeak Channel
    def thermometer(self,sensor):
        while True:
            #Calculate CPU temperature of Raspberry Pi in Degrees C
            temp = sensor
            params = urllib.urlencode({'field1': temp, 'key': 'Q7C4A7DWEM3ERA57'}) 
            headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = httplib.HTTPConnection("api.thingspeak.com:80")
            try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print temp
                print response.status, response.reason
                data = response.read()
                conn.close()
            except:
                print "connection failed"
            break



if __name__ == '__main__':
    while True:
        sensor_args = { '11': Adafruit_DHT.DHT11,
                        '22': Adafruit_DHT.DHT22,
                        '2302': Adafruit_DHT.AM2302 }
        if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
            sensor = sensor_args[sys.argv[1]]
            pin = sys.argv[2]
        else:
            print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
            print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
            sys.exit(1)


        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            Mrq = rq()
            Mrq.thermometer(humidity)
            time.sleep(2)
        else:
            print('Failed to get reading. Try again!')
            sys.exit(1)
