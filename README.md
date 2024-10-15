The pyhton environment I run this in is the envirnment from EQCorrscan using conda conda forge install eqcorrscan ( Just following thier instructions on their website.) Once the environment is set up, you can open the jupyter notebook, and then you should be able to run everything. 

The only caveat in this is that I download the quakeML files from our database (through sarchdb). I don't know if you'd like Benz to go through that, or if it would be easier for me to just grab the events. 
The process by which I download the QuakeML files is:
  Get a list of evids for the events (I usually hop on pnsn.org and do a custom search of the catalog, then download the catalog as a csv. Next I open the csv in excel and copy the entire Evid ID column. I copy that,and paste it in a text file while logged on to sarchdb. 
  Then I run a bash script to loop through the evids, and generate the quakeML files and save them to an output directory. 

  Then I copy (i use scp -r )  that direcroty over to my local machine, where I will run eqcorrscan. 
