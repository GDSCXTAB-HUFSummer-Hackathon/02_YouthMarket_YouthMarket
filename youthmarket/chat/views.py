# chat/views.py
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from post.models import User,Post
import json

def index(request):
    return render(request, 'index.html', {})

def room(request, multi_idx):
    post_idx, seller_idx, buyer_idx = map(int, multi_idx.split('-'))
    user_info = get_object_or_404(User, pk=request.session.get('user')) # buyer_idx
    userName = user_info.userName
    #seller_info = get_object_or_404(User, pk=seller_idx)
    if seller_idx == user_info.idx:
        your_info = get_object_or_404(User, idx = buyer_idx)
    else:
        your_info = get_object_or_404(User, pk=seller_idx)
    print('room()/user_info: ', user_info)
    print('room()/user_info.photo.url: ', user_info.photo.url) # /media/users/kim.jpeg
    #print('room()/seller_info: ', seller_info)
    #print('room()/seller_info.photo.url: ', seller_info.photo.url) # /media/users/kim.jpeg/
    # return render(request, 'chat_bb.html', {
    print("http://127.0.0.1:8000" + user_info.photo.url)
    post = get_object_or_404(Post, pk= post_idx)


    return render(request, 'chat_bbb.html', {
        'room_name_json': mark_safe(json.dumps(post_idx)),
        'userName': mark_safe(json.dumps(userName)),
        'yourName': mark_safe(json.dumps(your_info.userName)),
        'user_photo_url': mark_safe(json.dumps("http://127.0.0.1:8000" + user_info.photo.url)),
        'your_photo_url': mark_safe(json.dumps("http://127.0.0.1:8000" + your_info.photo.url)),
        'post_idx': mark_safe(json.dumps(post_idx)),
        'seller_idx': mark_safe(json.dumps(seller_idx)),
        'buyer_idx': mark_safe(json.dumps(buyer_idx)),

        'post_title': mark_safe(json.dumps(post.title)),
        'post_photo_url': mark_safe(json.dumps("http://127.0.0.1:8000" + post.photo.url)),

    })
# def chat(request, post_id):
#     return render(request, 'chat.html', {
#         'chat_room_json': mark_safe(json.dumps(post_id))
#     })
