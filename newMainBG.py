import cv2
import numpy as np
from playMidi import play_midi
import time
import random
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

    
    

def play_sound(note):
    play_midi(f"{note}")

def main(image_path):
    lines, image = detect_lines(image_path)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            note = determine_note_from_length(length)

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
        return "BackUpMid/test1_saved.mid"
    elif length < 175:
        print("G4")
        return "BackUpMid/test2_saved.mid"
    elif length < 200:
        print("B4")
        return "BackUpMid/test9_saved.mid"

    elif length < 250:
        print("F5")
        return "BackUpMid/test12.mid"
    # elif length < 275:
    #     print("A5")
    #     return "A5"
    else:
        return "BackUpMid/test.mid"


if __name__ == "__main__":
    # image_path = "black-hole-stats.png"

    
    image_path = "wallpaper.jpeg"
    main(image_path)
