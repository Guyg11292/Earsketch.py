# description: 
from earsketch import *

init()
setTempo(120)

sounds = [RD_POP_SYNTHBASS_5, ENTREP_THEME_BASS_1, RD_POP_SOFTINELEAD_1]
for i in range(len(sounds)):
    sound = sounds[i]
    track = i+1
    fitMedia(sound, track, 1, 17)

finish()
