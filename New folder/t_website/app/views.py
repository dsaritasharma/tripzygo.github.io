from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import packageform
# from django.views.decorators.csrf import csrf_protect 
from .models import myuser,contact
# from django.views.decorators.csrf import csrf_exempt
 

def register(request):
    if request.method == 'POST':
    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if myuser.objects.filter(username=username).exists():
                messages.warning(request, 'Username exists')
                return redirect('/')
            else:
                if myuser.objects.filter(email=email).exists():
                    messages.warning(request, 'email already exists')
                    return redirect('/')
                else:
                    user=myuser (username=username, email=email, password=password,
                                 confirm_password=confirm_password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login') 
        else:
            messages.warning(request, 'Password do not match')
            return redirect('/')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if  myuser.objects.filter(username=username):
            if myuser.objects.filter(password=password):
                request.session['saved_username']=username
                request.session['saved_password']=password
                
                return redirect('index')
        else:
            messages.warning(request, "'Invalid credentials'")
            return redirect('index ')
        
    return render(request, 'login.html')
 
def index(request):
    new = packageform
    return render(request,"index.html", context={"packageform":new})



def logout(request):
        return render(request, 'login.html')
    


def contacts(request):
    if request.method == 'POST':
        
        name= request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        next_destination= request.POST['next_destination']
        no_of_passanger=request.POST['no_of_passanger']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        share_your_message=request.POST['share_your_message']
        
    
        info=contact(name=name, email=email, phone=phone,next_destination=next_destination,
                                 no_of_passanger=no_of_passanger,start_date=start_date,
                                 end_date=end_date,share_your_message=share_your_message)
        info.save()

    return render(request, 'contact.html')

