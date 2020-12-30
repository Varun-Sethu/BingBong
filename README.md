# Bing Bong

Application that allows you to play notes on a musical instrument and perform certain actions on your computer...
For example:
 - An A# might map to a left click 
 - A B might map to the movement of the mouse rightwards


The application can easilly be configured by editing the config.ini file found at: bong/config.ini


## Components
There are two components to the application... Bing and Bong. Bing handles note detection and audio signal processing while Bong handles system functions and the execution of commands. Currently Bing features a simple implentation of the recursive cooley-tukey algorithm and an exponential average to compute the envelope of the incoming audio signal

BingBong *tries* to use the observer pattern :)
