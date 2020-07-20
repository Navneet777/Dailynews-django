from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from crypto.models import Contactmodel , Subscribe
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.views import generic
import requests
import json

try:

            def index(request):
                index_request = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&pageSize=25&apiKey=104f79640cb24be5813b553c9c1352c4")
                index = json.loads(index_request.content)
                now = datetime.now().strftime('%H:%M:%S')
                return render(request,'index.html',{'index':index,'now':now})

            def index1(request):
                index_request = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&pageSize=1&apiKey=104f79640cb24be5813b553c9c1352c4")
                index1 = json.loads(index_request.content)
                now = datetime.now().strftime('%H:%M:%S')
                return render(request,'index1.html',{'index1':index1,'now':now})


            def home(request):
                # Crypto price data
                price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
                price = json.loads(price_request.content)
                return render(request, 'home.html', {'price':price})
                # ---------------About Section-------------------
            def about(request):
                return render(request,'about.html')

            # ---------------News Section-------------------
            def map(request):
                return render(request, 'map.html')
            def post(request , post_id=id):
                item = get_object_or_404(Post, id=post_id)
                return render(request, 'post.html' ,{'post':item})
            def news(request):
                api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
                api = json.loads(api_request.content)
                return render(request, 'news.html', {'api':api})
            def que(request):
                que_request = requests.get("https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&pageSize=40&apiKey=104f79640cb24be5813b553c9c1352c4")
                que = json.loads(que_request.content)
                return render(request,'que.html',{'que':que})
    #-----------------india news -------------------
            def india(request):

                return render(request,'india.html')
    #-----------------india sports news -------------------
            def indiasport(request):
                indiasport_request = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&pageSize=60&apiKey=104f79640cb24be5813b553c9c1352c4")
                indiasport = json.loads(indiasport_request.content)
                return render(request,'indiasport.html',{'indiasport':indiasport})
            #-----------------india technology news -------------------
            def indiatechnology(request):
                indiatechnology_request = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&pageSize=60&apiKey=104f79640cb24be5813b553c9c1352c4")
                indiatechnology = json.loads(indiatechnology_request.content)
                return render(request,'indiatechnology.html',{'indiatechnology':indiatechnology})
            #-----------------india Entertainment news -------------------
            def indiaEntertainment(request):
                indiaEntertainment_request = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&pageSize=60&apiKey=104f79640cb24be5813b553c9c1352c4")
                indiaEntertainment = json.loads(indiaEntertainment_request.content)
                return render(request,'indiaEntertainment.html',{'indiaEntertainment':indiaEntertainment})
            #-----------------india Science news -------------------
            def indiascience(request):
                indiascience_request = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&pageSize=60&apiKey=104f79640cb24be5813b553c9c1352c4")
                indiascience = json.loads(indiascience_request.content)
                return render(request,'indiascience.html',{'indiascience':indiascience})
    #-----------------india Bussiness news -------------------
            def indiaBussiness(request):
                indiaBussiness_request = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&pageSize=60&apiKey=104f79640cb24be5813b553c9c1352c4")
                indiaBussiness = json.loads(indiaBussiness_request.content)
                return render(request,'indiaBussiness.html',{'indiaBussiness':indiaBussiness})
            #-----------------USA  news -------------------
            def usa(request):

                return render(request,'usa.html')
            #-----------------USA sports news -------------------
            def usasport(request):
                usasport_request = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=104f79640cb24be5813b553c9c1352c4")
                usasport = json.loads(usasport_request.content)
                return render(request,'usasport.html',{'usasport':usasport})
            #-----------------USA technology news -------------------
            def usatechnology(request):
                usatechnology_request = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=technology&pageSize=60&apiKey=104f79640cb24be5813b553c9c1352c4")
                usatechnology = json.loads(usatechnology_request.content)
                return render(request,'usatechnology.html',{'usatechnology':usatechnology})
            #-----------------USA Entertainment news -------------------
            def usaEntertainment(request):
                usaEntertainment_request = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=entertainment&pageSize=60&apiKey=104f79640cb24be5813b553c9c1352c4")
                usaEntertainment = json.loads(usaEntertainment_request.content)
                return render(request,'usaEntertainment.html',{'usaEntertainment':usaEntertainment})
            #-----------------USA Science news -------------------
            def usascience(request):
                usascience_request = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=104f79640cb24be5813b553c9c1352c4")
                usascience = json.loads(usascience_request.content)
                return render(request,'usascience.html',{'usascience':usascience})
            #-----------------USABussiness news -------------------
            def usaBussiness(request):
                usaBussiness_request = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=104f79640cb24be5813b553c9c1352c4")
                usaBussiness = json.loads(usaBussiness_request.content)
                return render(request,'usaBussiness.html',{'usaBussiness':usaBussiness})
            def russia(request):

                return render(request,'russia.html')
            #-----------------russia sports news -------------------
            def russiasport(request):
                russiasport_request = requests.get("https://newsapi.org/v2/top-headlines?country=ru&category=sports&apiKey=104f79640cb24be5813b553c9c1352c4")
                russiasport = json.loads(russiasport_request.content)
                return render(request,'russiasport.html',{'russiasport':russiasport})
            #-----------------russia technology news -------------------
            def russiatechnology(request):
                russiatechnology_request = requests.get("https://newsapi.org/v2/top-headlines?country=ru&category=technology&apiKey=104f79640cb24be5813b553c9c1352c4")
                russiatechnology = json.loads(russiatechnology_request.content)
                return render(request,'russiatechnology.html',{'russiatechnology':russiatechnology})
            #-----------------russia Entertainment news -------------------
            def russiaEntertainment(request):
                russiaEntertainment_request = requests.get("https://newsapi.org/v2/top-headlines?country=ru&category=entertainment&apiKey=104f79640cb24be5813b553c9c1352c4")
                russiaEntertainment = json.loads(russiaEntertainment_request.content)
                return render(request,'russiaEntertainment.html',{'russiaEntertainment':russiaEntertainment})
            #-----------------russia Science news -------------------
            def russiascience(request):
                russiascience_request = requests.get("https://newsapi.org/v2/top-headlines?country=ru&category=science&apiKey=104f79640cb24be5813b553c9c1352c4")
                russiascience = json.loads(russiascience_request.content)
                return render(request,'russiascience.html',{'russiascience':russiascience})
            #-----------------russia Bussiness news -------------------
            def russiaBussiness(request):
                russiaBussiness_request = requests.get("https://newsapi.org/v2/top-headlines?country=ru&category=business&apiKey=104f79640cb24be5813b553c9c1352c4")
                russiaBussiness = json.loads(russiaBussiness_request.content)
                return render(request,'russiaBussiness.html',{'russiaBussiness':russiaBussiness})
            #---------------china news -----------------------
            def china(request):

                return render(request,'china.html')
            #-------china sports news-----------
            def chinasport(request):
                chinasport_request = requests.get("https://newsapi.org/v2/top-headlines?country=cn&category=sports&apiKey=104f79640cb24be5813b553c9c1352c4")
                chinasport = json.loads(chinasport_request.content)
                return render(request,'chinasport.html',{'chinasport':chinasport})
            #--
            def chinatechnology(request):
                chinatechnology_request = requests.get("https://newsapi.org/v2/top-headlines?country=cn&category=technology&apiKey=104f79640cb24be5813b553c9c1352c4")
                chinatechnology = json.loads(chinatechnology_request.content)
                return render(request,'chinatechnology.html',{'chinatechnology':chinatechnology})
            #-----------------china Entertainment news -------------------
            def chinaEntertainment(request):
                chinaEntertainment_request = requests.get("https://newsapi.org/v2/top-headlines?country=cn&category=entertainment&apiKey=104f79640cb24be5813b553c9c1352c4")
                chinaEntertainment = json.loads(chinaEntertainment_request.content)
                return render(request,'chinaEntertainment.html',{'chinaEntertainment':chinaEntertainment})
            #-----------------china Science news -------------------
            def chinascience(request):
                chinascience_request = requests.get("https://newsapi.org/v2/top-headlines?country=cn&category=science&apiKey=104f79640cb24be5813b553c9c1352c4")
                chinascience = json.loads(chinascience_request.content)
                return render(request,'chinascience.html',{'chinascience':chinascience})
            #-----------------china Bussiness news -------------------
            def chinaBussiness(request):
                chinaBussiness_request = requests.get("https://newsapi.org/v2/top-headlines?country=cn&category=business&apiKey=104f79640cb24be5813b553c9c1352c4")
                chinaBussiness = json.loads(chinaBussiness_request.content)
                return render(request,'chinaBussiness.html',{'chinaBussiness':chinaBussiness})
            #--------------Headlines Section-------------------
            def Topbcc_headlines(request):
                bbc_request = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=104f79640cb24be5813b553c9c1352c4")
                bbcresponse = json.loads(bbc_request.content)
                return render(request,'topheadlinesbbcnews.html',{'bbcresponse':bbcresponse})

            def Topusa_headlines(request):
                usa_request = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=104f79640cb24be5813b553c9c1352c4")
                usaheadlines = json.loads(usa_request.content)
                return render(request,'uktopheadlines.html',{'usaheadlines':usaheadlines})

            def Topgermany_headlines(request):
                germany_request = requests.get("https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=104f79640cb24be5813b553c9c1352c4")
                germanyheadlines = json.loads(germany_request.content)
                return render(request,'topheadlinesgermany.html',{'germanyheadlines':germanyheadlines})

            def bitcoinartical(request):
                bitcoinnews_request = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=104f79640cb24be5813b553c9c1352c4")
                bitcoinresponse = json.loads(bitcoinnews_request.content)
                return render(request,'bitcoinartical.html',{'bitcoinresponse':bitcoinresponse})



            #-----------------SignUp coding----------------

            def Signup(request):
                if request.method =="POST":
                    username = request.POST['name']
                    email = request.POST['email']
                    password = request.POST['password']
                    password1 = request.POST['password1']

                    if password != password1 :
                            messages.success(request,' Confirm Password Not Match Please Enter Password Again.')
                            return render(request,'signup.html')
                    else:
                        if User.objects.filter(username=username).exists():
                            messages.success(request,'Username Already Taken')
                            return render(request,'signup.html')

                        elif User.objects.filter(email=email).exists():
                            messages.success(request,'Email Address Already Taken.')
                            return render(request,'signup.html')
                        else:
                            if email.endswith('@gmail.com') or email.endswith('@outlook.com') or email.endswith('@rediffmail.com') or email.endswith('@yahoo.com') :
                                entry = User.objects.create_user(username=username,email=email,password=password)
                                entry.save()
                                messages.success(request,'Account Created Successfully..Please Login')
                                return HttpResponseRedirect(reverse('index'))
                            else:
                                messages.success(request,'Please Enter Valid Email ID or Email Providers.')
                                return redirect('Signup')
                return render(request,'signup.html')
            def loginuser(request):
                if request.method =="POST":
                    username = request.POST['name']
                    password = request.POST['password']

                    user = auth.authenticate(username=username,password=password)
                    if user is not None:
                        auth.login(request,user)
                        return redirect('index')
                    else:
                        messages.success(request,'Please Enter Valid Username or Password')
                        return redirect('loginuser')
                return render(request,'signin.html')
            def Logout(request):
                auth.logout(request)
                return redirect('/')

            def Contactus(request):

                if request.method == "POST":
                    name = request.POST['name']
                    email = request.POST['email']
                    message = request.POST['message']
                    if name is not None:
                        if email is not None:
                            if message is not None:
                                if not email.endswith('@example.com'):
                                    messages.success(request,'Please Enter Valid Email Address.')
                                    return redirect('Signup')
                                else:
                                    if email.endswith('@gmail.com') or email.endswith('@outlook.com') or email.endswith('@rediffmail.com') or email.endswith('@yahoo.com') :
                                        entry = Contactmodel.objects.create(name=name,email=email,messages=message)
                                        entry.save()
                                        messages.success(request,'Your Message send Successfully..')
                                        return HttpResponseRedirect(reverse('index'))
                                    else:
                                        messages.success(request,'Enter Valid Email Provider Email ID')
                                        return redirect('Signup')
                else:
                    messages.success(request,'Please Fill all fields..')
                    return redirect('All in one/indexuser.html')
                return render(request,'signup.html')

            def fblogin(request):
                return render(request,'fblogin.html')

            def forgetpass(request):
                if request.method == "POST":

                    username = request.POST['name']
                    email = request.POST['email']
                    password = request.POST['password']
                    password1 = request.POST['password1']

                    if password != password1:
                        messages.success(request,'Password and Confirm Password is not Match Please Enter Again.')
                        return render (request,'forgetpass.html')

                    if User.objects.filter(username=username,email=email).exists() is False:
                        messages.success(request,'Username or Email  is not Match Please Enter Again.')
                        return HttpResponseRedirect(reverse('forgetpass'))

                    else:
                        if User.objects.filter(username=username,email=email).exists():
                            u = User.objects.get(username=username,email=email)
                            u.set_password(password)
                            u.save()
                            messages.success(request,'Your Password Successfully Updated Please Login.')
                            return HttpResponseRedirect(reverse('loginuser'))
                return render(request,'forgetpass.html')

            def subscribe(request):
                if request.method =="POST":
                    email = request.POST['email']
                    if  email is str(''):
                            messages.success(request,'Please Enter Valid Email Address.')
                            return redirect('Signup')

                    else:
                        if email.endswith('@gmail.com') or email.endswith('@outlook.com') or email.endswith('@rediffmail.com') or email.endswith('@yahoo.com') :
                            sub = Subscribe.objects.create(email=email)
                            sub.save()
                            messages.success(request,'Your Subscribe is successfully done.')
                            return HttpResponseRedirect(reverse('index'))

                return render(request, 'All in one/indexuser.html', )

except:
        print("file request api not import perfectly ")
