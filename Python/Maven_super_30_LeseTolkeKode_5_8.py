python
        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            song = random.choice(songs) 
            print(f"playing {song}...")
            os.startfile(os.path.join(music_dir, song))