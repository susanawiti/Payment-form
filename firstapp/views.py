from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from firstapp.forms import PaymentForm
from .serializers import AboutSerializer
from rest_framework import viewsets
from .models import About
# from firstapp.models import Home

# Create your views here.
def payment(request):
    
    context = {'form': payment}
    if request.method == "POST":
        form = payment(request.POST)
        if form.is_valid():
                form.save()
                return redirect('payment_index.html')
        else :
            return render_to_response('payment_index.html', 
                          {'form': form})
                         
    else :
        return render(
            request,
            'payment_index.html',
            context
        )


        
        
def about(request) : 
    return render(request,'about.html')
class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer       
        
        
        
        
        
        
        
        
        
        
        
        
        
    