from django.db import models
from django.db.models import Count
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
    
class GymClassQuerySet(models.QuerySet):
    def trending(self):
        return self.annotate(count=Count("members")).filter(count=15)

class GymClassManager(models.Manager):
    def get_queryset(self):
        return GymClassQuerySet(self.model, using=self._db)

    def trending(self):
        return self.get_queryset().trending()


class GymClass(CreatedUpdatedTimeStamp):
    title = models.CharField(max_length=50, null=True, blank=False)
    base_price = models.FloatField(null=True, blank=False)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_DEFAULT, default="No trainer added yet for this gym class", related_name="gymclass_trainer")
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.title
    
    objects = GymClassManager()
    
class Equipment(CreatedUpdatedTimeStamp):
    name = models.CharField(max_length=255, null=True, blank=False)
    is_damaged = models.BooleanField(default=False, null=True, blank=False)
    branch = models.ManyToManyField(Branch, related_name="equipment_branch")


class DamagedEquipmentQuerySet(models.QuerySet):
    def is_damaged(self):
        return self.filter(is_damaged=True)


class DamagedEquipmentManager(models.Manager):
    def get_queryset(self):
        return DamagedEquipmentQuerySet(self.model, using=self._db).is_damaged()

    def is_damaged(self):
        return self.get_queryset()


class DamagedEquipment(Equipment):
    
    objects = DamagedEquipmentManager()
    class Meta:
        proxy = True
        verbose_name = "a damaged equipment"
        verbose_name_plural = "Damaged Equipments"