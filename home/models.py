from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=122, null=True)
    email = models.EmailField(max_length=122, null=True)
    phone = models.CharField(max_length=12, null=True)
    desc = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.name


class EventAdvisor(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500, null=True)
    guest = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class EventBase(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500, null=True)
    guest = models.CharField(max_length=500, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CollegeEvent(EventBase):
    pass


class PartiesEvent(EventBase):
    pass


class WeddingEvent(EventBase):
    pass


class TechnicalEvent(EventBase):
    pass
