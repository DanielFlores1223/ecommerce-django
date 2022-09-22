from django.db import models

#Auth con django
# PARA PODER USARLO CORRECTAMENTE DEBEMOS IR AL ARCHIVO SETTINGS.PY 
#COLOCAL ESTO:
    # Registrando la clase que se va a usar para la autenticación
    #AUTH_USER_MODEL = 'account.Account'
# DESPUES DE LA CONSTANTE: WSGI_APPLICATION 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager( BaseUserManager ):
    def create_user( self ,first_name, last_name, email, username, password = None ):
        if not email:
            raise ValueError('El usuario debe tener un email')

        if not username:
            raise ValueError('El usuario dene tener un username')
        
        user = self.model( 
            email = self.normalize_email( email ),
            username = username, 
            first_name = first_name,
            last_name = last_name
        )

        user.set_password( password )
        user.save( using = self._db )
        return user

    def create_superuser( self, first_name, last_name, email, username, password ):
        user = self.create_user(
            email = self.normalize_email( email ),
            username = username, 
            first_name = first_name,
            last_name = last_name
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True 
        user.is_superadmin = True 

        user.set_password( password )
        user.save( using = self._db )
        return user

# Create your models here.
class Account( AbstractBaseUser ):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50 )
    username = models.CharField( max_length = 50, unique = True )
    email = models.CharField( max_length = 50, unique = True )
    phone_number = models.CharField( max_length = 50 )

    #Campos atributos django
    date_joined = models.DateTimeField( auto_now_add = True )
    last_login = models.DateTimeField( auto_now_add = True )
    is_admin = models.BooleanField( default = False )
    is_staff = models.BooleanField( default = False )
    is_active = models.BooleanField( default = False )
    is_superadmin = models.BooleanField( default = False )

    # Modifcando el valor con el que se va a hacer login, ya que por default esta el username
    USERNAME_FIELD = 'email'

    #campos obligatorios
    REQUIRED_FIELDS = [ 'username', 'first_name', 'last_name' ]

    #instanciando la clase para crear usuarios
    objects = MyAccountManager()

    def __str__( self ):
        return self.email

    #Estos dos metods son obligatorios 
    def has_perm( self, perm, obj = None ): # si tiene permiso a admin
        return self.is_admin

    def has_module_perms( self, add_label ): # si es admin para que tenga permiso a los modulos
        return True 
        
