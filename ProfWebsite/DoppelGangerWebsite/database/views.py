from django.views.generic.base import View
from database.models import Professors, User
from database.forms import UserForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from database import Testing


class MainPage(View):
    form_class = UserForm
    template_name = "index.html"

    def get(self, request):
        return render(request, "index.html")
#    def loadMatch(self, request):
#        match = Professors.match(userPicInput)
#        return render(request, "index.html", match)


    def model_form_upload(request):
        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            url = 'none'
            if form.is_valid():
                url = form.cleaned_data['image']
                print(url)
            context = {}
            posts = User.objects.last()
            context["posts"] = posts

            professorName = Testing.main(url)
            shortName = professorName[:-4]
            context["name"]=shortName

            url2 = 'https://github.com/Mochael/ProfessorDoppleganger/blob/master/ProfImages/'+professorName.replace(' ', '%20')+'?raw=true'
            context["url"] = url2
            return render(request, "compare.html", context)









            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('compare')
        else:
            form = UserForm()
        return render(request, 'index.html', {
            'form': form
        })

class ComparePage(View):
    def get(self, request):
        
        form = UserForm(request.POST, request.FILES)
        url = 'none'
        if form.is_valid():
            url = form.cleaned_data['url']
            print(url)
        context = {}
        posts = User.objects.last()
        context["posts"] = posts
        context["url"] = url

        return render(request, "compare.html", context)


'''    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('model_form_upload.html')
        return render(request, 'model_form_upload.html', {'form': form})'''
    
'''class MainPage(View):

    def SaveProfile(self, request):
        saved = False
    
        if request.method == "POST":
            #Get the posted form
            MyProfileForm = UserForm(request.POST, request.FILES)
            
            if MyProfileForm.is_valid():
                profile = User()
                profile.image = MyProfileForm.cleaned_data["picture"]
                profile.save()
                saved = True
        else:
            MyProfileForm = User()
                
        return render(request, 'index.html', locals())'''