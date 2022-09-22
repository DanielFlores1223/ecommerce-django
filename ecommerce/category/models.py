from django.db import models
from django.urls import reverse

# Create your models here.

class Category( models.Model ):
    category_name = models.CharField( max_length = 20, unique = True )
    description = models.CharField( max_length = 255, blank = True ) #blank -> permitir nulos
    slug = models.CharField( max_length = 100, unique = True )
    cat_image = models.ImageField( upload_to = 'photos/categories', blank = True )

    # Indicando en django como se llama esta tabla en singular y en plural
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    #En lugar de usar app_name:name_url se puede usar este metodo para viajar a la url indicada
    #llamandolo obj.get_url()
    def get_url( self ):
        return reverse( 'store:products_by_category', args=[self.slug] )

    def __str__( self ):
        return self.category_name