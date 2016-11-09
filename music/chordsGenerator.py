import random
import time

chromatic_scale = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

def getMajorScale(key_note):
    formula = [2,2,1,2,2]
    scale = []
    scale.append(key_note)
    for i in range(len(chromatic_scale)):
        if chromatic_scale[i] == key_note:
            break
    j = 0
    while len(scale) < 6:
        if i + formula[j] < 12:
            i += formula[j]
            j += 1
        else:
            i = 12 - (i + formula[j])
            j += 1
        scale.append(chromatic_scale[i])

    for i in range(len(scale)):
        if i in [2,3,6]:
            scale[i] += 'm'
    return scale

def getMinorScale(key_note):
    formula = [2,1,2,2,1]
    scale = []
    scale.append(key_note)
    for i in range(len(chromatic_scale)):
        if chromatic_scale[i] == key_note:
            break
    j = 0
    while len(scale) < 6:
        if i + formula[j] < 12:
            i += formula[j]
            j += 1
        else:
            i = abs(12 - (i + formula[j]))
            j += 1
        scale.append(chromatic_scale[i])

    for i in range(len(scale)):
        if i in [2,3,6]:
            scale[i] += 'm'
    return scale            

def compose(pref=None, key=None):
    if key==None:
        key_note = random.choice(chromatic_scale)
    else:
        key_note = key

    if pref == None:
        toss = [0,1]
        j = random.choice(toss)
    else:
        j = pref

    if j == 1:
        scale = getMinorScale(key_note)
    else:
        scale = getMajorScale(key_note)

    no_of_chords = random.randrange(3,6)

    chords = ''
    picked = []
    while chords.count(' ') < no_of_chords:
        k = random.randrange(6)
        if k not in picked:
            picked.append(k)
            chords += scale[k] + ' '

    return key_note, chords.strip()

def chordCheck(chords, scale):
    chords = chords.split(' ')
    #print chords, scale
    for chord in chords:
        if chord not in scale and chord != '':
            return False
    return True

def getKey(chords):
    for key in chromatic_scale:
        #print key + "---"
        if chordCheck(chords, getMinorScale(key)):
            return key
        elif chordCheck(chords, getMajorScale(key)):
            return key
    return "Key not found!!"


if __name__ == "__main__":
    print compose()