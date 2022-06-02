from django.shortcuts import redirect, render
from album.models import Album
from django.contrib.auth.decorators import login_required

def album(request):
    album_photo = Album.objects.all() 
    return render(request, "album/album.html", {"album_photo":album_photo})

# fonction pour ajouter une image
@login_required(login_url="/login/")
def new_photo(request):
    if request.method == "POST":
        # auteur = request.user
        title = request.POST['title']
        link = request.POST['link']
        auteur = request.user
        photo = Album.objects.create(
            title = title,
            link = link,
            auteur = auteur
        )
        photo.save()
        return redirect("/album/")
    return render(request, "album/new_photo.html")