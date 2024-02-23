
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import DepenseForm
from .models import Depense, Project, Categorie
from django.views.generic import CreateView
from django.utils.text import slugify

def project_list(request):

    list = Project.objects.all()
    return render(request, 'budget/project_list.html', {'list': list})





def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    

    if request.method== 'GET' :
        categorie_list = Categorie.objects.filter(project=project)
        return render(request, 'budget/project_detail.html', {'project': project, 'depense_list': project.depenses.all(), 'categorie_list': categorie_list})

    elif request.method == 'POST':
        
        form = DepenseForm(request.POST)
        if form.is_valid():
          titre = form.cleaned_data['titre']
          montant = form.cleaned_data['montant']
          categorie_nom = form.cleaned_data['categorie']
          
          categorie = get_object_or_404(Categorie, project=project, nom=categorie_nom)
          
          Depense.objects.create(project=project, titre=titre, montant=montant, categorie=categorie).save()





    elif request.method == 'DELETE':
        id = json.loads(request.body)['id']
        depense = Depense.objects.get(id=id)
        depense.delete()

        return HttpResponse('')


    return HttpResponseRedirect(project_slug)









class CreateViewProjet(CreateView):
    model = Project
    fields = ['nom', 'budget']
    template_name = 'budget/ajouter_projet.html'

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categorieString'].split(',')
        for categorie in categories:
            Categorie.objects.create(project=Project.objects.get(id=self.object.id),
            nom=categorie
            ).save()
        return HttpResponseRedirect(self.get_lien())
    def get_lien(self):
        return slugify(self.request.POST['nom'])
