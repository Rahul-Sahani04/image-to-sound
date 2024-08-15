from midiutil import MIDIFile

def create_midi(note, duration, instru, filename="output.mid"):
    midi = MIDIFile(1)  # Single track
    track = 0
    time = 0  # Start at the beginning
    channel = 0
    volume = 100  # 0-127, as per the MIDI standard

    midi.addProgramChange(track, channel, time, instru)  # 1 is for Acoustic Grand Piano
    

    midi.addNote(track, channel, note, time, duration, volume)
    
    
    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)

# Example usage
create_midi(60, 1,int( 270 / 15))  # Middle C (MIDI note 60) for 1 beat

from pygame import mixer

mixer.init() 
mixer.music.load("output.mid")
mixer.music.play()


# create notes for C4, E4, G4, and C5

# create_midi(60, 1, "C4.mid")
# create_midi(64, 1, "E4.mid")
# create_midi(67, 1, "G4.mid")
# create_midi(72, 1, "C5.mid")

# # create notes for D4, F4, A4, B4, and D5
# create_midi(62, 1, "D4.mid")
# create_midi(65, 1, "F4.mid")
# create_midi(69, 1, "A4.mid")
# create_midi(71, 1, "B4.mid")
# create_midi(74, 1, "D5.mid")

# # create notes for  F5, C6 and A5
# create_midi(77, 1, "F5.mid")
# create_midi(84, 1, "C6.mid")
# create_midi(81, 1, "A5.mid")

# A3
# create_midi(57, 2, "A3.mid")