from collections import defaultdict
from pandas import DataFrame,Series
from matplotlib import pylab

recode = [line.strip().replace("\n","").split("\t") for line in  open("../source/source.txt").readlines()[1:]]
frame = DataFrame(recode)
clean_tz = frame[1].fillna('Missing')
clean_tz[clean_tz == ''] = 'unknown'
tz_count = clean_tz.value_counts()
print('*************************')
print(frame)
print('*************************')
tz_count[:].plot(kind = 'barh' , rot = 0)