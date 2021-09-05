import os
from termcolor import colored
import cv2
from fastai import *
from fastai.vision.all import *
import gesture_recorder as gr
from time import sleep
from IPython.display import clear_output
from clear import clear

num_rcdings=10

grs=open('gestures.txt','r')
gestures=grs.read().split(',')
clear()
print(colored("Gestures :",'blue'))
print(gestures)
print(colored(f"The gesture record will strart in 10 seconds, with {num_rcdings} recordings per gesture",'cyan'))
sleep(5)
clear()




for gesture in gestures:
    try:
        os.mkdir('dataset/'+gesture)
    except Exception:
        pass

    cont=36
    for i in range(0,num_rcdings):
        
        print(colored(f'Do a {gesture} in 5 seconds','blue'))
        sleep(1)
        print(colored("4 seconds",'yellow'))
        sleep(1)
        print(colored("3 seconds",'yellow'))
        sleep(1)
        print(colored("2 seconds",'red'))
        sleep(1)
        print(colored("1 seconds",'red'))
        sleep(1)
        print(colored('Recording ... ','blue'))

        gr.record('dataset/'+gesture+'/'+str(cont),3)
        cont=cont+1
        clear()
        print(colored(f"Gesture recorded : {gesture}",'green'))
        sleep(1)
        clear()