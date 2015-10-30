from __future__ import print_function
import click
from .config import BANNER


def main():
    """
    Intercept the spotifycli call and print the banner first
    """
    print(BANNER)
    spotifycli()


@click.group()
def spotifycli():
    """
    Command line Spotify player.
    """
    print(BANNER)


#############################
# Search Spotify API commands
#############################
@spotifycli.group()
def search():
    """
    SEARCH [artist, album, or song]
    """
    pass


@search.command()
def artist():
    print("Hello search: artist")


@search.command()
def album():
    print("Hello search: album")


@search.command()
def song():
    print("Hello search: song")


#######################
# Play / Pause commands
#######################
@spotifycli.command()
def play():
    """
    PLAY
    """
    print("Hello play!")


@spotifycli.command()
def pause():
    """
    PAUSE
    """
    print("Hello pause!")


###########################
# Volume up / down commands
###########################
@spotifycli.group()
def volume():
    """
    VOLUME [up, down, get]
    """
    pass


@volume.command()
def up():
    print("Volume up")


@volume.command()
def down():
    print("Volume down")


@volume.command()
def get():
    print("Volume is 100%")


###############################
# Playlist information commands
###############################
@spotifycli.group()
def playlist():
    """
    PLAYLIST: [list]
    """
    pass


@playlist.command()
def list():
    print("The songs in this playlist are:")


#########################
# Current status commands
#########################
@spotifycli.group()
def current():
    """
    CURRENT [song, playlist, volume, status]
    """


@current.command()
def song():
    print("Current song: ")


@current.command()
def playlist():
    print("Current playlist: ")


@current.command()
def volume():
    print("Current volume: ")


@current.command()
def status():
    print("Current status: ")
