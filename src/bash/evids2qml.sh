#!/bin/bash

# conf=/app/rtem/db/qml.conf
# run=MtBaker
# output=/app/rtem/tmp_quakeml
# input=/home/ntsteven/MtBaker/evids.txt

# if [ -d $output ]; then
#     echo "Writing to existing dir: $output"
# else
#     echo "Creating output dir: $output"
#     mkdir -p $output

# qml -c $conf -i $input -o $output/$run.xml -S


echo "making subset evid list for Mt. Baker events with <= 20km offset from summit"
awk -F, '$20 <= 20 { print $1 }' ./MtBaker_50km_radius_origins.csv > ./MtBaker_evids_20km.txt
echo "generating QuakeML"
qml -i ./MtBaker_evids_20km.txt -o ./MBS_20km_query.xml -c /app/rtem/db/qml.conf -S

rm ./MtBaker_evids_20km.txt