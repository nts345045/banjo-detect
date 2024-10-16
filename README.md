# BANJO-DETECT
## Barrett Johnson's Earthquake Template Matching Workflow for the PNSN

Repo Manager: Barret Johnson (bnjo@uw.edu)
Contributor: Nate Stevens (ntsteven@uw.edu)

## General Workflow  
1) Get PNSN catalog event ID's from `archdb` or `sarchdb`  
2) Create QuakeML files from `archdb`/`sarchdb` for desired EVIDs  
3) Load QuakeML file(s) into ObsPy `Catalog` objects & curate picks desired for template generation  
4) Use QuakeML files to generate an EQcorrscan `Tribe` object (Template Generation)  
5) Use EQcorrscan `Tribe` objects to detect for new events (Detection)  


## Python Environment Installation
The `conda` environment to run this repository can be installed by running:
```
conda create env -f environment.yml
```
It installs `EQcorrscan` along with suggested supporting libraries, namely `obsplus` and `jupyterlab`.

## Applications

### Hanford
Example *.evids file input to `src/bash/quakeml_pull.sh` for generating QuakeML files from the PNSN archival database

The process by which I download the QuakeML files is:
  Get a list of evids for the events (I usually hop on pnsn.org and do a custom search of the catalog, then download the catalog as a csv. Next I open the csv in excel and copy the entire Evid ID column. I copy that,and paste it in a text file while logged on to sarchdb. 
  Then I run a bash script to loop through the evids, and generate the quakeML files and save them to an output directory.   
  Then I copy (i use scp -r )  that direcroty over to my local machine, where I will run eqcorrscan. 

ADDENDUM: Added hanford.evids and quakeml_pull.sh. 
Here is the file I use to pull the QuakeML files from the database on sarchdb, and the evid text file the bash script loops through. the order of steps isn’t explicit in the script, but the way I have it currently is to: 1. make the output directory first, then 2. add the run_name.evids file to that directory. Then  3. run the script.
#### TODO
 Ideally, I would like to have a script where you give it the run_name, it generates the output directory, moves the .evids file into that directory, then loops through the evids and generates the files, but I haven’t gotten to it yet.

### Mt. Adams
Example template generation workflow from B. Johnson in the form of a Jupyter Notebook

### Mt. Hood
Example template detection workflow from B. Johnson in the form of a python script




  
