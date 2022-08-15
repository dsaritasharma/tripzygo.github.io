from django.db import models

class myuser(models.Model):
    email   = models.EmailField(max_length=250)
    username  = models.CharField(max_length=200)
    password=models.CharField(max_length=50)  
    confirm_password  = models.CharField(max_length=200)
    
    class Meta:
        
        db_table = "database"
      
    def __str__(self):
        return self.email


    
class contact(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField(max_length=500)
    phone=models.CharField(max_length=12)
    next_destination=models.CharField(max_length=500)
    no_of_passanger=models.CharField(max_length=500)
    start_date=models.DateField(("Date"))
    end_date=models.DateField(("Date"))
    share_your_message=models.CharField(max_length=500)
    
    class Meta: 
        
        db_table="database2"
    
    
    def __str__(self):
        return self.name

class package(models.Model):
    destination=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="products")
    def __str__(self):
            return self.destination
