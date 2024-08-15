import cv2
import numpy as np
from playMidi import play_midi
import time
import random
from midiutil import MIDIFile
import threading

def detect_lines(image_path):
    # Read the original image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges
    edges = cv2.Canny(gray_image, 50, 150)

    # Detect lines using Hough Transform
    lines = cv2.HoughLinesP(
        edges, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=10
    )

    return lines, image

def detect_edges(image_path):
    # Read the original image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges
    edges = cv2.Canny(gray_image, 50, 150)

    return edges

    

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

def play_sound(note):
    play_midi(f"AcousticPiano/{note}.mid")

def main(image_path, instru=1):
    lines, image = detect_lines(image_path)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            # note = determine_note_from_length(length)
            if length > 255:
                length = random.randint(150, 255)
            
            print(length)
            create_midi(int(length), 1, instru, f"AcousticPiano/{length}.mid")
            note = f"{length}"

            # Draw the line incrementally
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.imshow('Visualizing Lines with Music', image)
            cv2.waitKey(1)  # Small delay to visualize the drawing step by step

            # Play the corresponding note
            play_sound(note)

            # Pause briefly to sync with the visualization
            # random sleep time to make it more interesting
            time.sleep(0)

    cv2.destroyAllWindows()

def determine_note_from_length(length):
    # Dummy implementation: map length to note
    if length < 100:
        print("A3")
        return "A3"
    elif length < 125:
        print("C4")
        return "C4"
    elif length < 150:
        print("E4")
        return "E4"
    elif length < 175:
        print("G4")
        return "G4"
    elif length < 200:
        print("B4")
        return "B4"
    elif length < 225:
        print("D5")
        return "D5"
    elif length < 250:
        print("F5")
        return "F5"
    elif length < 275:
        print("A5")
        return "A5"
    else:
        return "C6"


if __name__ == "__main__":
    image_path = "black-hole-stats.png"

    # Get the instrument number from the user input (1-128)
    instru = int(input("Enter the instrument number (1-128): "))
    
    # image_path = "wallpaper.jpeg"
    main(image_path, instru)