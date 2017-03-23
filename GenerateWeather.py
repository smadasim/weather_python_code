#==============================================================================
#Title           :GenerateWeatherData.py
#Description     :
#
#                :This is used to generate weather data using python
#Author          :Mohamed Asimulla S
#Date            :22/04/2017
#Version         :1.0
#Usage           :GenerateWeather.py <Location>
#Output          :Out_Weather_Report.txt
#Notes           :
#Limitation:     :Desgined to work with one input variable
#                :Generate weather information based on location
#                :Melbourne
# List of locations details : Adelaide, Perth, London, Melbourne,Moscow, Ottawa, Paris, Seoul, Shanghai, Singapore, Sydney, Tokyo,Toronto
#==============================================================================
import time
import random
import sys
import string
import os
import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geocoder
from random import choice
from time import sleep
import pytz



'''
Function: to Initialise  weather condition
'''

def init_weather_condition(temperature_range=[],location_temperature=[],humidity_range=[],location_humidity=[]):

    # Range of temperature, simulate cold, warm and hot areas temperature ranges. Using dictionary.
    temperature_range['cold']="-11,24"
    temperature_range['warm']="12,30"
    temperature_range['hot']="18,40"


    # Type of locations. Classify locations areas by cold, warm & hot. Using dictionary.
    location_temperature['Adelaide']="hot"
    location_temperature['Perth']="hot"
    location_temperature['London']="cold"
    location_temperature['Melbourne']="cold"
    location_temperature['Moscow']="cold"
    location_temperature['Ottawa']="cold"
    location_temperature['Paris']="cold"
    location_temperature['Seoul']="cold"
    location_temperature['Shanghai']="warm"
    location_temperature['Singapore']="hot"
    location_temperature['Sydney']="cold"
    location_temperature['Tokyo']="warm"
    location_temperature['Toronto']="cold"


    # Range of humidity, simulate seaside & non-seaside areas humidity. Using dictionary.
    humidity_range['seaside']="65,100"
    humidity_range['notseaside']="33,80"

    # Type of locations. Classify locations areas by seaside & non-seaside. Using dictionary.
    location_humidity['Adelaide']="seaside"
    location_humidity['Melbourne']="notseaside"
    location_humidity['Brisbane']="notseaside"
    location_humidity['Sydney']="seaside"
    location_humidity['Perth']="seaside"
    location_humidity['London']="notseaside"
    location_humidity['Miami']="notseaside"
    location_humidity['Moscow']="notseaside"
    location_humidity['New_York']="notseaside"
    location_humidity['Ottawa']="notseaside"
    location_humidity['Paris']="notseaside"
    location_humidity['Seoul']="notseaside"
    location_humidity['Shanghai']="seaside"
    location_humidity['Singapore']="seaside"
    location_humidity['Tokyo']="seaside"
    location_humidity['Toronto']="notseaside"


'''
Function: to generator lantitude & longtitude based on city name
'''
def perform_geocode(geolocator,address):
    try:
        if "_" in address:
            address = string.replace(address,'_',' ')
        sleep(1)
        return geolocator.geocode(address,timeout=None)
    except GeocoderTimedOut:
        print ("GeoPy API policy restriction on query frequency. Wait 1s to re-try.")
        return perform_geocode(geolocator,address)
    except:
        print ("Error: geocode has failed on input %s with message %s" %(address, sys.exc_info()[0]))
        exit(3)

'''
Function: to Initialise  location values
'''

def  init_location_values(location_label=[],timezone_location=[],city=[]):

    '''
    Initialise location labels
    '''
    location_label['Adelaide']="Adelaide"
    location_label['Perth']="Perth"
    location_label['London']="London"
    location_label['Melbourne']="Melbourne"
    location_label['Moscow']="Moscow"
    location_label['Ottawa']="Ottawa"
    location_label['Paris']="Paris"
    location_label['Seoul']="Seoul"
    location_label['Shanghai']="Shanghai"
    location_label['Singapore']="Singapore"
    location_label['Sydney']="Sydney"
    location_label['Tokyo']="Tokyo"
    location_label['Toronto']="Toronto"

    '''
    Initialise TimeZone details
    '''
    timezone_location['Adelaide']="Australia/Adelaide"
    timezone_location['Perth']="Etc/GMT+8"
    timezone_location['London']="Etc/GMT+1"
    timezone_location['Melbourne']="Australia/Melbourne"
    timezone_location['Moscow']="Etc/GMT+3"
    timezone_location['Ottawa']="Etc/GMT-4"
    timezone_location['Paris']="Etc/GMT+2"
    timezone_location['Seoul']="Etc/GMT+9"
    timezone_location['Shanghai']="Asia/Shanghai"
    timezone_location['Singapore']="Asia/Singapore"
    timezone_location['Sydney']="Australia/Sydney"
    timezone_location['Tokyo']="Etc/GMT+9"
    timezone_location['Toronto']="Etc/GMT+9"

    weather_data_structure=location_label.get(city) + "|"
    return weather_data_structure

'''
Function: to get  location
'''

def get_location(weather_data_structure=[],location_label=[],city=[]):

    '''
    Begin to prepare the  weather data structure
    '''

    weather_data_structure=location_label.get(city) + "|"
    return weather_data_structure

'''
Function: to get geo location
'''

def get_geolocaiton(weather_data_structure=[],Out_Location_File=[],city=[]):

    '''
    In order to generate city's lantitude and longtitude information.
    python GeoPy package is required.
    '''
    # Get this python program full path to let use can program anywhere.

    absolute_directory_path =  os.path.dirname(os.path.abspath(sys.argv[0]))
    geolocations_file_data = absolute_directory_path + Out_Location_File


    # Initial geolocation dictionary to store written data.

    geolocaiton = {}

    '''
     Instead of calling GeoPy use policy everytime
     we will write location into a file. In the next
     query request, the program will read the data from the file directly.
     Format in the file: [city],[lantitude],[longtitude]
    '''

    # Check whether the file exist or not
    if os.path.isfile(geolocations_file_data):
        filereaderlocation = open(geolocations_file_data,'r')
        for line in filereaderlocation:
            temp = line.strip().split(',')
            geolocaiton[temp[0]] = temp[1] + "," + temp[2]
        filereaderlocation.close()

    # Check whether the input city exists in the location file.
    if not geolocaiton.has_key(city):
        filewriterlocation = open(geolocations_file_data,'a')
        geolocator = Nominatim()
        location = perform_geocode(geolocator,city.lower())
        lan = location.latitude
        lon = location.longitude
        filewriterlocation.write(city + "," + str(round(float(lan),2)) + "," + str(round(float(lon),2)) + "\n")
        filewriterlocation.close()
    else:
        location = geolocaiton.get(city)
        lan = location.split(',')[0]
        lon = location.split(',')[1]


    # Write into the  weather data structure
    weather_data_structure =  weather_data_structure + str(round(float(lan),2)) + "," + str(round(float(lon),2)) + ","

    '''
    The following part generate city's altitude.
    geocoder package required.
    '''

    g = geocoder.elevation([lan,lon])
    alt = g.meters

    # Write into the  weather data structure
    weather_data_structure =  weather_data_structure + str(int(alt)) + "|"
    return weather_data_structure

'''
Function: to get local time
'''

def get_local_time(weather_data_structure=[],timezone_location=[],city=[]):

    '''
    Get current time using standard format
    '''
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts,pytz.timezone(timezone_location.get(city))).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Write into the  weather data structure
    weather_data_structure =  weather_data_structure + st + "|"
    return weather_data_structure


'''
Function: to get weather  condition
'''

def get_weather_condition(weather_data_structure=[],conditions=[]):
    '''
    Randomly get weather conditions
    '''
    weather_data_structure =  weather_data_structure + choice(conditions) + "|"

    return weather_data_structure
'''
Function: to get temperature
'''

def get_temperature( weather_data_structure=[],temperature_range=[],location_temperature=[],city=[]):

    '''
    Randomly get temperature details
    '''
    range_temperature = temperature_range.get(location_temperature.get(city))
    low_temperature = int(range_temperature.split(',')[0])
    high_temperature = int(range_temperature.split(',')[1])
    weather_data_structure =  weather_data_structure + str(round(random.uniform(low_temperature,high_temperature),1)) + "|"
    return weather_data_structure

'''
Function: to get pressure
'''

def get_pressure( weather_data_structure=[]):

    '''
    Randomly get pressure data
    '''
    # Range of pressure, high & low as int.
    high=1200
    low=800
    weather_data_structure =  weather_data_structure + str(round(random.uniform(low,high),1)) + "|"
    return weather_data_structure

'''
Function: to get humidity
'''

def get_humidity( weather_data_structure=[],humidity_range=[],location_humidity=[],city=[]):

    '''
    Randomly get humidity data
    '''
    range_humidity = humidity_range.get(location_humidity.get(city))
    low_humidity = float(range_humidity.split(',')[0])
    high_humidity = float(range_humidity.split(',')[1])
    weather_data_structure =  weather_data_structure + str(int(random.uniform(low_humidity,high_humidity)))
    return weather_data_structure

'''
Function: to prepare in memory data structures
'''

def prepareData(Out_Location_File,temperature_range=[], location_temperature=[],humidity_range=[],location_humidity=[],location_label=[],timezone_location=[],city=[],weather_data_structure=[],conditions=[]):

    # Get location data
    weather_data_structure_Loc=get_location(weather_data_structure,location_label,city)

    # Get city's lantitude and longtitude.
    weather_data_structure_geo=get_geolocaiton(weather_data_structure_Loc,Out_Location_File,city)

    # Get current time using standard format
    weather_data_structure_time=get_local_time(weather_data_structure_geo,timezone_location,city)

    # Get Weather Condition
    weather_data_structure_cond=get_weather_condition(weather_data_structure_time,conditions)

    # Get Temperature
    weather_data_structure_temp=get_temperature(weather_data_structure_cond,temperature_range,location_temperature,city)

    # Get Pressure
    weather_data_structure_press=get_pressure(weather_data_structure_temp)

    # Get humidity
    weather_data_structure_humidit=get_humidity(weather_data_structure_press,humidity_range,location_humidity,city)

    return weather_data_structure_humidit


'''
Function: to flush memory data structure into a file
'''
def writeData_to_File(Out_Weather_Report_File, weather_data_structure=[],location_label=[],city=[]):

    weather_infomation = {}
    absolute_directory_path =  os.path.dirname(os.path.abspath(sys.argv[0]))

    # Specify the file name and path of the output
    file_path = absolute_directory_path + Out_Weather_Report_File
    if os.path.isfile(file_path):
        filereader = open(file_path,'r')
        '''
        Check if there is any historic city weather information data that can be used.
        '''
        for line in filereader:
            temp =  line.split('|')
            weather_infomation[temp[0]] = line.strip()
        # Update the latest information
        weather_infomation[location_label.get(city)] =  weather_data_structure
        #close the file reader pointer
        filereader.close()
    # Writing data into table format
    filewriter = open(file_path,'w')
    if len(weather_infomation.keys()) == 0:
        filewriter.write( weather_data_structure + "\n")
    else:
        for key in weather_infomation:
            filewriter.write(weather_infomation[key] + "\n")
    #close the file writer pointer
    filewriter.close()

'''
Function: to release rescources to OS
'''
def cleanup():
    print("...")

def is_input_args_valid(city=[]):
    # Verify the arguments
    if len(sys.argv) != 2:
        print ("The no. of arguments specified are not correct. Please check and retry.")
        print ("Usage: python WeatherGenerator.py <Location>")
        print ("List of locations: Adelaide, Perth, London, Melbourne, Moscow, Ottawa, Paris, Seoul, Shanghai, Singapore, Sydney, Tokyo,Toronto")
        exit(1)

    # List of locations, which can generate weather report
    list_of_loctions=['Adelaide', 'Perth', 'London', 'Melbourne', 'Moscow', 'Ottawa', 'Paris', 'Seoul', 'Shanghai', 'Singapore', 'Sydney', 'Tokyo','Toronto']


    # Verify the city, which user is going to input
    city=sys.argv[1]

    if not city in list_of_loctions:
        print ("%s is not recognized. Please choose from list of locations specified below." %city)
        print ("Usage: python WeatherGenerator.py <Location>")
        print ("List of valid locations: Adelaide, Perth, London, Melbourne, Moscow, Ottawa, Paris, Seoul, Shanghai, Singapore, Sydney, Tokyo,Toronto")
        exit(2)
    return city

'''
Main Function:
'''
def main():


    #input file
    InputFile = ""

    #Output  files
    Out_Weather_Report_File = "/Out_Weather_Report.txt"
    Out_Location_File = "/Location.txt"

    # Initalise data variables
    conditions=['Rain','Snow','Sunny']
    temperature_range={}
    location_temperature={}
    humidity_range={}
    location_humidity={}
    location_label={}
    timezone_location={}
    city=[]

    #Validate input args
    city=is_input_args_valid(city)

   # Initalise  the data set.
    weather_data_structure=init_location_values(location_label,timezone_location,city)

    # Initalise  the data set.
    init_weather_condition(temperature_range,location_temperature,humidity_range,location_humidity)

    # Prepare  the data set with in memory data structure
    weather_data_structure_result=prepareData(Out_Location_File,temperature_range, location_temperature,humidity_range,location_humidity, location_label,timezone_location,city, weather_data_structure,conditions)

    # Load  the data set to a Persistant file system
    writeData_to_File(Out_Weather_Report_File,weather_data_structure_result,location_label,city)

    #release the OS resources
    cleanup()

main()
