python
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            print(strTime)  
            speak(f"Sir, the time is {strTime}")