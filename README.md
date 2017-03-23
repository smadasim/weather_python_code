###The code in this example demonstrates how to:

1. How to invoke python script from Unix Shell script.
2. Connect to a Python API's' to get weather data 
3. Store the data into output file Out_Weather_Report.txt .

## Getting Started

These instructions will get your project up and running on your device for development and testing purposes.

### Prerequisities

Python and its depend modules are given below
1. geopy
2. geocoder

###Note :This is tested on Mac OSx machine .However it will work on any favour of unix and Linux Operating systems.It is also tested on EC2 Linux AMI on AWS cloud .

##Grant Required permissions

chmod +x GenerateWeather.py
chmod +x GenerateWeatherData.sh

##Run Unix Shell script  
./GenerateWeatherData.sh



```
Output 

sh-3.2# ./GenerateWeatherData.sh
Adelaide
...
Perth
...
London
...
Melbourne
...
Moscow
...
Ottawa
...
Paris
...
Seoul
...
Shanghai
...
Singapore
...
Sydney
...
Tokyo
...
Toronto
...
sh-3.2# 
sh-3.2# ls -plrt
total 1520
-rwxrwxrwx@ 1 Yaqoob  staff     888 Mar 23 00:12 readTagValue.sh
-rwxrwxrwx@ 1 Yaqoob  staff   14412 Mar 23 22:49 GenerateWeather.py
-rwxrwxrwx  1 root    staff     265 Mar 23 23:04 Location.txt
-rwxrwxrwx@ 1 Yaqoob  staff     277 Mar 23 23:17 Location.xml
-rwxrwxrwx@ 1 Yaqoob  staff    2103 Mar 23 23:20 GenerateWeatherData.sh
-rwxrwxrwx  1 root    staff     830 Mar 23 23:20 Out_Weather_Report.txt
-rw-r--r--@ 1 Yaqoob  staff    6148 Mar 23 23:41 .DS_Store
-rwxrwxrwx@ 1 Yaqoob  staff  725702 Mar 23 23:45 Assignment.docx
-rw-r--r--@ 1 Yaqoob  staff    1068 Mar 24 00:03 README.md
sh-3.2# date
Fri Mar 24 00:03:55 AEDT 2017
sh-3.2# whoami
root
sh-3.2# 
sh-3.2# cat Out_Weather_Report.txt
Toronto|43.65,-79.38,86|2017-03-23T03:20:16Z|Rain|6.4|827.6|69
Tokyo|34.23,139.29,-302|2017-03-23T03:20:15Z|Rain|16.2|1007.4|93
Seoul|37.57,126.98,40|2017-03-23T03:20:13Z|Snow|22.2|1128.0|69
Singapore|1.29,103.85,8|2017-03-23T20:20:14Z|Rain|21.6|823.4|71
Paris|48.86,2.35,37|2017-03-23T10:20:12Z|Rain|12.9|1020.8|69
Moscow|55.75,37.62,138|2017-03-23T09:20:10Z|Rain|15.4|1145.8|69
Shanghai|31.23,121.49,10|2017-03-23T20:20:13Z|Sunny|12.7|953.4|78
Ottawa|45.42,-75.69,71|2017-03-23T16:20:11Z|Snow|18.9|1039.9|51
Melbourne|-37.81,144.96,35|2017-03-23T23:20:09Z|Rain|-9.9|816.8|76
Perth|-31.95,115.86,14|2017-03-23T04:20:07Z|Rain|28.7|851.4|89
Sydney|-33.85,151.22,3|2017-03-23T23:20:15Z|Snow|-7.2|860.0|74
London|51.51,-0.13,19|2017-03-23T11:20:08Z|Rain|3.3|855.9|55
Adelaide|-34.93,138.6,44|2017-03-23T22:50:06Z|Snow|35.8|1041.8|68
sh-3.2# 
