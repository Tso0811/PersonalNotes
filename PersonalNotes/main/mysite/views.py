from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.views.generic import  CreateView
from mysite.models import Note
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def homepage(request) :
    if request.method == 'POST':
        title = request.POST['title']
        slug = request.POST['slug']
        content = request.POST['content']
        note = Note(title=title,slug=slug,content=content)
        note.save()
        return redirect('homepage')
    
    notes = Note.objects.all().order_by('-add_time')
    
    return render(request,'index.html',{'notes':notes})

def showdetail (request , slug ):
    detail = Note.objects.get(slug = slug)
    return render(request , 'showdetail.html' , locals())

def delete_note(request , note_slug): #從urls.py中取得slug
    if request.method == 'POST':
        note = get_object_or_404(Note, slug = note_slug) #如果找到指定的條件 會return 反之則return 404錯誤
        note.delete()
    return redirect('homepage')  
    


def edit_note(request , edit_note_slug):
    note = get_object_or_404(Note,slug=edit_note_slug)
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        content = request.POST.get('content')
        note.title = title
        note.slug = slug
        note.content = content
        note.save()

        return redirect('showdetail',slug = note.slug)
    return render(request , 'edit_note.html', {'note_dic': note}) #鍵是 'note'，而值是變數 note  用字典會比local()安全且快速

