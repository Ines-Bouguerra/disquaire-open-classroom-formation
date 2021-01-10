# Create your views here.

from django.http import HttpResponse
from .models import ALBUMS


def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)


def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)


def detail(request, album_id):
    id = int(album_id)  # make sure we have an integer.
    album = ALBUMS[id]  # get the album with its id.
    # grab artists name and create a string out of it.
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(
        album['name'], artists)
    return HttpResponse(message)
