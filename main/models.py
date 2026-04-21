from django.db import models

# Create your models here.


class CreatedUpdatedTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True  

class Member(CreatedUpdatedTimeStamp):
    name = models.CharField(max_length=255, null=True, blank=False)
    balance = models.FloatField(null=True, blank=False)

    def __str__(self):
        return self.name

    @property
    def is_vip(self):
        return self.balance > 1000
    
class Trainer(CreatedUpdatedTimeStamp):
    name = models.CharField(max_length=255, null=True, blank=False)
    specialization = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name
    

class Branch(CreatedUpdatedTimeStamp):
    name = models.CharField(max_length=50, null=True, blank=False)
    location = models.CharField(max_length=50, null=True, blank=False)
    
    def __str__(self):
        return self.name
    
class GymClass(CreatedUpdatedTimeStamp):
    title = models.CharField(max_length=50, null=True, blank=False)
    base_price = models.FloatField(null=True, blank=False)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_DEFAULT, default="No trainer added yet for this gym class", related_name="gymclass_trainer")
    members = models.ManyToManyField(Member, related_name="gymclass_members")

    def __str__(self):
        return self.title
    
    
class Equipment(CreatedUpdatedTimeStamp):
    name = models.CharField(max_length=255, null=True, blank=False)
    is_damaged = models.BooleanField(default=False, null=True, blank=False)
    branch = models.ManyToManyField(Branch, related_name="equipment_branch", null=True, blank=False)
    