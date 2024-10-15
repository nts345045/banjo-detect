#!/bin/bash
# Auth: Barrett Johnson & Nathan Stevens
# Email: bnjo@uw.edu; ntsteven@uw.edu
# Org: Pacific Northwest Seismic Network
# License: GPLv3
# Purpose: This script takes a list of event ID's for the PNSN
#    seismic catalog and fetches the necessary data from the
#    post processing database to generate a QuakeML file for the
#    listed EVIDs.
#
# NOTE: Must be run as USER `rtem`
#
# Script formatting aided by ChatGPT 3.5

usage() {
    echo "Usage: $0 -i input_evid_file -o output_QML_file -n run_name -c config"
    exit 1
}

# Parse command line argument
while getopts "i:o:r" opt; do
    case "$opt" in 
        i) input_file="$OPTARG" ;;
        o) output_file="$OPTARG" ;;
        n) run_name="$OPTARG" ;;
        c) config="$OPTARG" ;;
        *) usage ;;
    esac
done

# Check if all required arguments are provided
# Check if all required arguments are provided
if [ -z "$input_file" ] || [ -z "$output_file" ] || [ -z "$run_name" ] || [ -z "$config" ]; then
    echo "Error: Missing required arguments."
    usage
fi

cfile=$odir/${run_name}_qml_pull.sh
while read -r line; do
    evid=` echo $line | awl ' { print $1 } '`
    ofile=${evid}.xml
    echo "qml -c $config -o $output_file -S $evid"
    echo "Done with $evid"
done < $input_file
# cp pull_quakeml.sh $cfile