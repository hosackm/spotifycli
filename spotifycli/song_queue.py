from random import shuffle


class SongQueue():
    """
    Class to represent a queue of songs to be played by the Spotify player.
    Songs can be shuffled in place to be played randomly.
    After the queue has been exhausted it can be reloaded and played again.

    >>> s = SongQueue()
    >>> s.load(["abc"])
    >>> len(s)
    1
    >>> s.get_next()
    'abc'
    >>> s.has_songs_left()
    False
    >>> s.reload(True)
    >>> s.get_next()
    'abc'
    """

    def __init__(self):
        self.songs = []  # master list of songs
        self.notplayed = []  # songs yet to be played

    @property
    def notplayed(self):
        return self.notplayed

    @notplayed.setter
    def notplayed(self, v):
        self.notplayed = v

    @property
    def songs(self):
        return self.songs

    def has_songs_left(self):
        """
        Check to see if there are songs left to play
        :return: songs left to be played
        :rtype: bool
        """
        return bool(self.notplayed)

    def get_next(self):
        """
        Return the next song to be played
        :return: next song in queue
        :rtype: Song
        """
        n = self.notplayed.pop()
        return n

    def shuffle(self):
        """
        Shuffle the songs in the queue
        """
        shuffle(self.notplayed)

    def load(self, seq):
        """
        Load the queue with a list of songs
        :param list seq: list of songs to put in the queue
        """
        self.songs = seq
        self.notplayed = self.songs[:]

    def reload(self, shuffle=False):
        """
        Reload all songs played into the queue
        :param bool shuffle: shufle the queue after reloading
        """
        self.notplayed = self.songs[:]
        if shuffle:
            self.shuffle()

    def add_song(self, s):
        """
        Append a song to the queue
        :param Song s: song to be appended to queue
        """
        self.songs.append(s)

    def __iter__(self):
        while self.has_songs_left():
            yield self.get_next()

    def __len__(self):
        return len(self.songs)


if __name__ == "__main__":
    s = SongQueue()
    s.load(["song_" + str(i) for i in xrange(100)])
    for song in s:
        print song

    s.reload(True)
    for song in s:
        print song
