from __future__ import unicode_literals

import os
import uuid
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
import datetime

# Create your models here.

def photos_papka(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('photos/carphotos', filename)

class Make(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=255)
    make = models.ForeignKey(Make)

    def __str__(self):
        return self.name

class Gearbox(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Engine(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

YEAR_EMPTY = [('','---------')]
YEAR_CHOICES = []
for r in range(1920, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
YEAR_CHOICES = YEAR_CHOICES + YEAR_EMPTY
		
class Car(models.Model):

    make = models.ForeignKey(Make, verbose_name=_('Make:'))
    model = ChainedForeignKey(
        Model,
        chained_field="make",
        chained_model_field="make",
        show_all=False,
        auto_choose=True,
		verbose_name=_('Model:')
    )
    probeg = models.IntegerField()
    hp = models.PositiveIntegerField()
    year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default='') #datetime.datetime.now().year
    color = models.ForeignKey(Color)
    region = models.ForeignKey(Region)
    engine = models.ForeignKey(Engine)
    gearbox = models.ForeignKey(Gearbox)
    condition = models.ForeignKey(Condition)
    price = models.PositiveIntegerField()
    gps = models.BooleanField(default=False, verbose_name=_('GPS'))
    trc = models.BooleanField(default=False, verbose_name=_('Traction Control'))
    afl = models.BooleanField(default=False, verbose_name=_('Adaptive front lights'))
    abs = models.BooleanField(default=False, verbose_name=_('Anti-lock braking system'))
    airbagf = models.BooleanField(default=False, verbose_name=_('Airbag front'))
    airbagr = models.BooleanField(default=False, verbose_name=_('Airbag rear'))
    airbags = models.BooleanField(default=False, verbose_name=_('Airbag side'))
    ebd = models.BooleanField(default=False, verbose_name=_('Electronic Brakeforce Distribution'))
    esp = models.BooleanField(default=False, verbose_name=_('Electronic Stability Program'))
    tpc = models.BooleanField(default=False, verbose_name=_('Tire Pressure Sensor'))
    parkingsensor = models.BooleanField(default=False, verbose_name=_('Parking Sensor'))
    dsa = models.BooleanField(default=False, verbose_name=_('Dynamic Stability Assistance'))
    asr = models.BooleanField(default=False, verbose_name=_('Anti-Slip Regulation'))
    dbs = models.BooleanField(default=False, verbose_name=_('Dry Brake System'))
    distronic = models.BooleanField(default=False, verbose_name=_('Distronic'))
    bas = models.BooleanField(default=False, verbose_name=_('Brake Assistant'))
    ass = models.BooleanField(default=False, verbose_name=_('Auto Start Stop Function'))
    bthf = models.BooleanField(default=False, verbose_name=_('Bluetooth Hands Free'))
    dvdtv = models.BooleanField(default=False, verbose_name=_('DVD/TV'))
    steptip = models.BooleanField(default=False, verbose_name=_('Steptronic/Tiptronic'))
    usbaux = models.BooleanField(default=False, verbose_name=_('USB/AUX'))
    airmatic = models.BooleanField(default=False, verbose_name=_('Adaptive Air Suspension'))
    keyless = models.BooleanField(default=False, verbose_name=_('Keyless Ignition'))
    diffblock = models.BooleanField(default=False, verbose_name=_('Differential Lock'))
    boardpc = models.BooleanField(default=False, verbose_name=_('Board Computer'))
    lightsensor = models.BooleanField(default=False, verbose_name=_('Light Sensor'))
    elmirrors = models.BooleanField(default=False, verbose_name=_('Electric Mirrors'))
    elwindows = models.BooleanField(default=False, verbose_name=_('Electric Windows'))
    elsuspension = models.BooleanField(default=False, verbose_name=_('Electric Suspension'))
    elseats = models.BooleanField(default=False, verbose_name=_('Electric Seats'))
    elps = models.BooleanField(default=False, verbose_name=_('Electric Power Steering'))
    acc = models.BooleanField(default=False, verbose_name=_('Air Conditioner'))
    mfv = models.BooleanField(default=False, verbose_name=_('Multifunctional Steering Wheel'))
    navi = models.BooleanField(default=False, verbose_name=_('Navigation'))
    swheat = models.BooleanField(default=False, verbose_name=_('Steering Wheel Heating'))
    pechka = models.BooleanField(default=False, verbose_name=_('Heating Unit'))
    fwheating = models.BooleanField(default=False, verbose_name=_('Front Window Heating'))
    seatsheating = models.BooleanField(default=False, verbose_name=_('Seats Heating'))
    swreg = models.BooleanField(default=False, verbose_name=_('Steering Wheel Regulation'))
    rainsensor = models.BooleanField(default=False, verbose_name=_('Rain Sensor'))
    servo = models.BooleanField(default=False, verbose_name=_('Power Steering'))
    hlwash = models.BooleanField(default=False, verbose_name=_('Headlights Washing System'))
    ccontrol = models.BooleanField(default=False, verbose_name=_('Cruise Control'))
    audiosys = models.BooleanField(default=False, verbose_name=_('Audio System'))
    dpf = models.BooleanField(default=False, verbose_name=_('DPF'))
    accjabka = models.BooleanField(default=False, verbose_name=_('Hladilna jabka'))

    integrale = models.BooleanField(default=False, verbose_name=_('4x4'))
    sedemseats = models.BooleanField(default=False, verbose_name=_('7 seats'))
    barter = models.BooleanField(default=False, verbose_name=_('Barter'))
    lpg = models.BooleanField(default=False, verbose_name=_('LPG'))
    crashed = models.BooleanField(default=False, verbose_name=_('Crashed'))
    lizing = models.BooleanField(default=False, verbose_name=_('Leasing'))
    metan = models.BooleanField(default=False, verbose_name=_('Metane'))
    forparts = models.BooleanField(default=False, verbose_name=_('For parts'))
    obslujen = models.BooleanField(default=False, verbose_name=_('Serviced'))
    novvnos = models.BooleanField(default=False, verbose_name=_('Not registered'))
    registriran = models.BooleanField(default=False, verbose_name=_('Registered'))
    serviznaknijka = models.BooleanField(default=False, verbose_name=_('Service book'))
    tuning = models.BooleanField(default=False, verbose_name=_('Tuning'))

    dvevrati = models.BooleanField(default=False, verbose_name=_('Two Door'))
    chetirivrati = models.BooleanField(default=False, verbose_name=_('Four Door'))
    ledfarove = models.BooleanField(default=False, verbose_name=_('Led headlights'))
    ksenon = models.BooleanField(default=False, verbose_name=_('Xenon'))
    aludjanti = models.BooleanField(default=False, verbose_name=_('Alloy Wheels'))
    metalic = models.BooleanField(default=False, verbose_name=_('Metallic'))
    wipersheating = models.BooleanField(default=False, verbose_name=_('Wipers Heating'))
    shibidah = models.BooleanField(default=False, verbose_name=_('shibidah'))
    spoileri = models.BooleanField(default=False, verbose_name=_('Spoilers'))
    teglich = models.BooleanField(default=False, verbose_name=_('Teglich'))
    halogeni = models.BooleanField(default=False, verbose_name=_('Halogen Lights'))

    alarma = models.BooleanField(default=False, verbose_name=_('Alarm System'))
    broniran = models.BooleanField(default=False, verbose_name=_('Bulletproof'))
    imobilaizer = models.BooleanField(default=False, verbose_name=_('Immobilizer'))
    kasko = models.BooleanField(default=False, verbose_name=_('Insurance'))
    centralno = models.BooleanField(default=False, verbose_name=_('Central Locking System'))
    grajdanska = models.BooleanField(default=False, verbose_name=_('Grajdanska'))

    kojensalon = models.BooleanField(default=False, verbose_name=_('Leather Seats'))
    velurensalon = models.BooleanField(default=False, verbose_name=_('Veluren salon'))
    alkantara = models.BooleanField(default=False, verbose_name=_('Alkantara'))
    desenvolan = models.BooleanField(default=False, verbose_name=_('Right Hand Drive'))

    taxi = models.BooleanField(default=False, verbose_name=_('Taxi'))
    zainvalid = models.BooleanField(default=False, verbose_name=_('Za invalid'))
    katafalka = models.BooleanField(default=False, verbose_name=_('Katafalka'))
    lineika = models.BooleanField(default=False, verbose_name=_('Ambulance'))
    ucheben = models.BooleanField(default=False, verbose_name=_('Ucheben'))
    hladilen = models.BooleanField(default=False, verbose_name=_('Hladilen'))
    slug = models.SlugField()

    def __str__(self):
        return '%s %s %s' % (self.pk, self.make, self.model)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Newly created object, so set slug
            self.slug = slugify(unicode('%s %s %s' % (self.pk, self.make, self.model)))

        super(Car, self).save(*args, **kwargs)
		
class CarImage(models.Model):

    car = models.ForeignKey(Car, related_name='images')
    image = models.ImageField(upload_to=photos_papka)
		

