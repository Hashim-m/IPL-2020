from django.db import models



class Squad(models.Model):
     name= models.CharField(max_length=100)
     description=models.TextField(max_length=200)
     img_url =models.CharField(max_length=2083)   


class Orangecap(models.Model):
     name= models.CharField(max_length=100)
     img_url =models.CharField(max_length=2083)

class Purplecap(models.Model):
     name= models.CharField(max_length=100)
     img_url =models.CharField(max_length=2083)

 


     

   
        

     