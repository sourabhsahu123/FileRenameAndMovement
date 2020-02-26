# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
import logging
import threading
import time
import csv
import shutil
import pathlib
def thread_function(name,newname,dirtomove):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", newname)
    #os.rename(name, newname)
    if not os.path.isdir(dirtomove):
        pathlib.Path(dirtomove).mkdir(parents=True, exist_ok=True)
        
    shutil.move(name,os.path.join(dirtomove, newname))  
    
    print(os.path.join(dirtomove, newname))

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
  
    with open('copyfileswithDistrictAndBlock.csv', "r") as f:
        csvreader = csv.reader(f) 
        try:
           # t = f.read().split(',')
            for row in csvreader:
                try:
               # rows.append(row) 
                    print(row)
                    x = threading.Thread(target=thread_function,args=(row[0],row[1]+'_'+row[2]+'_'+row[3],row[1]+'_'+row[2]))
                    logging.info("Main    : before running thread")
                    x.start()
                    #time.sleep(1)
                except Exception as d:
                    print(d)
        except Exception as e:
            print(e)
        #Thread.sleep(1000000)
    #logging.info("Main    : wait for the thread to finish")
    # x.join()
    #logging.info("Main    : all done")
# Function to rename multiple files 

