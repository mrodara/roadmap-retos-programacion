"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

def make_album(artist_name: str, album_title: str, number_songs: int = None) -> dict:
    album = {
        "artist" : artist_name.title(),
        "album_title" : album_title.title()
        
    }
    
    if number_songs:
            album["number_songs"] = number_songs
    
    return album

editing = True

while editing:
    
    artist = input("Introduce the artist name (exit to quit): ")
    
    if artist.lower() == "exit":
        editing = False
        break

    album = input("Introduce the album name: ")
    
    print(make_album(artist, album))