from django.db import models

# Create your models here.
class Phone(models.Model):
    # model_number as the primary key
    model_number = models.CharField(max_length=200, primary_key=True)
    
    # ram in kilo-bytes
    ram = models.CharField(max_length=100,blank=True)
    processor = models.CharField(max_length=200, blank=True)
    manufacturer = models.CharField(max_length=200, blank=True)
    system = models.CharField("Operating System", max_length=200, blank=True)
    screen_size = models.CharField(max_length=200, blank=True)
    screen_resolution = models.CharField(max_length=200, blank=True)
    battery_capacity = models.CharField(max_length=200, blank=True)
    talk_time = models.CharField(max_length=200, blank=True)
    camera_megapixels = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=200, blank=True)
    storage_options = models.CharField(max_length=200, blank=True)
    dimensions = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)

    # the toStr method
    def __str__(self):
        return self.model_number
    
    
    def __unicode__(self):
        return str(self.model_number)
    
    # save an instanve of onject to database
    def savedb(self):
        self.save()
        
    def toDict(self):
        dictionary = {
                'model_number':self.model_number,
                'ram': self.ram,
                'processor':self.processor,
                'manufacturer':self.manufacturer,
                'system':self.system,
                'screen_size':self.screen_size,
                'screen_resolution':self.screen_resolution,
                'battery_capacity':self.battery_capacity,
                'talk_time':self.talk_time,
                'camera_megapixels':self.camera_megapixels,
                'price':self.price,
                'weight':self.weight,
                'storage_options':self.storage_options,
                'dimensions':self.dimensions,
                'image':self.image,
            }
        return dictionary

# this is the base class for reviews.
class Review(models.Model):
    # the phone that is reviewed, foreign key
    phone = models.ForeignKey(Phone)
    
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=300)
    
    # the toStr method
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return str(self.title)
        
    # save an instanve of onject to database
    def savedb(self):
        self.save()
