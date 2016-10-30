from django.contrib import admin
from .models import Make, Model, Car, CarImage, Engine, Gearbox, Condition, Color, Region
# Register your models here.

admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Engine)
admin.site.register(Gearbox)
admin.site.register(Condition)
admin.site.register(Color)
admin.site.register(Region)

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 3
	
class CarAdmin(admin.ModelAdmin):
    model = Car
    fieldsets = (
        ('Base info', {
            'fields': (('make', 'model', 'year', 'probeg', 'hp'), ('engine', 'gearbox', 'region'), ('condition', 'price', 'color'))
        }),
        ('Safety', {
            'fields': (('gps', 'trc', 'afl', 'abs', 'airbagf', 'airbagr', 'airbags', 'ebd', 'esp', 'tpc', 'parkingsensor', 'dsa', 'asr', 'dbs', 'distronic', 'bas'),)
        }),
        ('Extras', {
            'fields': (('ass', 'bthf', 'dvdtv', 'steptip', 'usbaux', 'airmatic', 'keyless', 'diffblock', 'boardpc', 'lightsensor', 'elmirrors', 'elwindows', 'elsuspension', 'elseats', 'elps', 'acc', 'mfv', 'navi', 'swheat', 'pechka', 'fwheating', 'seatsheating', 'swreg', 'rainsensor', 'servo', 'hlwash', 'ccontrol', 'audiosys', 'dpf', 'accjabka', 'integrale'),)
        }),
        ('Other', {
            'fields': (('sedemseats', 'barter', 'lpg', 'crashed', 'lizing', 'metan', 'forparts', 'obslujen', 'novvnos', 'registriran', 'serviznaknijka', 'tuning'),)
        }),
        ('More', {
            'fields': (('dvevrati', 'chetirivrati', 'ledfarove', 'ksenon', 'aludjanti', 'metalic', 'wipersheating', 'shibidah', 'spoileri', 'teglich', 'halogeni', 'alarma', 'broniran', 'imobilaizer', 'kasko', 'centralno', 'grajdanska', 'kojensalon', 'velurensalon', 'alkantara', 'desenvolan', 'taxi', 'zainvalid', 'katafalka', 'lineika', 'ucheben', 'hladilen'),)
        }),
    )
	
    inlines = [ CarImageInline, ]
	
admin.site.register(Car, CarAdmin)
