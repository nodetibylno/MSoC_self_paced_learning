# coding: utf-8

# In[ ]:


from __future__ import print_function

import sys
import numpy as np
import math
from time import time
import matplotlib.pyplot as plt 

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

PI = 3.1415926536897932384626
numSamples = 89

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPbitFile/r09943019/self_paced/design_1.bit")
    ipcordic = ol.pp4fpga_cordic_0

    xSeq = []
    sin_value = []
    cos_value = []
    zsin_value = []
    zcos_value = []
    timeKernelStart = time()

    for i in range(numSamples):
        radian = (i+1)*PI/180
        xSeq.append(radian)
        
        ipcordic.write(0x10, int(radian * (2**20)))
        
        ipcordic.write(0x00, 0x01)
        while (ipcordic.read(0x00) & 0x4) == 0x0:
            continue

        sin = ipcordic.read(0x18)
        cos = ipcordic.read(0x20)
        sin_value.append(float(sin)/(2**20))
        cos_value.append(float(cos)/(2**20))

        zsin_value.append(math.sin(radian))
        zcos_value.append(math.cos(radian))
        
    error_sin = []
    error_cos = []
    for i in range(numSamples):
        error_sin.append((abs(sin_value[i]-zsin_value[i])/zsin_value[i])*100.0);
        error_cos.append((abs(cos_value[i]-zcos_value[i])/zcos_value[i])*100.0);
    
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
      
    print('Radian \t\t Baseline_sin \t Baseline_cos \t CORDIC_sin \t CORDIC_cos \t error_sin(%) \t error_cos(%)')
    for i in range(numSamples):
        print('%f \t %f \t %f \t %f \t %f \t %f \t %f '%(xSeq[i], zsin_value[i], zcos_value[i], sin_value[i], cos_value[i], error_sin[i], error_cos[i]))
        
    print('Total_Error_Sin=%f, Total_error_Cos=%f'%(sum(error_sin),sum(error_cos)))
    
    plot1 = plt.figure(1)
    plt.title("CORDIC sine waveform")
    plt.xlabel("Radian") 
    plt.ylabel("Value")
    plt.plot(xSeq, zsin_value, 'b-', xSeq, sin_value, 'r-')
    plt.legend(('Baseline sine', 'CORDIC sine'), loc='best', framealpha=0.5, prop={'size': 'large', 'family': 'monospace'})
    plt.grid(True)
    plt.show() # In Jupyter, press Tab + Shift keys to show plot then redo run
    
    plot2 = plt.figure(2)
    plt.title("CORDIC cosine waveform")
    plt.xlabel("Radian") 
    plt.ylabel("Value")
    plt.plot(xSeq, zcos_value, 'b-', xSeq, cos_value, 'r-')
    plt.legend(('Baseline cosine', 'CORDIC cosine'), loc='best', framealpha=0.5, prop={'size': 'large', 'family': 'monospace'})
    plt.grid(True)
    plt.show()

    print("============================")
    print("Exit process")