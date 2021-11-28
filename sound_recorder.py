from scipy.io.wavfile import write
from pathlib import Path
import sounddevice
import os

def recordVoice():
    fs = 44100
    second = int(input("Please enter the duration: "))

    print("Recording...")

    record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels = 2)
    sounddevice.wait()

    recordVoice.counter = int(readCounterVal())

    filename = Path("vrecord.wav")

    if filename.is_file():
        filename = f"vrecord{str(recordVoice.counter)}.wav"
        recordVoice.counter += 1
        writeCounterVal(str(recordVoice.counter))

    write(str(filename), fs, record_voice)

    print("Sound Recording done!")

    print(os.path.abspath(str(filename)))

def writeCounterVal(value):
    f = open("counterValVR.txt", "w")

    if not Path("counterValVR.txt").is_file():
        f.write("0")
    else:
        f.write(value)

    f.close()

def readCounterVal():
    if not Path("counterValVR.txt").is_file():
        content = "0"
    else:
        f = open("counterValVR.txt", "r")
        content = f.read()
        f.close()

    return content


if __name__ == "__main__":
    recordVoice()
    