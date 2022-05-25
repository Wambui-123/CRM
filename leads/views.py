from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# CRUD+L- CREATE RETRIEVE UPDATE DELETE + LIST
class LandingPageView(TemplateView):
    template_name = 'landing.html'

def landing_page(request):
    return render(request, "landing.html")
    
class LeadListView(ListView): 
    template_name = 'leads/lead_list.html'  
    queryset = Lead.objects.all()
    context_object_name = 'leads'
     
def lead_list(request):
    # return HttpResponse("Hello world")
    leads = Lead.objects.all()
    context = {
        # "name": "Yvonne",
        # "age": 35
        "leads" : leads
    }
    return render(request, "leads/lead_list.html", context)

class LeadDetailView(DetailView): 
    template_name = 'leads/lead_detail.html'  
    queryset = Lead.objects.all()
    context_object_name = 'lead'

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)

#Creating a form
class LeadCreateView(CreateView): 
    template_name = 'leads/lead_create.html'  
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads: lead-list')
    
    
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print('Recieving Post Request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

# Updating forms
class LeadUpdateView(UpdateView): 
    template_name = 'leads/lead_update.html'  
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    context_object_name = 'lead'
    
    def get_success_url(self):
        return reverse('leads:lead-list')
    

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance = lead)
    if request.method == "POST":
        print('Recieving Post Request')
        form = LeadModelForm(request.POST, instance = lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        "form": form,
         "lead": lead
    }
    return render(request, "leads/lead_update.html", context)

# delete
class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html' 
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse('leads:lead-list')
 
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')
    


# def lead_update(request, pk):
    # lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('Is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             # Updating
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect('/leads')
    # context = {
    #     "form": form,
    #      "lead": lead
    # }
#     return render(request, "leads/lead_update.html", context)

    
# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         print('REcieving Post Request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('Is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = form.cleaned_data['agent']
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent= agent
#             )
#             print('Created Lead')
#             return redirect('/leads')
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)