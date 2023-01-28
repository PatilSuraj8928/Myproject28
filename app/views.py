from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_data(request):
    if request.method == 'POST':
        a=request.POST['Sport']              # value = dict_name[key]
        T=Topic.objects.get_or_create(Topic_name=a)[0]
        T.save()

        b=request.POST['Player']
        c=request.POST['URL']
        W=Webpage.objects.get_or_create(Topic_name=T,Name=b,URL=c)[0]
        W.save()

        d=request.POST['Date']
        A=Access_Recod.objects.get_or_create(Name=W,Date=d)[0]
        A.save()

        return HttpResponse('Info Insertrd')

    return render(request, 'insert_data.html')

def Display_models(request):
    QST=Topic.objects.all()
    QSW=Webpage.objects.all()
    QSA=Access_Recod.objects.all()
    d={'Topic':QST, 'Webpage':QSW, 'Access':QSA}
    return render(request, 'Display_models.html',d)