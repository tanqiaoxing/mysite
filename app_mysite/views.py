from django.shortcuts import render
from app_mysite.models import BlogsPost

# Create your views here.
def blog_index(request):
	blog_list = BlogsPost.objects.all()
	return render(request, 'index.html', {'blog_list':blog_list})