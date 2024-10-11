from django.shortcuts import render, redirect, resolve_url
from django.views.generic import CreateView

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo
from pyperclip import copy

# Create your views here.


def home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET)

    if search_form.is_valid() and search_form.cleaned_data['pet_name']:
        all_photos = all_photos.filter(
            tagged_pets__name__icontains=search_form.cleaned_data['pet_name']
        )

    content = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form
    }
    return render(request, 'common/home-page.html', content)


def like_functionality(request, photo_id):
    liked_photo = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_photo:
        liked_photo.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST or None)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


