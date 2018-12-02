MENU = """Songs To Learn 1.0 - by Kay Zin Phone"""
MENU_1 = """MENU:
L - List songs
A - Add new song
C - Complete a song
Q - Quit"""

def list_song():
    pass
def complete_song():
    pass
def add_new_song(t, a, y):
    pass
def main():
    songs_file = open("songs.csv", "r")
    song_length = songs_file.readlines()
    print(MENU)
    print("{} songs loaded".format(len(song_length)))
    print(MENU_1)
    choice = input(">>>").upper()

    while choice != 'Q':
        if choice == 'L':
            list_song()
        elif choice == 'A':
            title = input("Title: ")
            artist = input("Artist: ")
            year = input("Year: ")
            add_new_song(title, artist, year)
        elif choice == 'C':
            complete_song()
        else:
            print("Your input is invalid")

        choice = input(MENU_1 + "\n>>>")
    print("{} songs saved to songs.csv\nHave a nice day :)".format(len(song_length)))
    songs_file.close()


main()
