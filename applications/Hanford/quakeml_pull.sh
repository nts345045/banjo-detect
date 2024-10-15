#!/bin/bash
# Load the QuakeML configuration file from role `rtem`
config=/app/rtem/db/qml.conf
# Name of the run
run_name=hanford

odir=/home/bnjo/${run_name}/
ifile=//home/bnjo/${run_name}/${run_name}.evids
cfile=${run_name}_qml_pull.sh
while read -r line; do
  eid=` echo $line | awk ' { print $1 } '`
  ofile=${eid}.xml

  qml -c $config -o $odir/$ofile  -S $eid

  echo 'Done with event'
  echo $eid
done < $ifile

cp pull_quakeml.sh $cfile
mv $cfile $odir
