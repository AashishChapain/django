from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post


class PostListView(ListView):

    posts = post.objects.all()

    model = post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = post
    template_name = 'detail_view.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    template_name = 'post-create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    template_name = 'post-create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = post
    template_name = 'delete_post.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about_view(request):
    return render(request, 'about.html')


def invoice(request):
    return render(request, 'invoice.html')

