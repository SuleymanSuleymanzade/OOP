import inspect 
import flask 
class MetaSingleton(type):
	__instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls.__instances:
			cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls.__instances[cls]

# ======================== helper =====================

class MediaPlayer(metaclass = MetaSingleton):
	def __init__(self, songs):
		self.songs = songs 

	def show_playlist(self):
		print('--------------')
		for song in self.songs:
			print(song)

	def update(self, songs):
		self.songs = songs

#==================== Client ==========================

songs = ['s1', 's2', 's3', 's4', 's5']

mp = MediaPlayer(songs)

mp.show_playlist()

mp2 = MediaPlayer(['a1','a2', 'a3', 'a4'])

mp2.update(['a1', 'a2', 'a3'])

mp2.show_playlist()
mp.show_playlist()






