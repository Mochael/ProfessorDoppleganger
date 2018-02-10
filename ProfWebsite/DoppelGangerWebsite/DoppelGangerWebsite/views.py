from django.views.generic import View
from database.models import Professors, User
from django.shortcuts import render

class MainPage(View):
#    def loadMatch(self, request):
#        match = Professors.match(userPicInput)
#        return render(request, "index.html", match)

    def post(self, request):
        form = User(request.POST)
        return render(request, "index.html", {"form":form})