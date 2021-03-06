from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .models import Blog, Comment

def main(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'main.html', context)

def detail(request, id):
    detail_data = get_object_or_404(Blog, pk=id)
    comments = Comment.objects.filter(blog_id = id)
    context = {
        'title' : detail_data.title,
        'writer' : detail_data.writer,
        'body' : detail_data.body,
        'pub_date' : detail_data.pub_date,
        'id' : id,
        'comments':comments,
        'image':detail_data.image,
    }
    return render(request, 'detail.html', context)

def create_page(request):
    return render(request, 'create.html')

def create(request):
    new_data = Blog()
    new_data.title = request.POST['title']
    new_data.writer = request.POST['writer']
    new_data.body = request.POST['body']
    new_data.image = request.FILES['image']
    new_data.pub_date = timezone.now()
    new_data.save()
    return redirect('main')

def update_page(request, id):
    update_data = get_object_or_404(Blog, pk=id)
    context = {
        'id' : id,
        'title' : update_data.title,
        'writer' : update_data.writer,
        'body' : update_data.body,
        'image' : update_data.image,
    }
    return render(request, 'update.html', context)

def update(request, id):
    update_data = get_object_or_404(Blog, pk=id)
    update_data.title = request.POST['title']
    update_data.writer = request.POST['writer']
    update_data.body = request.POST['body']
    update_data.pub_date = timezone.now()
    update_data.image = request.FILES['image']
    update_data.save()
    return redirect('main')

def delete(request, id):
    delete_data = get_object_or_404(Blog, pk=id)
    delete_data.delete()
    return redirect('main')


def create_comment(request, id):
    new_comment = Comment()
    blog_id = Blog.objects.get(pk=id)
    new_comment.blog_id = blog_id
    new_comment.user = request.POST['user']
    new_comment.content = request.POST['content']
    new_comment.pub_date = timezone.now()
    new_comment.save()

    return redirect('detail', id)

def delete_comment(request,id,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()

    return redirect('detail',id)

