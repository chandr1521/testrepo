import pandas as pd
chunk_size=5
batch_no=1
for chunk in pd.read_csv('DUMP.csv',chunksize=chunk_size, delimiter=';', skiprows=0, low_memory=False,):
    chunk.to_csv('chunk'+str(batch_no)+'.csv',index=False)
    batch_no=1
print (chunk)


