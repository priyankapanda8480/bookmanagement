from django.shortcuts import render, redirect
from .models import BookData
import datetime
def mainpage(request):
    data = BookData.objects.all()
    return render(request,'mainpage.html', {'data':data})
# Create your views here.
def addBooks(request):
    return render(request,'addBooks.html')
def addBooks(request):
    if request.method == 'GET':
        return render(request, 'addBooks.html')
    else:
        BookData(
        book_name = request.POST.get('bname'),
        author_name = request.POST.get('authname'),
        book_id =request.POST.get('bookid'),
        book_price =request.POST.get('bookprice')
        ).save()
        return redirect('mainpage')
def update(request, id):
    data = BookData.objects.get(id=id)
    return render(request,'update.html',{'data':data})

def update_data(request,id):
    data = BookData.objects.get(id=id)
    data.book_name=request.POST.get('bname')
    data.author_name=request.POST.get('authname')
    data.book_id=request.POST.get('bookid')
    data.book_price=request.POST.get('bookprice')
    data.save()
    return redirect('mainpage')
def delete(request, id):
    data = BookData.objects.get(id=id)
    data.delete()
    
    return redirect('mainpage')
