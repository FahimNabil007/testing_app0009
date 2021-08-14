from django.shortcuts import render
from tester.models import Post

# Create your views here.
def tester(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'tester.html')  
        

        else:
                return render(request,'tester.html')
        
      
            return render(request, "success.html")
def success(request):
                return render(request, 'success.html')
