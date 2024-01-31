from django.db import models


class City( models.Model ):
    """ координаты городов """
    name = models.CharField( 
        max_length=500, 
        verbose_name=u"Город", 
        default='',
        db_index= True 
    )
    latitude = models.DecimalField( 
        max_digits=9, 
        decimal_places=6, 
        default=0 
    )
    longitude = models.DecimalField( 
        max_digits=9, 
        decimal_places=6, 
        default=0 
    )

    class Meta:
        verbose_name         = u"Город"
        verbose_name_plural     = u"Города"
        ordering                = ( 'name', )

    def __str__( self ):
        return self.name