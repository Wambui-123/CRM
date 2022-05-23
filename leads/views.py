from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm

# Create your views here.
def lead_list(request):
    # return HttpResponse("Hello world")
    leads = Lead.objects.all()
    context = {
        # "name": "Yvonne",
        # "age": 35
        "leads" : leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)

#Creating a form
def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        print('REcieving Post Request')
        form = LeadForm(request.POST)
        if form.is_valid():
            # print('Is valid')
            # print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent= agent
            )
            # print('Created Lead')
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)