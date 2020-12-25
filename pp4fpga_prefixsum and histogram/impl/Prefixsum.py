
# coding: utf-8

# In[ ]:


from __future__ import print_function

import sys
import numpy as np
from time import time
import matplotlib.pyplot as plt 

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

SIZE = 128

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPbitFile/r09943019/self_paced/design_1.bit")
    IP = ol.prefixsum_hw_0

    inBuffer0 = allocate(shape=(SIZE,), dtype=np.int32)
    outBuffer0 = allocate(shape=(SIZE,), dtype=np.int32)

    for i in range(SIZE):
        inBuffer0[i] = int(i)
        
    prefixsum_sw = np.arange(SIZE)
    prefixsum_sw = np.cumsum(prefixsum_sw)
    
    timeKernelStart = time()
    
    IP.write(0x10, inBuffer0.device_address)
    IP.write(0x18, outBuffer0.device_address)
    IP.write(0x00, 0x01)
    while (IP.read(0x00) & 0x4) == 0x0:
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
      
    print(prefixsum_sw)
    print(outBuffer0)
    if(np.array_equal(prefixsum_sw,outBuffer0)):
        print("Simulation PASS")
    else:
        print("Simulation FAIL")

    print("============================")
    print("Exit process")
