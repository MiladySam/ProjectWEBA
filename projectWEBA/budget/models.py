
from typing import Iterable
from django.db import models
from django.utils.text import slugify



class Project(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Project, self).save(*args, **kwargs)
        
    def budget_dispo(self):
        depenses = self.depenses.all()
        total = 0
        for depense in depenses:
            total += depense.montant
        # Retourner la différence entre le budget et le total des dépenses
        return self.budget - total
        

    def transac(self):

        list_des_depenses = self.depenses.all()
        return len(list_des_depenses)


        
    



class Categorie(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
   


class Depense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='depenses')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    titre = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-montant']
