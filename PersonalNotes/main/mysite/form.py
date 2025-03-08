from django import forms
from mysite.models import Note

class NoteForm (forms.ModelForm):
    class Meta :
        model = Note
        fields = ['title' , 'slug' , 'content']
    
    def clean_slug(self):
        slug = self.cleaned_data['slug'] #self.cleaned_data 是 Django 表單提供的一個字典 會初步檢查格式或是否有多餘的空格
        if Note.objects.filter(slug=slug).exclude(pk = self.instance.pk).exists(): #檢查資料庫中是否存在 slug 相同但 primary key 不同的 Note 物件
            raise forms.ValidationError('此slug已經存在')
        else:
            return  slug

