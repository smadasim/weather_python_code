#!/bin/sh
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
filePath=$1 #XML file path
tagName=$2  #Tag name to fetch values
echo "`awk '!/<.*>/' RS="<"$tagName">|</"$tagName">" $filePath`"
