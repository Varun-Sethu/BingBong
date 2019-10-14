# Lib that just deals with the detection of musical notes
import numpy as np
from collections import deque

from .processing import breakup
from . import util




    


class Note_Detector:
    def __init__(self):
        self.detected_notes = deque()


    def process(self, chunk):
        detected_sounds = breakup(chunk)
        for sound in detected_sounds:
            detected_note = self.__identify_note(chunk)
            if detected_note != None:
                self.detected_notes.append(detected_note)




    # Function that identifies the note of a given frequency
    def __identify_note(self, signal):
        notes = {1: "C", 2: "C#", 3: "D", 4: "D#", 5: "E", 6: "F", 7: "F#", 8: "G", 9: "G#", 10: "A", 11: "A#", 12: "B"}

        # Compute the frequency of the signal, if there is no absolute frequency then just trow it out
        fft_break = np.abs(np.fft.fft(signal))
        dominant_freq = fft_break.argmax(axis=0)
        mag = fft_break[dominant_freq]

        if mag/np.sum(fft_break) >= 0.8:
            dominant_freq = dominant_freq/len(fft_break)
        else:
            return None


        harmonic = 12*np.log(frequency - 440, 2)
        # This is a really weird algorithm to determine if a value falls within a 10% range but basically if ceil(n-0.1) = floor(n) then n is within a 10% range of a note
        # Checks that it is above a note
        if np.ceil(harmonic-0.1) == np.floor(harmonic):
            return notes[np.floor(harmonic)]

        # checks that it is below a ntoe
        if np.floor(harmonic + 0.1) == np.ceil(harmonic):
            return notes[np.ceil(harmonic)]
        return None    
