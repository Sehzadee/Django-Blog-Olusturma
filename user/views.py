from django.shortcuts import redirect, render
from  . forms import ResgisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages



# Create your views here.
def register(request):
    
    
        form = ResgisterForm(request.POST or None)
        if form.is_valid():  
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            
            newUser= User(username = username)
            newUser.set_password(password)
            
            newUser.save()
            login(request,newUser)
            messages.info(request, 'Başarıyla Kayıt Oldunuz...')
            return redirect("index")
        
        context= {
        "form": form
        }
        return render (request, "register.html",context)    
    
def loginUser(requset):
    form= LoginForm(requset.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")
        
        user = authenticate(username = username,password=password)
        
        if user is None : #Böyle Bir Kullanıcı Yoksa!!
            messages.info(requset,"Kullanıcı Adı veya Parola Hatalı")
            return render(requset, "login.html",context)
        # Kullanıcı varsa User varsa İf Blogu Çalışmaz...
        messages.success(requset,"Başarıyla Giriş Yaptınız.")
        login(requset,user)
        return redirect ("index")
    # form is valid değilse yani bir hata ile karşılaşıldıysa
    return render (requset, "login.html",context)
def logoutUser(requset):
    logout(requset)
    messages.success(requset,"Başarıyla Çıkış Yaptınız")
    return redirect("index")