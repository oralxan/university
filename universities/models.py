from django.db.models import *
class University(Model):
    name = CharField(
        'name univer',
        max_length=256
    )
    address = TextField(
        'address'
    )
    phone_number = CharField(
        'uni num',
        max_length=13
    )
    image = ImageField(
        'img univer',
        upload_to='university-image/'
    )
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universitys'