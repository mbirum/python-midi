
pin_notes = {
    0: 'F#2',
    1: 'F#1',
    2: 'C1',
    3: 'B1',
    4: 'E#1',
    5: 'D',
    6: 'A2',
    7: 'B2',
    8: 'C#',
    9: 'G1',
    10: 'G#1',
    11: 'A#2'
}

note_values = {
    'C': 60,
    'C#': 61,
    'D': 62,
    'D#': 63,
    'E': 64,
    'E#': 65,
    'F': 66,
    'F#': 67,
    'G': 68,
    'G#': 69,
    'A1': 70,
    'A#1': 71,
    'B1': 72,
    'B#1': 73,
    'C1': 74,
    'C#1': 75,
    'D1': 76,
    'D#1': 77,
    'E1': 78,
    'E#1': 79,
    'F1': 80,
    'F#1': 81,
    'G1': 82,
    'G#1': 83,
    'A2': 84,
    'A#2': 85,
    'B2': 86,
    'B#2': 87,
    'C2': 88,
    'C#2': 89,
    'D2': 90,
    'D#2': 91,
    'E2': 92,
    'E#2': 93,
    'F2': 94,
    'F#2': 95,
    'G2': 96,
    'G#2': 97,
    'A3': 98,
    'A#3': 99,
    'B3': 100,
    'B#3': 101
}

def pinValue(pin):
    note = pin_notes.get(pin)
    return note_values.get(note)