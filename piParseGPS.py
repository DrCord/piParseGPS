import serial
import json
ser = serial.Serial('/dev/ttyACM0', 115200)
while 1:
    parsed_data = json.loads(ser.readline())
    print(parsed_data['sensor'])
    print(parsed_data['time'])
    print(parsed_data['longitude'])
    print(parsed_data['latitude'])
    print(parsed_data['altitude'])
    print(parsed_data['speed'])
    print(parsed_data['course'])
    print('\n')
