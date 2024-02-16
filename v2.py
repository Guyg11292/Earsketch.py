# description: 
from earsketch import *

init()
setTempo(120)

sounds = [RD_POP_SYNTHBASS_5, AK_UNDOG_PIANO_3, ENTREP_VOX_BK_BLKMAN]
for i in range(len(sounds)):
    sound = sounds[i]
    track = i+1
    fitMedia(sound, track, 1, 17)

finish()
