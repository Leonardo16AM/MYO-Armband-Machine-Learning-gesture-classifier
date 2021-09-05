
# MYO Armband Machine Learning gesture classifier
Myo Armband Gesture classifier with Machine Learning. I used Fastai for simplicity and converted EMG signals from MYO to pictures and then proccessed with a Convolutional Neural Network to classify between gestures.

----  
## Usage:
First of all install Thalmic Labs Myo Controller.  
Then, if you want to train with your own gestures (recomended), add the gestures name to the file `gestures.txt` (comma separated).  

Run `gesture_data_recorder.py` and follow the steps to record the dataset of gestures, you can change the number of training records for gesture just changing `num_rcdings` (recomended more than 30, you can also duplicate images but not recomended).  

Then run all the cells from `trainer.ipynb`. If you want to display pictures of the gestures once recognised add them to the folder `gest_images` and change the last cell from `trainer.ipynb`. 

----
### Files:
 - `gesture_recorder.py`: Contains the function ```record(file,secs)```, it saves an image of the plot of the last 3 seconds of an interval of `secs` seconds with name `file`.jpg .
 - `gesture_data_recorder.py`: Do the process of recording data to the dataset for every gesture.
 - `train.ipynb` trains the CNN and in the last cell can classify gestures (later this will be in other file and will run in real time).

---
### Self recomendations for the future:
  - Don`t use a CNN to classify gestures, they work, but probably not the best solution.
  - Create an app to clasify your own gestures in real time, it can be done now but not in real time.


---
>This proyect uses  Niklas Rosenstein 's [ Myo-Python ](https://github.com/NiklasRosenstein/myo-python) library, a great library to manage MYO with python.  
---
>This project is made with love to learn and contribute to the Myo community.

----

<p align="center">2021 Leonardo Artiles Montero</p>
