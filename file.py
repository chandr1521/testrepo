import pandas as pd
chunk_size=5
batch_no=1
for chunk in pd.read_csv('/home/chanda/Pictures/JUMO_DUMP/JUMO_DUMP.csv',chunksize=chunk_size, delimiter=';', skiprows=0, low_memory=False,):
    chunk.to_csv('chunk'+str(batch_no)+'.csv',index=False)
    batch_no=1

#df = pd.read_csv('/home/chanda/Pictures/JUMO_DUMP/JUMO_DUMP.csv', delimiter=',', skiprows=0, low_memory=False,nrows=5)
print (chunk)


