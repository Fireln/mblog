from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Post,Group
from datetime import datetime
# Create your views here.

def homepage(request):
    """
    主页
    :param request: 
    :return: 
    """
    template = get_template('index.html')
    posts = Post.objects.all()
    groups = Group.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
def showpost(request,id):
    """
    博客详情页
    :param request: 
    :param id: 
    :return: 
    """
    template = get_template('post.html')
    try:
        post = Post.objects.get(id=id)
        groups = Group.objects.all()
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def post_list(requesr,id):
    """
    博客列表页
    :param requesr: 
    :param group_id: 
    :return: 
    """
    template = get_template('postlist.html')
    try:
        groups = Group.objects.all()
        group = Group.objects.get(id=id)
        post_list = Post.objects.filter(group_id=id)
        if post_list != None:
            html = template.render(locals())
            return HttpResponse(html)

    except:
        return redirect(
            '/'
        )

def writeblog(requesr):
    template = get_template('writeblog.html')
    try:
        groups = Group.objects.all()
        html = template.render(locals() )
        return HttpResponse(html)
    except:
        redirect('/')

def wblog(request):
    if request.POST:
        title = request.POST['title']
        group = request.POST['group']
        content = request.POST['content']
    try:
        group_id = Group.objects.get(group_name=group)
        Post(title=title,group_id=group_id,body=content)
        Post.save()
        return redirect('/')
    except:
        redirect('/')