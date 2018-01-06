from django.shortcuts import render
from wotlogin.models import *
from wotlogin.functions import *
import random
import string
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'wotlogin/index.html')



def guestlogin(request):
    user_name = ''.join([random.choice(string.ascii_uppercase + string.digits) for s in range(10)])
    user = User.objects.create_user(user_name, 'guest@pai.com', '111111')
    user.last_name = 'guest'
    user.save()
    pet = Pet(user = user, pettype="unknown")
    pet.save()
    petevent = PetEvent(pet = pet, eventtype = "disease", discription = request.POST['description'], date = datetime.now(), addedinfo = "", potentialinfo = "")
    petevent.save()
    userinfo = UserInfo(user = user, currentpet = pet.id, currentevent=petevent.id) 
    userinfo.save()
    user = authenticate(request, username = user_name, password = '111111')
    login(request, user)
    return HttpResponseRedirect(reverse('wotlogin:result'))

def result(request):
    userinfo = request.user.userinfo_set.all()[0]
    petevent = PetEvent.objects.get(pk=userinfo.currentevent) 
    if request.method == "POST":
        if request.POST["selected"].split("_")[0] == "add":
            templist = [i for i in petevent.addedinfo.split(',') if len(i)>0]
            templist.append(petevent.potentialinfo.split(',')[int(request.POST["selected"].split("_")[1])-1])
            petevent.addedinfo = ','.join(templist)
        else:
            templist =  petevent.addedinfo.split(',')
            del templist[int(request.POST["selected"].split("_")[1])-1]
            petevent.addedinfo = ','.join(templist)
            petevent.save()
    sentence = petevent.discription + " ".join(petevent.addedinfo.split(","))
    #calculation
    features = WordExtractor(sentence)
    output = DiseaseMapping(features)
    addedinfo = petevent.addedinfo.split(',')
    addedinfo = [i for i in addedinfo if len(i)>0]
    potentialinfo = CalculatePotentialInfo(output)
    petevent.potentialinfo = ','.join(potentialinfo)
    petevent.save()
    showform = GenerateShowForm(addedinfo, potentialinfo, output)

    return render(request, 'wotlogin/result.html', {"addedinfo": showform["addedinfo"], "potentialinfo": showform["potentialinfo"], "output": showform["output"]})    
