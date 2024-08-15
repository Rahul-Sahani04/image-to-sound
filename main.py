import cv2
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

from playMidi import play_midi


def detect_lines(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 50, 150)
    lines = cv2.HoughLinesP(
        edges, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=10
    )
    return lines


def play_sound(note):
    sound = AudioSegment.from_file(f"{note}.mid")
    play(sound)


def main(image_path):
    lines = detect_lines(image_path)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            note = determine_note_from_length(
                length
            )  # implement this function based on your needs
            play_midi(f"{note}.mid")


def determine_note_from_length(length):
    # Dummy implementation: map length to note
    if length < 100:
        return "C4"
    elif length < 200:
        return "E4"
    else:
        return "G4"


if __name__ == "__main__":
    image_path = "black-hole-stats.png"
    main(image_path)
