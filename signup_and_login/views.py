from django.shortcuts import render
from .models import UserData
from django.shortcuts import redirect
from django.db.models import Q
from django. contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login,authenticate


def patient(request,user):

    if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            addressLine1 = request.POST.get('addressLine1')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            user_email = request.POST.get('user_email')

            UserData.objects.filter(username=user).update(first_name=first_name,last_name=last_name,addressLine1=addressLine1,city=city,state=state,pincode=pincode,user_email=user_email)

            first_name = UserData.objects.filter(username = user).values_list("first_name")
            last_name = UserData.objects.filter(username = user).values_list("last_name")
            addressLine1 = UserData.objects.filter(username = user).values_list("addressLine1")
            city = UserData.objects.filter(username = user).values_list("city")
            state = UserData.objects.filter(username = user).values_list("state")
            pincode = UserData.objects.filter(username = user).values_list("pincode")
            username = UserData.objects.filter(username = user).values_list("username")
            user_email = UserData.objects.filter(username = user).values_list("user_email")
            photo = UserData.objects.filter(username = user).values_list("photo")

            return render(request, "Patient.html",{'first_name':first_name[0][0],"addressLine1":addressLine1[0][0],"last_name":last_name[0][0],"username":username[0][0],"city":city[0][0],"state":state[0][0],"pincode":pincode[0][0],"user_email":user_email[0][0],"photo":photo[0][0]})      
            
    first_name = UserData.objects.filter(username = user).values_list("first_name")
    last_name = UserData.objects.filter(username = user).values_list("last_name")
    addressLine1 = UserData.objects.filter(username = user).values_list("addressLine1")
    city = UserData.objects.filter(username = user).values_list("city")
    state = UserData.objects.filter(username = user).values_list("state")
    pincode = UserData.objects.filter(username = user).values_list("pincode")
    username = UserData.objects.filter(username = user).values_list("username")
    user_email = UserData.objects.filter(username = user).values_list("user_email")
    photo = UserData.objects.filter(username = user).values_list("photo")
    return render(request, "Patient.html",{'first_name':first_name[0][0],"addressLine1":addressLine1[0][0],"last_name":last_name[0][0],"username":username[0][0],"city":city[0][0],"state":state[0][0],"pincode":pincode[0][0],"user_email":user_email[0][0],"photo":photo[0][0]})
    


def docter(request,user):

    if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            addressLine1 = request.POST.get('addressLine1')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            user_email = request.POST.get('user_email')

            UserData.objects.filter(username=user).update(first_name=first_name,last_name=last_name,addressLine1=addressLine1,city=city,state=state,pincode=pincode,user_email=user_email)

            first_name = UserData.objects.filter(username = user).values_list("first_name")
            last_name = UserData.objects.filter(username = user).values_list("last_name")
            addressLine1 = UserData.objects.filter(username = user).values_list("addressLine1")
            city = UserData.objects.filter(username = user).values_list("city")
            state = UserData.objects.filter(username = user).values_list("state")
            pincode = UserData.objects.filter(username = user).values_list("pincode")
            username = UserData.objects.filter(username = user).values_list("username")
            user_email = UserData.objects.filter(username = user).values_list("user_email")
            photo = UserData.objects.filter(username = user).values_list("photo")

            return render(request, "Docter.html",{'first_name':first_name[0][0],"addressLine1":addressLine1[0][0],"last_name":last_name[0][0],"username":username[0][0],"city":city[0][0],"state":state[0][0],"pincode":pincode[0][0],"user_email":user_email[0][0],"photo":photo[0][0]})      
            
    
    first_name = UserData.objects.filter(username = user).values_list("first_name")
    last_name = UserData.objects.filter(username = user).values_list("last_name")
    addressLine1 = UserData.objects.filter(username = user).values_list("addressLine1")
    city = UserData.objects.filter(username = user).values_list("city")
    state = UserData.objects.filter(username = user).values_list("state")
    pincode = UserData.objects.filter(username = user).values_list("pincode")
    username = UserData.objects.filter(username = user).values_list("username")
    user_email = UserData.objects.filter(username = user).values_list("user_email")
    photo = UserData.objects.filter(username = user).values_list("photo")
    return render(request, "Docter.html",{'first_name':first_name[0][0],"addressLine1":addressLine1[0][0],"last_name":last_name[0][0],"username":username[0][0],"city":city[0][0],"state":state[0][0],"pincode":pincode[0][0],"user_email":user_email[0][0],"photo":photo[0][0]})
    
    
 

def loginpage(request):

    try:

        if request.method == 'POST':
            username = request.POST.get('un')
            password = request.POST.get('pw')

            queryset_role = UserData.objects.filter(username=username).values_list("user_role")
            queryset_pw = UserData.objects.filter(username = username).values_list("user_password")

            if UserData.objects.filter(username = username).exists():
                    if(password == queryset_pw[0][0]):
                        if queryset_role[0][0] == "Patient":
                           return redirect("patient/"+username)
                        if queryset_role[0][0] == "Doctor":
                           return redirect("docter/"+username)
                    else:
                        messages.error(request,'Incorrect Password !')
                        return render(request, "index.html")
            else:
                messages.error(request,'Incorrect Username !')
                return render(request, "index.html")
    except Exception as e:
        print(e)

    return render(request, "index.html")


def signup(request):
    try:

        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            addressLine1 = request.POST.get('addressLine1')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            username = request.POST.get('username')
            user_email = request.POST.get('user_email')
            user_password = request.POST.get('user_password')
            confirmPassword = request.POST.get('confirmPassword')
            user_role = request.POST.get('user_role')            
            photo = request.FILES.get('photo')

            if user_password != confirmPassword :
                messages.error(request,"Note : The Password Doesn't Match! ")
                return render(request, "signup.html")
           
            elif UserData.objects.filter(username=username).exists():
                messages.error(request,"Note : Username Is Already Taken ! ")
                return render(request, "signup.html")

            else: 
                 UserData.objects.create(first_name=first_name,last_name=last_name,addressLine1=addressLine1,city=city,state=state,pincode=pincode,username=username,user_email=user_email,user_password=user_password,user_role=user_role,photo=photo)
                 return render(request, "index.html")
                
                 
                 
    except Exception as e:
        print(e)       
    
    return render(request, "signup.html")


    