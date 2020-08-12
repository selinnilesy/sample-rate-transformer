import sys
import os
from scipy.io import wavfile
import subprocess
import numpy as np

SAMPLE_RATE=16000


def transformer(label_directory): 
    # list all .waw files under label_directory in a sorted way
    files = sorted([os.path.join(label_directory, x)
                    for x in os.listdir(label_directory) if x.endswith(".wav")])
    for fname in files:
        # sample rate of each file
        sr, input_sound = wavfile.read(fname)

        nname = fname.replace(".wav", f"_{SAMPLE_RATE}.wav")
        # rearrange the sample rate
        retcode = subprocess.call(["ffmpeg", "-i", fname, "-ar", str(SAMPLE_RATE),
                                       "-ac", "1", nname])
        if retcode != 0:
            raise Exception("ffmpeg failed") # error occured
        os.rename(fname, fname + "-prev") # previous version of the updated file (nname)
        fname = nname # update
        print( f"{fname} transformation is completed")


if __name__ == "__main__":   #  script:  python3 sr_transformer.py <category_name_here>
    input_category = os.path.normpath(sys.argv[1]) # normalize path
    labels=files = sorted([os.path.join(input_category, label)
                            for label in os.listdir(input_category)])
    
    for label in labels:
            transformer(label) # process categories