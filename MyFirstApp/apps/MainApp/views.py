from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Item
from django.urls import reverse

def index(request):
    latest_items_list = Item.objects.order_by('-pub_date')[:5]
    return render(request, 'MainApp/list.html', {'latest_items_list': latest_items_list})

def item(request, item_id):
    try:
        item = Item.objects.get(id = item_id)
    except expression as identifier:
        raise Http404('Товара нет!')

    comments_list = item.comment_set.order_by('-id')[:10]

    return render(request, 'MainApp/item.html', {'items': item, 'comments_list': comments_list})

def leave_comment(request, item_id):
    try:
        item = Item.objects.get(id = item_id)
    except expression as identifier:
        raise Http404('Товара нет!')

    item.comment_set.create(author_name = request.POST['name'], text = request.POST['text'])

    return HttpResponseRedirect(reverse('main:item', args=(item.id,)))