def make_album(artist_name, album_title, number_tracks=''):
	""" function takes artist and album names and returns dictionary """
	album_dict = {
		'artist': artist_name.title(), 
		'album': album_title.title()
		}
	if number_tracks:
		album_dict['number_tracks'] = number_tracks
	return album_dict

#prepare prompts for user data entry
artist_prompt = "\nEnter 'q' to quit the prompt at any time.\n\nWho is your favorite musical artist?: "
album_prompt = "And what is their best album?: "

#while loop to prompt the user for the artist name and album title
while True:
	artist = input(artist_prompt)
	if artist == 'q':
		break
	album = input(album_prompt)
	if title == 'q':
		break
	album = make_album(artist, album)
	print(album)