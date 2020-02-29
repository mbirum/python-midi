note_values = {
    'C': 24,
    'C#': 25,
    'D': 26,
    'D#': 27,
    'E': 28,
    'F': 29,
    'F#': 30,
    'G': 31,
    'G#': 32,
    'A': 33,
    'A#': 34,
    'B': 35,
    'C1': 36,
    'C#1': 37,
    'D1': 38,
    'D#1': 39,
    'E1': 40,
    'F1': 41,
    'F#1': 42,
    'G1': 43,
    'G#1': 44,
    'A1': 45,
    'A#1': 46,
    'B1': 47,
    'C2': 48,
    'C#2': 49,
    'D2': 50,
    'D#2': 51,
    'E2': 52,
    'F2': 53,
    'F#2': 54,
    'G2': 55,
    'G#2': 56,
    'A2': 57,
    'A#2': 58,
    'B2': 59
}

def getNote(pin):
    n = open('/home/pi/devl/midi/touch-pins/%s/note'%(pin), 'r')
    note = n.read()
    print note
    return note_values.get(note)

def getVelocity(pin):
    v = open('/home/pi/devl/midi/touch-pins/%s/velocity'%(pin), 'r')
    velocity = v.read()
    return velocity