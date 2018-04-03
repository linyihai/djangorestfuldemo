import simplejson
from music_type.models import Album, MusicType, MusicSubType
from django.http import HttpResponse, QueryDict
from django.core.paginator import Paginator

# Create your views here.
def album(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        singer = request.POST.get('singer', '')
        desc = request.POST.get('desc', '')
        if name is not None:
            album, not_exist = Album.objects.get_or_create(name=name)
            if not_exist:
                resp = {'error_msg': 'record already exists', 'id': ''}
            else:
                album.singer = singer
                album.desc = desc
                album.save()
                resp = {'error_msg': '', 'id': album.id}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'name is required', 'id': ''}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'PUT':
        q = QueryDict(request.body)
        _id = q.get('id', None)
        name = q.get('name', None)
        singer = q.get('singer', None)
        if _id is not None:
            album = Album.objects.get(id__exact=_id)
            if album:
                if name:
                    album.name = name
                if singer:
                    album.singer = singer
                album.save()
                resp = {'error_msg': '', 'id': album.id}
                return HttpResponse(content=simplejson.dumps(resp))
            else:
                resp = {'error_msg': 'record has deleted', 'id': album.id}
                return HttpResponse(status=404, content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'id is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'GET':
        total = 0
        page_size = request.GET.get('page_size', 10)
        page = request.GET.get('page', 1)
        name = request.GET.get('name', None)
        singer = request.GET.get('singer', None)
        albums = Album.objects
        if name is not None:
            albums = albums.filter(name=name)
        if singer is not None:
            albums = albums.filter(singer=singer)
        albums = albums.all()
        p = Paginator(albums, page_size)
        album_list = []
        for album in p.page(page).object_list:
            album_list.append({'name':album.name, 'singer':album.singer, 'desc':album.desc})
        resp = {'error_msg': '', 'albums': album_list, 'total': p.count}
        return HttpResponse(content=simplejson.dumps(resp))
    elif request.method == 'DELETE':
        q = QueryDict(request.body)
        _id = q.get('id', None)
        if _id is not None:
            Album.objects.get(id__exact=_id).delete()
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'id is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    else:
        resp = {'error_msg': 'not support http method', 'id': ''}
        return HttpResponse(status=405, content=simplejson.dumps(resp))


# music_sub_type
def music_type(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        desc = request.POST.get('singer', '')
        if name is not None:
            # should check name existence
            music_type, not_exist = MusicType.objects.get_or_create(name=name)
            if not_exist:
                music_type.desc = desc
                music_type.save()
                resp = {'error_msg': '', 'id': music_type.id}
            else:
                resp = {'error_msg': 'record already exists', 'id': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'name is required', 'id': ''}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'PUT':
        q = QueryDict(request.body)
        _id = q.get('id', None)
        name = q.get('name', None)
        desc = q.get('desc', None)
        if _id is not None:
            # check name existence
            music_type = MusicType.objects.get(id__exact=_id)
            if name:
                music_type.name = name
            if desc:
                music_type.desc = desc
            music_type.save()
            resp = {'error_msg': '', 'id': music_type.id}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'id is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'GET':
        total = 0
        page_size = request.GET.get('page_size', 10)
        page = request.GET.get('page', 1)
        name = request.GET.get('name', None)
        desc = request.GET.get('desc', None)
        music_types = MusicType.objects
        if name is not None:
            music_types = music_types.filter(name=name)
        if desc is not None:
            music_types = music_types.filter(desc=desc)
        music_types = music_types.all()
        p = Paginator(music_types, page_size)
        music_type_list = []
        for music_type in p.page(page).object_list:
            music_type_list.append({'name':music_type.name, 'desc':music_type.desc})
        resp = {'error_msg': '', 'music_type': music_type_list, 'total': p.count}
        return HttpResponse(content=simplejson.dumps(resp))
    elif request.method == 'DELETE':
        q = QueryDict(request.body)
        _id = q.get('id', None)
        if _id is not None:
            MusicType.objects.get(id__exact=_id).delete()
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'id is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    else:
        resp = {'error_msg': 'not support http method', 'id': ''}
        return HttpResponse(status=405, content=simplejson.dumps(resp))


# music_sub_type
def music_sub_type(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        desc = request.POST.get('singer', '')
        if name is not None:
            # should check name existence
            music_sub_type, not_exist = MusicSubType.objects.get_or_create(name=name)
            if not_exist:
                music_sub_type.desc = desc
                music_sub_type.save()
                resp = {'error_msg': '', 'id': music_sub_type.id}
            else:
                resp = {'error_msg': 'record already exists', 'id': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'name is required', 'id': ''}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'PUT':
        q = QueryDict(request.body)
        _id = q.get('id', None)
        name = q.get('name', None)
        desc = q.get('desc', None)
        if _id is not None:
            # check name existence
            music_sub_type = MusicSubType.objects.get(id__exact=_id)
            if name:
                music_sub_type.name = name
            if desc:
                music_sub_type.desc = desc
            music_sub_type.save()
            resp = {'error_msg': '', 'id': music_sub_type.id}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'id is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'GET':
        page_size = request.GET.get('page_size', 10)
        page = request.GET.get('page', 1)
        name = request.GET.get('name', None)
        desc = request.GET.get('desc', None)
        music_sub_types = MusicSubType.objects
        if name is not None:
            music_sub_types = music_sub_type.filter(name=name)
        if desc is not None:
            music_sub_types = music_sub_type.filter(desc=desc)
        music_sub_types = music_sub_types.all()
        p = Paginator(music_sub_types, page_size)
        music_sub_type_list = []
        for music_sub_type in p.page(page).object_list:
            music_sub_type_list.append({'name':music_sub_type.name, 'desc':music_sub_type.desc})
        resp = {'error_msg': '', 'music_type': music_sub_type_list, 'total': p.count}
        return HttpResponse(content=simplejson.dumps(resp))
    elif request.method == 'DELETE':
        q = QueryDict(request.body)
        _id = q.get('id', None)
        if _id is not None:
            MusicSubType.objects.get(id__exact=_id).delete()
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'id is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    else:
        resp = {'error_msg': 'not support http method', 'id': ''}
        return HttpResponse(status=405, content=simplejson.dumps(resp))

# album, music_type relationship
def album_music_type(request):
    if request.method == 'POST':
        album_id = request.POST.get('album_id', None)
        music_type_ids = simplejson.loads(request.POST.get('music_type_ids', None))
        if album_id is not None and music_type_ids is not None:
            album = Album.objects.get(id__exact=album_id)
            for music_type_id in music_type_ids:
                music_type = MusicType.objects.get(id__exact=music_type_id)
                album.music_type.add(music_type)
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'album_id and music_type_ids is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'PUT':
        q = QueryDict(request.body.decode(encoding="utf-8"))
        album_id = q.get('album_id', None)
        music_type_ids = simplejson.loads(q.get('music_type_ids', None))
        if album_id is not None and music_type_ids is not None:
            album = Album.objects.get(id__exact=album_id)
            album.music_type.clear()
            for music_type_id in music_type_ids:
                music_type = MusicType.objects.get(id__exact=music_type_id)
                album.music_type.add(music_type)
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'album_id and music_type_ids is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'GET':
        page_size = request.GET.get('page_size', 10)
        page = request.GET.get('page', 1)
        album_id = request.GET.get('album_id', None)
        if album_id is not None:
            album = Album.objects.get(id__exact=album_id)
            music_types = album.music_type.all()
            p = Paginator(music_types, page_size)
            music_type_list = []
            for music_type in p.page(page).object_list:
                music_type_list.append({'name':music_type.name, 'desc':music_type.desc})
            resp = {'error_msg': '', 'music_type': music_type_list, 'album_id': album.id, 'total': p.count}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'album_id required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'DELETE':
        q = QueryDict(request.body.decode(encoding="utf-8"))
        album_id = q.get('album_id', None)
        music_type_ids = simplejson.loads(q.get('music_type_ids', None))
        if album_id is not None and music_type_ids is not None:
            album = Album.objects.get(id__exact=album_id)
            for music_type_id in music_type_ids:
                music_type = MusicType.objects.get(id__exact=music_type_id)
                album.music_type.remove(music_type)
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'album_id is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    else:
        resp = {'error_msg': 'not support http method', 'id': ''}
        return HttpResponse(status=405, content=simplejson.dumps(resp))

# music_type, music_sub_type relationship
def music_type_music_sub_type(request):
    if request.method == 'POST':
        music_type_id = request.POST.get('music_type_id', None)
        music_sub_type_ids = simplejson.loads(request.POST.get('music_sub_type_ids', None))
        if music_type_id is not None and music_sub_type_ids is not None:
            music_type = MusicType.objects.get(id__exact=music_type_id)
            for music_sub_type_id in music_sub_type_ids:
                music_sub_type = MusicSubType.objects.get(id__exact=music_sub_type_id)
                music_type.music_sub_type.add(music_sub_type)
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'music_type_id and music_type_ids is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'PUT':
        q = QueryDict(request.body.decode(encoding="utf-8"))
        music_type_id = q.get('music_type_id', None)
        music_sub_type_ids = simplejson.loads(q.get('music_sub_type_ids', None))
        if music_type_id is not None and music_sub_type_ids is not None:
            music_type = MusicType.objects.get(id__exact=music_type_id)
            music_type.music_sub_type_set.clear()
            for music_sub_type_id in music_sub_type_ids:
                music_sub_type = MusicSubType.objects.get(id__exact=music_sub_type_id)
                music_type.music_sub_type.add(music_sub_type)
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'music_type_id and music_sub_type_ids is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'GET':
        page_size = request.GET.get('page_size', 10)
        page = request.GET.get('page', 1)
        music_type_id = request.GET.get('music_type_id', None)
        if music_type_id is not None:
            music_type = MusicType.objects.get(id__exact=music_type_id)
            music_sub_types = music_type.music_sub_type.all()
            p = Paginator(music_sub_types, page_size)
            music_sub_type_list = []
            for music_sub_type in p.page(page).object_list:
                music_sub_type_list.append({'name':music_sub_type.name, 'desc':music_sub_type.desc})
            resp = {'error_msg': '', 'music_type': music_sub_type_list, 'music_type_id': music_type.id, 'total': p.count}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'music_type_id required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    elif request.method == 'DELETE':
        q = QueryDict(request.body.decode(encoding="utf-8"))
        music_type_id = q.get('music_type_id', None)
        music_sub_type_ids = simplejson.loads(q.get('music_sub_type_ids', None))
        if music_type_id is not None and music_sub_type_ids is not None:
            music_type = MusicType.objects.get(id__exact=music_type_id)
            for music_sub_type_id in music_sub_type_ids:
                music_sub_type = MusicSubType.objects.get(id__exact=music_sub_type_id)
                music_type.music_sub_type.remove(music_sub_type)
            resp = {'error_msg': ''}
            return HttpResponse(content=simplejson.dumps(resp))
        else:
            resp = {'error_msg': 'music_type_id is required'}
            return HttpResponse(status=400, content=simplejson.dumps(resp))
    else:
        resp = {'error_msg': 'not support http method', 'id': ''}
        return HttpResponse(status=405, content=simplejson.dumps(resp))
