import xml.etree.ElementTree as ET

def show_menu():
    print("\nMenú Principal:")
    print("1. Álbumes")
    print("2. Artistas")
    print("3. Canciones")
    print("4. Géneros")
    print("0. Salir")

def show_menu_songs():
    print("\nMenú de Canciones:")
    print("1. Listar todas las canciones")
    print("2. Buscar canción por título")
    print("0. Volver")

def show_menu_albums():
    print("\nMenú de Álbumes:")
    print("1. Listar todos los álbumes")
    print("2. Buscar álbum por título")
    print("0. Volver")

def show_menu_artists():
    print("\nMenú de Artistas:")
    print("1. Listar todos los artistas")
    print("2. Buscar artista por nombre")
    print("0. Volver")

def show_menu_genres():
    print("\nMenú de Géneros:")
    print("1. Listar todos los géneros")
    print("2. Buscar género por nombre")
    print("0. Volver")

def load_data():
    # Cargar los archivos XML
    albums_tree = ET.parse('albums.xml')
    artists_tree = ET.parse('artists.xml')
    songs_tree = ET.parse('songs.xml')
    genres_tree = ET.parse('genres.xml')

    albums = albums_tree.getroot()
    artists = artists_tree.getroot()
    songs = songs_tree.getroot()
    genres = genres_tree.getroot()

    return albums, artists, songs, genres

def list_songs(songs):
    # Aquí listamos todas las canciones
    print("\nCanciones disponibles:")
    for song in songs.findall('song'):
        title = song.find('title').text
        artist = song.find('artist').text
        album = song.find('album').text
        year = song.find('year').text
        genre = song.find('genre').text
        print(f"Título: {title}, Artista: {artist}, Álbum: {album}, Año: {year}, Género: {genre}")

def list_albums(albums):
    # Aquí listamos todos los álbumes
    print("\nÁlbumes disponibles:")
    for album in albums.findall('album'):
        title = album.find('title').text
        artist = album.find('artist').text
        year = album.find('year').text
        print(f"Título: {title}, Artista: {artist}, Año: {year}")

def list_artists(artists):
    # Aquí listamos todos los artistas
    print("\nArtistas disponibles:")
    for artist in artists.findall('artist'):
        name = artist.find('name').text
        print(f"Nombre: {name}")

def main():
    albums, artists, songs, genres = load_data()

    while True:
        show_menu()
        try:
            choice = int(input("Seleccione una opción: "))
            if choice == 0:
                print("Saliendo...")
                break
            elif choice == 1:
                show_menu_albums()
                album_choice = int(input("Seleccione una opción: "))
                if album_choice == 1:
                    # Listar álbumes
                    list_albums(albums)
                elif album_choice == 2:
                    # Buscar álbum
                    print("Buscar álbum por título")
                elif album_choice == 0:
                    continue
                else:
                    print("Opción no válida")

            elif choice == 2:
                show_menu_artists()
                artist_choice = int(input("Seleccione una opción: "))
                if artist_choice == 1:
                    # Listar artistas
                    list_artists(artists)
                elif artist_choice == 2:
                    # Buscar artista
                    print("Buscar artista por nombre")
                elif artist_choice == 0:
                    continue
                else:
                    print("Opción no válida")

            elif choice == 3:
                show_menu_songs()
                song_choice = int(input("Seleccione una opción: "))
                if song_choice == 1:
                    # Listar canciones
                    list_songs(songs)
                elif song_choice == 2:
                    # Buscar canción
                    print("Buscar canción por título")
                elif song_choice == 0:
                    continue
                else:
                    print("Opción no válida")

            elif choice == 4:
                show_menu_genres()
                genre_choice = int(input("Seleccione una opción: "))
                if genre_choice == 1:
                    # Mostrar géneros
                    print("Géneros seleccionados")
                elif genre_choice == 2:
                    # Buscar género
                    print("Buscar género por nombre")
                elif genre_choice == 0:
                    continue
                else:
                    print("Opción no válida")

            else:
                print("Opción no válida")

        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
