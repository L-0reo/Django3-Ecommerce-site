from django.db import models



class Item(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title + '-' + str(self.quantity) + ' left'


class Adresa(models.Model):
    selling_what = models.ForeignKey(Item, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    judet = models.CharField(max_length=100)
    localitate = models.CharField(max_length=100)
    strada = models.CharField(max_length=100)
    numar = models.CharField(max_length=100)
    bloc = models.CharField(max_length=100)
    scara = models.CharField(max_length=100)
    ap = models.CharField(max_length=100)
    email = models.EmailField(max_length = 200)
    telefon = models.CharField(max_length=100)
    cantitate = models.IntegerField()
