# BANJO-DETECT
## Barrett Johnson's EQcorrscan implementation for Cascades Volcanoes Template Matching


## Installation
The `conda` environment to run this repository can be installed by running:
```
conda create env -f environment.yml
```
It installs `EQcorrscan` along with suggested supporting libraries, namely `obsplus` and `jupyterlab`.

The python environment I run this in is the environment from EQCorrscan (just following thier instructions on their website)
```
conda create env -n eqcorrscan -c conda-forge install eqcorrscan
``` 

 Once the environment is set up, you can open the jupyter notebook, and then you should be able to run everything. 

The only caveat in this is that I download the quakeML files from our database (through sarchdb). I don't know if you'd like Benz to go through that, or if it would be easier for me to just grab the events. 
The process by which I download the QuakeML files is:
  Get a list of evids for the events (I usually hop on pnsn.org and do a custom search of the catalog, then download the catalog as a csv. Next I open the csv in excel and copy the entire Evid ID column. I copy that,and paste it in a text file while logged on to sarchdb. 
  Then I run a bash script to loop through the evids, and generate the quakeML files and save them to an output directory.   
  Then I copy (i use scp -r )  that direcroty over to my local machine, where I will run eqcorrscan. 


ADDENDUM: Added hanford.evids and quakeml_pull.sh. 
Here is the file I use to pull the QuakeML files from the database on sarchdb, and the evid text file the bash script loops through. the order of steps isn’t explicit in the script, but the way I have it currently is to: 1. make the output directory first, then 2. add the run_name.evids file to that directory. Then  3. run the script.
 Ideally, I would like to have a script where you give it the run_name, it generates the output directory, moves the .evids file into that directory, then loops through the evids and generates the files, but I haven’t gotten to it yet.
  
