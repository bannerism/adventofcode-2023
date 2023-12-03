#!/bin/bash

day=${1:-`date +%-d`}
echo downloading Advent of Code day $day 2023 inputs...
filename=./data/"$day"_inputs.txt
touch $filename
aocd $day 2023 > $filename 
