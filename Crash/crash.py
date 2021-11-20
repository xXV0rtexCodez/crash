import time
from playsound import playsound
def crash(ReturnMessage):
    def keyint():
        time.sleep(0.8)
        playsound('/Users/1642128/Downloads/Crash/Assets/sound.wav')
        raise KeyboardInterrupt(ReturnMessage) from None
    t = keyint()
    return t