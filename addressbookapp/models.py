from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class State(models.Model):
    statename = models.CharField(max_length=50)
    abbreviation=models.CharField(max_length=2)

    def __str__(self):
        return self.statename  
    
StateChoices = (
('AL' , 'Alabama' ), 
('AK' , 'Alaska' ), 
('AZ' , 'Arizona' ), 
('AR' , 'Arkansas' ), 
('CA' , 'California' ), 
('CZ' , 'Canal Zone' ), 
('CO' , 'Colorado' ), 
('CT' , 'Connecticut' ), 
('DE' , 'Delaware' ), 
('DC' , 'District of Columbia' ), 
('FL' , 'Florida' ), 
('GA' , 'Georgia' ), 
('GU' , 'Guam' ), 
('HI' , 'Hawaii' ), 
('ID' , 'Idaho' ), 
('IL' , 'Illinois' ), 
('IN' , 'Indiana' ), 
('IA' , 'Iowa' ), 
('KS' , 'Kansas' ), 
('KY' , 'Kentucky' ), 
('LA' , 'Louisiana' ), 
('ME' , 'Maine' ), 
('MD' , 'Maryland' ), 
('MA' , 'Massachusetts' ), 
('MI' , 'Michigan' ), 
('MN' , 'Minnesota' ), 
('MS' , 'Mississippi' ), 
('MO' , 'Missouri' ), 
('MT' , 'Montana' ), 
('NE' , 'Nebraska' ), 
('NV' , 'Nevada' ), 
('NH' , 'New Hampshire' ), 
('NJ' , 'New Jersey' ), 
('NM' , 'New Mexico' ), 
('NY' , 'New York' ), 
('NC' , 'North Carolina' ), 
('ND' , 'North Dakota' ), 
('OH' , 'Ohio' ), 
('OK' , 'Oklahoma' ), 
('OR' , 'Oregon' ), 
('PA' , 'Pennsylvania' ), 
('PR' , 'Puerto Rico' ), 
('RI' , 'Rhode Island' ), 
('SC' , 'South Carolina' ), 
('SD' , 'South Dakota' ), 
('TN' , 'Tennessee' ), 
('TX' , 'Texas' ), 
('UT' , 'Utah' ), 
('VT' , 'Vermont' ), 
('VI' , 'Virgin Islands' ), 
('VA' , 'Virginia' ), 
('WA' , 'Washington' ), 
('WV' , 'West Virginia' ), 
('WI' , 'Wisconsin' ), 
('WY' , 'Wyoming' ), 
    )




class AddressBook(models.Model):
    name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2,choices=StateChoices) #  models.ForeignKey(State,on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=10)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    #owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)  #workaround for existing recordds without owners


    def __str__(self):
        return self.name

