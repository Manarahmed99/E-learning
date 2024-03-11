from django.db import models


class Items(models.Model):
 name=models.CharField(max_length=50)
 def __str__(self):
        return self.name

class ItemDetails(models.Model):
    title=models.CharField(max_length=50)
    description = models.TextField()
    instructor=models.CharField(max_length=50)
    image=models.CharField(max_length=150)

    price=models.FloatField()

    tax=models.FloatField()
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title

class Cart(models.Model):
    Id_product=models.IntegerField()
    Id_user=models.IntegerField()
    price=models.FloatField()
    title=models.CharField(max_length=50)
    image=models.CharField(max_length=150)
    itemsid=models.CharField(max_length=50)
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    Created_at=models.DateTimeField(auto_now_add=True)


