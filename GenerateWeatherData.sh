#!/bin/ksh
#######################################################
#Author: Wang Cheng
#Date: 19 June 2016
#Des: Using WeatherGenerator.py python program generates
#all cities weather information.
#######################################################

##################################################################################
#Title           :GenerateWeatherData.sh
#Description     :
#
#                : This is to generate weather data
#Author          :Mohamed Asimulla S
#Date            :22/04/2017
#Version         :1.0
#Usage           :GenerateWeatherData.sh
#Notes           :
#Limitation:     :Desgined to work without any parameter
#                :
##################################################################################

#Variable Initialization

ENV=""
HOSTNAME=`hostname`
IPADRESS=`grep $HOSTNAME /etc/hosts |grep "^[^#;]" |awk '{print $1}'`
USERID=`whoami`
LOGNAME=$HOSTNAME
LOGDIR=~/
TMP=${LOGDIR}/${LOGNAME}.${pid}
TMP2=${LOGDIR}/${LOGNAME}.${pid}.$$
LOCATIONS_LIST="`./readTagValue.sh Location.xml  Weather_location`"
#Overtite XML value for testing it might be shell depend
#LOCATIONS_LIST=" Adelaide Perth London Melbourne Moscow Ottawa Paris Seoul Shanghai Singapore Sydney Tokyo Toronto"
set -A LOCATIONS_LIST Adelaide Perth London Melbourne Moscow Ottawa Paris Seoul Shanghai Singapore Sydney Tokyo Toronto
##################################################################################
#Error Handling
##################################################################################
Clean_Up()
{

        # Perform program exit housekeeping
        # Optionally accepts an exit status
        exit 1
}


trap Clean_Up SIGHUP SIGINT SIGTERM


##################################################################################
#Main Function Call
##################################################################################

i=0
while [ $i -lt ${#LOCATIONS_LIST[*]} ]
do
echo ${LOCATIONS_LIST[$i]}
python GenerateWeather.py ${LOCATIONS_LIST[$i]}
(( i=i+1 ))
done

#this required to ensure the process has terminated the program normally
exit 0
