#!/usr/bin/python

import subprocess
import os
from datetime import datetime

lt  = datetime.now()
logname = os.path.join('logs',str(lt).replace(' ','_'))
log = open(logname,'w')


inputimage = 'images/dicom/foot.mha'
outdir = 'out'

params = [(0.011,0.232),
          (0.005,0.200)]

# get lowerThreshold and outputScaleLevels
for lt,osl in params:
  outname = ('foot_lt-%f_osl-%f.mha' % (lt,osl))
  outpath = os.path.join(outdir,outname)
  if os.path.exists(outpath):
    print '[-] ERROR: %s already exist' % outpath
  else:
    command = ('./bin/watershedExamples/WatershedSegmentation2 %s %s %f %f'
               % (inputimage,outpath,lt,osl))
    log.write(command + '\n')
    subprocess.call(command,stdout=log,stderr=log)
