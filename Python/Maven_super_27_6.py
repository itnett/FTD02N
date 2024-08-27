python
    def binær_søk(liste, mål):
        lav = 0
        høy = len(liste) - 1
        
        while lav <= høy:
            midt = (lav + høy) // 2
            if liste[midt] == mål:
                return midt
            elif liste[midt] < mål:
                lav = midt + 1
            else:
                høy = midt - 1
        
        return -1