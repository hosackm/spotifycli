import spotify
from threading import Event
from song_queue import SongQueue


class App():
    def __init__(self):
        # Spotify Session
        self.session = spotify.Session()

        # Queue to hold songs to be played
        self.SongQueue = SongQueue()

        # Event Blockers
        # self.logged_in_state_changed = Event()
        # self.play_state_changed = Event()
        self.is_logged_in = False

        # Spotify Event Loop
        self.loop = spotify.EventLoop(self.session)
        self.loop.start()

        # Set callbacks
        self.set_callbacks()

        # Audio player
        self.audio = spotify.PortAudioSink(self.session)

        # List of events to handle during run loop
        self.events = []

    def set_callbacks(self):
        self.session.on(spotify.SessionEvent.CONNECTION_STATE_UPDATED,
                        self.connection_cb)
        self.session.on(spotify.SessionEvent.END_OF_TRACK, self.playstate_cb)

    def connection_cb(self, session):
        if self.session.connection.state is spotify.ConnectionState.LOGGED_IN:
            # self.logged_in_state_changed.set()
            self.is_logged_in = True
        else:
            self.is_logged_in = False

    def playstate_cb(self, session):
        self.end_of_track.set()

    def login(self, user, pw):
        self.session.login(user, pw)
        while not self.is_logged_in:
            pass

if __name__ == "__main__":
    from getpass import getpass
    a = App()
    a.login(raw_input(), getpass())
