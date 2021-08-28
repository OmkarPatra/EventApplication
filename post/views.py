from django.shortcuts import render,redirect, get_object_or_404
from .forms import PostForm
from django.views.generic import ListView,DetailView,CreateView,RedirectView
from .models import EventList
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
# Create your views here.

def LikeView(request,pk):
    post = EventList.objects.get(id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def getLikes(request):
    new = EventList.objects.filter(likes=request.user)
    return render(request,'post/liked-events.html',{'new':new})

class HomeView(ListView):
    model = EventList
    template_name = 'post/event-list.html'

def likePage(request):
    context = {}
    return render(request, 'post/liked-events.html', context)


class AddPostView(CreateView):
    model = EventList
    form_class = PostForm
    template_name = 'post/add-event.html'


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = EventList.objects.get(id=post_id)
        

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = EventList.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()

        # data = {
        #     'value': like.value,
        #     'likes': post_obj.liked.all().count()
        # }

        # return JsonResponse(data, safe=False)
    return redirect('home')