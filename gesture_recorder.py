from matplotlib import pyplot as plt
from collections import deque
from threading import Lock, Thread

import myo
import numpy as np
import os
import time

import matplotlib.style as style
from IPython.display import clear_output
from time import sleep
from termcolor import colored

class EmgCollector(myo.DeviceListener):
  def __init__(self, n):
    self.n = n
    self.lock = Lock()
    self.emg_data_queue = deque(maxlen=n)

  def get_emg_data(self):
    with self.lock:
      return list(self.emg_data_queue)

  def on_connected(self, event):
    event.device.stream_emg(True)

  def on_emg(self, event):
    with self.lock:
      self.emg_data_queue.append((event.timestamp, event.emg))


colors=['DarkBlue','DarkGreen','DarkRed','Gold','blue','DarkSlateBlue','red','DarkOrange']


class Plot(object):

  def __init__(self, listener):
    self.n = listener.n
    self.listener = listener


    self.fig = plt.figure()
    self.yaxe=np.zeros(400)
    for i in range(0,8):
      plt.subplot(8,1,i+1)
      plt.ylim([-100, 100])
      plt.plot(self.yaxe,c=colors[i])
    self.graphs=plt.ion()

  def update_plot(self,file):
    emg_data = self.listener.get_emg_data()
    le=400-len(emg_data)
    emg_data=[('',[0,0,0,0,0,0,0,0])]*le+emg_data

    clear_output(wait=True)
    
    for i in range(0,8):
      plt.subplot(8,1,i+1)
      plt.ylim([-100, 100])  
      self.yaxe=np.zeros(400)
      for  j in range(0,400):
        self.yaxe[j]=emg_data[j][1][i]
      plt.plot(self.yaxe,c=colors[i])
    plt.savefig(file+'.jpg')



  def start_plot(self,file):
    while True:
      self.update_plot(file)
      plt.pause(1.0 / 30)
      
  
  def save_plot(self,file,secs):
    sleep(5)
    self.update_plot(file)
    

def record(file,secs):
  myo.init(sdk_path=os.path.join('..', os.getcwd(), 'myo-sdk-win-0.9.0'))
  hub = myo.Hub()
  listener = EmgCollector(400)
  with hub.run_in_background(listener.on_event):
    Plot(listener).save_plot(file,secs)


if __name__=='__main__':
    record('Test_img',2)