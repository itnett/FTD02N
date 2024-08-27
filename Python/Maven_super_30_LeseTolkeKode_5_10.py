python
        elif 'coding' in query or 'code' in query:
            NetBeans = "C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe"
            Thonny = "C:\\Users\\Madhav\\AppData\\Local\\Programs\\Thonny\\thonny.exe"
            PyCharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
            VSCode = "C:\\Users\\Madhav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

            speak("Which IDE do you wanna use sir?")
            mknc = Command().lower()
            pycharm_list = {"pycharm", "picharm", "pi charm", "py charm"}
            VSCode_list = {"vscode", "vs code", "v s code"}

            if "netbeans" in mknc:
                print("Starting NetBeans...")
                os.startfile(NetBeans)
            elif mknc == "thonny" or mknc == "thony":
                print("Starting Thonny...")
                os.startfile(Thonny)
            elif mknc in pycharm_list:
                print("Starting Pycharm...")
                os.startfile(PyCharm)
            elif mknc in VSCode_list:
                print("Starting VS Code...")
                os.startfile(VSCode)