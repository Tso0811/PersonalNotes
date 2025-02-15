from django.shortcuts import render , redirect
from django.http import HttpResponse
from mysite.models import Note
# Create your views here.

def homepage(request) :
    if request.method == 'POST':
        title = request.POST['title']
        slug = request.POST['slug']
        content = request.POST['content']
        note = Note(title=title,slug=slug,content=content)
        note.save()
        return redirect('/')
    notes = Note.objects.all()
    note_list = list()
    for count , note in enumerate (notes,start=1) :
        note_list.append('NO:{}:'.format(count)+str(note)+'<br>')
    return render(request,'index.html',locals())

def showdetail (request , slug ):
    detail = Note.objects.get(slug = slug)
    return render(request , 'showdetail.html' , locals())
