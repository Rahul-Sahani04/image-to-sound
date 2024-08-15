import pygame

def play_midi(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    # Volume control
    pygame.mixer.music.set_volume(0.5)

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    play_midi("output.mid")
    
