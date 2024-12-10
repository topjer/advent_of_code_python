#! /bin/bash

if ! [ -z "$VIRTUAL_ENV" ]; then
  basepath=$(dirname $VIRTUAL_ENV)/src; else
  basepath="."
fi

echo Basepath was set to: $basepath.

year=$1
day=$2

echo You chose year: $year, day: $day

# check for existing of the year folder
#
if ! [ -d $basepath/$year ]; then
  mkdir $basepath/$year
  echo Folder $year has been created.
fi

if [ -d $basepath/$year/day_$day ]; then
  echo The there is already a folder for day: $day in year: $year. Aborting!
  exit 1
fi

echo Copying template

cp -r $basepath/template $basepath/$year/day_$day

echo Downloading input

# Session cookie must be stored in an environment variable for this to work
curl https://adventofcode.com/$year/day/$day/input -H "Cookie: $AOC_COOKIE" >> $basepath/$year/day_$day/input
