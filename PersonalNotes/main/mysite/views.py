from django.shortcuts import render , redirect , get_object_or_404
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

def delete_note(request , note_slug): #從urls.py中取得slug
    if request.method == 'POST':
        note = get_object_or_404(Note, slug = note_slug) #如果找到指定的條件 會return 反之則return 404錯誤
        note.delete()
    return redirect('/')  
    




