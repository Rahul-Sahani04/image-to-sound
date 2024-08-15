from midiutil import MIDIFile

def create_midi(note, duration, instru, filename="output.mid"):
    midi = MIDIFile(1)  # Single track
    track = 0
    time = 0  # Start at the beginning
    channel = 0
    volume = 100  # 0-127, as per the MIDI standard
    
    midi.addProgramChange(track, channel, time, instru)  # 2 is for Acoustic Grand Piano
    

    midi.addNote(track, channel, note, time, duration, volume)
    
    
    with open( "BackUpMid/" + filename, "wb") as output_file:
        midi.writeFile(output_file)

# Example usage
create_midi(60, 2, 1, filename="test.mid")  # Middle C (MIDI note 60) for 1 beat

from pygame import mixer
import os
mixer.init()
mixer.music.load("test.mid")
mixer.music.play()

for i in range( 20, 30):
    create_midi(60, 1, i , f"test{i}.mid")
    
    mixer.music.load(f"BackUpMid/test{i}.mid")
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    print(" Done", i)
    
    # Ask the user to press a key to delete the file and play the next one or repeat the current one
    while True:
        print("\n\n\n\n\nPress Enter to play the next file, or type 'r' to repeat the current file or type 's' to save the current file")
        user_input = input()
        if user_input == "":
            os.remove(f"BackUpMid/test{i}.mid")
            break
        elif user_input == "s":
            print("Saving the current file")
            os.rename(f"BackUpMid/test{i}.mid", f"BackUpMid/test{i}_saved.mid")
            break
        elif user_input == "r":
                
            print("Repeating the current file")
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