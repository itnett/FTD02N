bash
#!/bin/bash

# Funksjon for å sjekke om en mappe eksisterer, og lage den hvis den ikke gjør det
createIfNot() {
    if [ ! -d "$1" ]; then  # Sjekk om mappen ikke eksisterer
        mkdir "$1"  # Lag mappen
    fi
}

# Funksjon for å flytte filer til en bestemt mappe
move() {
    folder="$1"  # Navnet på mappen
    shift  # Fjern første argument (mappenavnet) fra argumentlisten
    for file in "$@"; do  # Iterer gjennom resten av argumentene (filene)
        mv "$file" "$folder"/  # Flytt filen til mappen
    done
}

# Liste over alle filer i gjeldende katalog
files=(*)

# Opprett mapper for ulike filtyper
createIfNot "Images"
createIfNot "Audios"
createIfNot "Videos"
createIfNot "Docs"

# Arrays som holder filtyper
imgs=(".png" ".jpg" ".jpeg")
audios=(".mp3" ".m4a" ".wav" ".flv")
videos=(".mp4")
docs=(".pdf" ".doc" ".docx" ".txt")

# Funksjon for å finne filer med bestemte filendelser
find_files() {
    local extensions=("$@")
    local matched_files=()
    for file in "${files[@]}"; do
        for ext in "${extensions[@]}"; do
            if [[ "$file" == *"$ext" ]]; then
                matched_files+=("$file")
            fi
        done
    done
    echo "${matched_files[@]}"
}

# Finn og flytt filer til riktig mappe
move "Images" $(find_files "${imgs[@]}")
move "Audios" $(find_files "${audios[@]}")
move "Videos" $(find_files "${videos[@]}")
move "Docs" $(find_files "${docs[@]}")