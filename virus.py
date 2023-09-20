import pygame
import time
import tkinter as tk
import threading

def create_window():
    window = tk.Tk()
    window.title("Message")
    label = tk.Label(window, text="There is no escape", font=("Arial Bold", 20))
    label.pack()
    window.mainloop()

def play_mp3(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        # check if the music is playing
        time.sleep(1) # wait for 1 second before checking again

file_name = "Rick Astley - Never Gonna Give You Up (Official Music Video).mp3"

# Create threads for playing music and creating window
thread1 = threading.Thread(target=play_mp3, args=(file_name,))
thread2 = threading.Thread(target=create_window)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

