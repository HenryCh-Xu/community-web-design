from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import lost_find_topic
from .models import lost_find_entry
from .models import electronics_topic
from .models import electronics_entry
from .models import necessary_topic
from .models import necessary_entry
from .forms import LFT_Form
from .forms import LFT_EntryForm
from .forms import ET_Form
from .forms import ET_EntryForm
from .forms import NT_Form
from .forms import NT_EntryForm


# Create your views here.

def index(request):
    return render(request, 'webpages/index.html')

def topics(request):
    topics = Topic.objects.order_by('date')
    context = {'topics': topics}
    return render(request, 'webpages/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'webpages/topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id) 

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('webpages:topic',\
                                                args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'webpages/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webpages:topic',\
                                                args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'webpages/edit_entry.html', context)

def classification(request):
    return render(request, 'webpages/classification.html')

def for_sale(request):
    return render(request, 'webpages/for_sale/for_sale.html')

def community(request):
    return render(request, 'webpages/community/community.html')

def studying(request):
    return render(request, 'webpages/studying/studying.html')

def school(request):
    return render(request, 'webpages/school/school.html')

#community
    #失物招领
def L_F(request):
    L_F = lost_find_topic.objects.order_by('L_F_T_date')
    context = {'L_F': L_F}
    return render(request, 'webpages/community/lost_find.html', context)
    
def L_F_T(request, L_F_T_id):
    L_F_T = lost_find_topic.objects.get(id=L_F_T_id)
    L_F_T_entries = L_F_T.lost_find_entry_set.order_by('L_F_T_date')
    context = {'L_F_T':L_F_T, 'L_F_T_entries':L_F_T_entries}
    return render(request, 'webpages/community/lost_find_topic.html', context)

def LFT_new_topic(request):
    if request.method != 'POST':
        form = LFT_Form()
    else:
        form = LFT_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webpages:lost_find'))
    context = {'form':form}
    return render(request, 'webpages/community/LFT_new_topic.html', context)

def LFT_new_entry(request, L_F_T_id):
    L_F_T = lost_find_topic.objects.get(id=L_F_T_id) 

    if request.method != 'POST':
        form = LFT_EntryForm()
    else:
        form = LFT_EntryForm(data=request.POST)
        if form.is_valid():
            LFT_new_entry = form.save(commit=False)
            LFT_new_entry.L_F_T = L_F_T
            LFT_new_entry.save()
            return HttpResponseRedirect(reverse('webpages:lost_find_topic',\
                                                args=[L_F_T_id]))
    context = {'L_F_T': L_F_T, 'form': form}
    return render(request, 'webpages/community/LFT_new_entry.html', context)

def LFT_edit_entry(request, L_F_E_id):
    L_F_E = lost_find_entry.objects.get(id=L_F_E_id)
    L_F_T = L_F_E.L_F_T
    if request.method != 'POST':
        form = LFT_EntryForm(instance=L_F_E)
    else:
        form = LFT_EntryForm(instance=L_F_E, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webpages:lost_find_topic',\
                                                args=[L_F_T.id]))
    context = {'L_F_E': L_F_E, 'L_F_T': L_F_T, 'form': form}
    return render(request, 'webpages/community/LFT_edit_entry.html', context)

#for sale
    #电子产品
def electronics(request):
    electronics = electronics_topic.objects.order_by('E_T_date')
    context = {'electronics':electronics}
    return render(request, 'webpages/for_sale/electronics.html', context)

def E_T(request, E_T_id):
    E_T = electronics_topic.objects.get(id=E_T_id)
    E_T_entries = E_T.electronics_entry_set.order_by('E_T_date')
    context = {'E_T':E_T, 'E_T_entries':E_T_entries}
    return render(request, 'webpages/for_sale/electronics_topic.html', context)

def ET_new_topic(request):
    if request.method != 'POST':
        form = ET_Form()
    else:
        form = ET_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webpages:electronics'))
    context = {'form':form}
    return render(request, 'webpages/for_sale/ET_new_topic.html', context)

def ET_new_entry(request, E_T_id):
    E_T = electronics_topic.objects.get(id=E_T_id)

    if request.method != 'POST':
        form = ET_EntryForm()
    else:
        form = ET_EntryForm(data=request.POST)
        if form.is_valid():
            ET_new_entry = form.save(commit=False)
            ET_new_entry.E_T = E_T
            ET_new_entry.save()
            return HttpResponseRedirect(reverse('webpages:electronics_topic',\
                                                args=[E_T_id]))
    context = {'E_T': E_T, 'form': form}
    return render(request, 'webpages/for_sale/ET_new_entry.html', context)

def ET_edit_entry(request, E_E_id):
    E_E = electronics_entry.objects.get(id=E_E_id)
    E_T = E_E.E_T
    if request.method != 'POST':
        form = ET_EntryForm(instance=E_E)
    else:
        form = ET_EntryForm(instance=E_E, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webpages:electronics_topic',\
                                                args=[E_T.id]))
    context = {'E_E': E_E, 'E_T': E_T, 'form': form}
    return render(request, 'webpages/for_sale/ET_edit_entry.html', context)

    #日常用品
def necessary(request):
    necessary = necessary_topic.objects.order_by('N_T_date')
    context = {'necessary':necessary}
    return render(request, 'webpages/for_sale/necessary.html', context)

def N_T(request, N_T_id):
    N_T = necessary_topic.objects.get(id=N_T_id)
    N_T_entries = N_T.necessary_entry_set.order_by('N_T_date')
    context = {'N_T':N_T, 'N_T_entries':N_T_entries}
    return render(request, 'webpages/for_sale/necessary_topic.html', context)

def NT_new_topic(request):
    if request.method != 'POST':
        form = NT_Form()
    else:
        form = NT_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webpages:necessary'))
    context = {'form':form}
    return render(request, 'webpages/for_sale/NT_new_topic.html', context)

def NT_new_entry(request, N_T_id):
    N_T = necessary_topic.objects.get(id=N_T_id) 

    if request.method != 'POST':
        form = NT_EntryForm()
    else:
        form = NT_EntryForm(data=request.POST)
        if form.is_valid():
            NT_new_entry = form.save(commit=False)
            NT_new_entry.N_T = N_T
            NT_new_entry.save()
            return HttpResponseRedirect(reverse('webpages:necessary_topic',\
                                                args=[N_T_id]))
    context = {'N_T': N_T, 'form': form}
    return render(request, 'webpages/for_sale/NT_new_entry.html', context)

def NT_edit_entry(request, N_E_id):
    N_E = necessary_entry.objects.get(id=N_E_id)
    N_T = N_E.N_T
    if request.method != 'POST':
        form = NT_EntryForm(instance=N_E)
    else:
        form = NT_EntryForm(instance=N_E, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('webpages:necessary_topic',\
                                                args=[N_T.id]))
    context = {'N_E': N_E, 'N_T': N_T, 'form': form}
    return render(request, 'webpages/for_sale/NT_edit_entry.html', context)








