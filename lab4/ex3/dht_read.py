# Import all the libraries we need to run
from time import sleep
import Adafruit_DHT

# Setup the pins we are connected to
DHTpin = 23

def get_sensor_data():
        hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin, 5, 2) #$
        if hum is not None and temp is not None:
                return (str(hum), str(temp))
        else:
                hum = 0
                temp = 0
                return (str(hum), str(temp))

def main():
    print 'Starting...'
    hum, temp = get_sensor_data()

    print "Temperature: " + str(temp) + " Humidity: " + str(hum)

if __name__ == '__main__':

    main()