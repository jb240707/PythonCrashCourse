def make_album(artist_name, album_title, number_tracks=''):
	""" function takes an artist name and album title and returns a dictionary then gives the option to add the number of tracks on the album """
	album_dict = {
		'artist': artist_name.title(), 
		'album': album_title.title()
		}
	#Provide option to give the number of tracks for each album
	if number_tracks:
		album_dict['number_tracks'] = number_tracks
	return album_dict

#Print data from dictionary in make_album after providing data for each key 
formatted = make_album('chevelle', 'ttot', '13')
print(formatted)

formatted = make_album('as i lay dying', 'awakening')
print(formatted)

formatted = make_album('sevendust', 'all i see', number_tracks=10)
print(formatted)