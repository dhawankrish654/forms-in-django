from django.shortcuts import render
from basicapp.forms import NewUserForm


def index(request):
    return render(request,'basicapp/index.html')


def users(request):
    form=NewUserForm()
    if(request.method=="post"):
        form=NewUserForm(request.post)

        if(form.is_valid()):
            form.save(commit=True)
            return index(request)
        else:
            print("error")
            return render(request,'basicapp/users.html',{'form':form})
    return render(request,'basicapp/users.html',{'form':form})



# Create your views here.
