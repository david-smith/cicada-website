from cicada.blog.models import Post
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('blog/index.html', {'latest_post_list' : post_list}, context_instance=RequestContext(request))

def read(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    return render_to_response('blog/read.html', {'post': p}, context_instance=RequestContext(request))


def main_page(request):
    p = Post.objects.latest('id')
    return render_to_response('home.html', {'post' : p}, context_instance=RequestContext(request))