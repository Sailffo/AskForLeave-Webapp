from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from django.urls import reverse

# Create your views here.
def update_comment(request):
    user = request.user
    text = request.POST['text']
    content_type = request.POST['content_type']
    object_id = request.POST['object_id']
    model_class = ContentType.objects.get(model=content_type).model_class()
    model_obj = model_class.objects.get(pk = object_id)

    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_type = model_obj
    comment.save()

    referer = request.META.get('HTTP_REFERER',reverse('home'))
    return redirect(referer)