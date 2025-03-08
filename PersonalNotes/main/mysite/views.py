from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import  CreateView
from mysite.models import Note
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse , reverse_lazy
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from mysite.form import NoteForm

# Create your views here.
@login_required
def homepage(request):
    if request.method == 'POST':
        form = NoteForm(request.POST) #處裡表單 表單的欄位在NoteForm中定義 圖像則在html檔案中顯示
        if form.is_valid():
            note = form.save(commit=False) #儲存表單但不提交
            note.user = request.user # 將當前使用者指派給 note 的 user 欄位
            note.save()
            return redirect('homepage')
    else :
        form = NoteForm()
    
    notes = Note.objects.filter(user=request.user).order_by('-add_time')  # Note.objects.all()，會顯示所有筆記 用過濾器只顯示目前使者的筆記
    return render(request, 'index.html', {'notes': notes, 'form': form})
        
@login_required
def showdetail (request , slug ):
    detail = get_object_or_404(Note , slug = slug , user = request.user) #加入判斷使用者 避免非使用者輸入url來查看其他人的筆記
    return render(request , 'showdetail.html' , {'detail' : detail})

@login_required
def delete_note(request , slug): #從urls.py中取得slug
    note = get_object_or_404(Note , slug = slug , user = request.user )
    if request.method == 'POST':
        note.delete()
    return redirect('homepage')  
    

@login_required
def edit_note(request , edit_note_slug):
    note = get_object_or_404(Note , slug = edit_note_slug , user = request.user)
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

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))
    username = request.POST.get('username') #從表單中的name取得資料
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('homepage'))
    else:
        return render(request, 'login.html', locals())
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

class sign_up(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'

