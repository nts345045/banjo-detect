import time
import numpy as np
from obspy import UTCDateTime as utcdt
from obspy.clients.fdsn import Client
client = Client('IRIS')
from eqcorrscan import Tribe

def run_detections():

    def chunky(start,end,plen):
        process_len=plen
        start_time = utcdt(start)
        end_time = utcdt(end)
        chunks = []
        chunk_start = start_time
        while chunk_start < end_time:
            chunk_end = chunk_start + process_len
            if chunk_end > end_time:
                chunk_end = end_time
            chunks.append((chunk_start, chunk_end))
            chunk_start += process_len
        return chunks

    def oneTribe(t):
        tribe = Tribe()
        tribe.read(filename='/Users/bnjo/home/bnjo/hood2/detect/TRIBES/'+t)
        tribe = tribe_check(tribe)
        return tribe

    def tribe_check(tribe):
        tribe = check_process_len(tribe)
        tribe = check_template_len(tribe)
        return tribe

    def check_process_len(tribe):
        bad=[]
        for i in range(len(tribe.templates)):
            template = tribe.templates[i]
            if template.process_length != 3600.0:
                name = template.name
                bad.append(i)
        bad = np.flip(bad)
        for b in bad:
            tribe.remove(tribe.templates[b])
        return tribe

    def check_template_len(tribe):
        bad2=[]
        for i in range(len(tribe.templates)):
            template = tribe.templates[i]
            tst = template.st
            for tr in tst:
                if tr.stats.npts != 300:
                    bad2.append(i)
                    print('different size',i,tr.stats.npts, template.name,tr.stats.station,tr.stats.channel)
        bad2=np.flip(bad2)
        for b in bad2:
            tribe.remove(tribe.templates[b])
        return tribe


    def lets_party_with_client(tribe,hour,thresh):
        party= tribe.client_detect(
                    client=client,
                    starttime = utcdt(hour),
                    endtime = utcdt(hour)+3600,
                    threshold = thresh,
                    threshold_type = "MAD",
                    trig_int = 6.0,
                    ignore_bad_data = True,
                    return_stream=False,
                    concurrency='multiprocess',
                    parallel = True,
                    num_cores = 9,
                    concurrent_processing=True,
            group_size = 9)
        return party

    def tribe_detection(t,hour,tname):
        year = utcdt(hour).year
        jday = utcdt(hour).julday
        hr = utcdt(hour).hour
        hr = str(hr).zfill(2)
        jday = str(jday).zfill(3)
        party_name = tname+"_"+str(year)+"_"+str(jday)+"_"+str(hr)
        party_path = '/Users/bnjo/home/bnjo/hood2/detect/PARTIES/P/'
        party_out = party_path+party_name
        thresh= 9
        party=lets_party_with_client(tribe,hour,thresh=thresh)
        return party,party_out

    def party_clean(party,party_out):
        if len(party)>=1:
            party=party.decluster(trig_int=6.0, timing='detect',min_chans=5)
            party.write(
                party_out,
                format='tar',
                write_detection_catalog=True,
                catalog_format='QUAKEML',
                overwrite=True)
        return party

    def detection(t,hour,tname):
        party,party_out = tribe_detection(t,hour,tname)
        party = party_clean(party,party_out)
        return party



    a = utcdt(2019,1,7,4,0,0)
    b = utcdt(2019,3,1,0,0,0)
    t = 'hood2-3600R695.tgz'
    tribe_name = t.split(sep='.')[0]
    tribe=oneTribe(t)
    duration = chunky(a,b,3600)
    for hour in duration:
        hr = utcdt(hour[0])
        try:
            party = detection(tribe,hr,tribe_name)
        except:
            print(f'something is up {hr}')
        continue
if __name__ == '__main__':
    
    
    import time
    start_time = time.time()
    run_detections()
    end_time = time.time()
    print("10-15-20 to 1-1-21 took ", (time.time() - start_time)/60, " minutes to run")
    print("10-15-20 to 1-1-21 took ", ((time.time() - start_time)/60)/60, " hours to run")
    print("10-15-20 to 1-1-21 took ", (((time.time() - start_time)/60)/60)/24, " days to run")
