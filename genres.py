# The favorite_genre function finds each user's most listened-to music genre.

# Approach:
# - Create a song-to-genre mapping.
# - Count the frequency of each genre for every user.
# - Determine the genres with the highest count per user.

# TC: O(m + n) - Mapping and counting operations.
# SC: O(m + n) - Space for storing mappings.


from collections import defaultdict

def favorite_genre(user_map, genre_map):
    # Create a song to genre mapping
    song_to_genre = {}
    for genre, songs in genre_map.items():
        for song in songs:
            song_to_genre[song] = genre
    
    result = {}
    for user, songs in user_map.items():
        genre_count = defaultdict(int)
        max_count = 0
        for song in songs:
            if song in song_to_genre:
                genre = song_to_genre[song]
                genre_count[genre] += 1
                max_count = max(max_count, genre_count[genre])
        
        # Find the genres with the highest count
        result[user] = [genre for genre, count in genre_count.items() if count == max_count]
    
    return result

if __name__ == "__main__":
    user_songs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"]
    }

    song_genres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }

    res = favorite_genre(user_songs, song_genres)
    print(res)