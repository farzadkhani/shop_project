 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.urls import reverse
from Products.models import ShopProduct
from Orders.models import Basket


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name,password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            #image=image,
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(_('email address'), unique=True, db_index=True ,blank=False, null=False)
    mobile = models.IntegerField( 
        _('mobile number is like 09127770077'), 
        #max_length=11, 
        unique=True, 
        db_index=True
        )
    first_name = models.CharField(_('first name'), max_length=150, null=False, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, null=False, blank=False)
    image = models.ImageField(_('image'), upload_to='accounts/user/images', null=True, blank=True)
    
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-id']
        #abstract = True


    ###   All this for creating the user ###
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile', 'first_name', 'last_name']


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def get_full_name_(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    #@property  #return like parameter instead function like 'name = person.full_name' instead of 'name = person.full_name()'
    #def full_name(self):
    #    return '%s %s' % (self.first_name, self.last_name)

    #def get_short_name(self):
    #    """Return the short name for the user."""
    #    return self.first_name

    #def email_user(self, subject, message, from_email=None, **kwargs):
    #    send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def get_address(self):
        address = Address.objects.filter(user=self)
        return address
    
    def __str__(self):
        return self.email   
    
    @property
    def get_shop(self):
        shop = Shop.objects.get(user=self)
        return shop

    @property
    def have_shop(self):
        try:
            shop = Shop.objects.get(user=self)
            if shop.is_active == True:
                return True
            else:
                return False
        except:
            return False

    @property
    def get_basket(self):
        try:
            basket = Basket.objects.get(user=self)
            return basket
        except:
            basket = Basket.objects.create(user=self)
            return  basket

class Profile(models.Model):
    pass


class Address(models.Model):    #for address of users
    name = models.CharField(_('place name'), max_length=500)
    user = models.ForeignKey(
        'User', 
        verbose_name=_('User'), 
        on_delete=models.CASCADE, 
        related_name='Address', 
        related_query_name='Address'
        )
    city = models.CharField(_('city name'), max_length=300)
    street = models.CharField(_('streets name'), max_length=1000)
    number = models.IntegerField(_('house number'))
    zip_code = models.IntegerField(_('zip code number'))
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        ordering = ['-id']
        #unique_together = [['user', 'city', 'street', 'allay', 'zip_code']]

    def __str__(self):
        return str(self.user)
        #return self.user

    #def get_absolute_url(self):
    #    return reverse("Address_detail", kwargs={"pk": self.pk})


class Shop(models.Model):   #the saler hear is registrate
    user = models.ForeignKey(
        'User', 
        verbose_name=_('User'), 
        on_delete=models.CASCADE,
        related_name="Shop", 
        related_query_name='Shop'
        )
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
    #    "User"),related_name="user_shop", on_delete=models.SET_NULL, null=True, blank=True)    
    name = models.CharField(_('name'), max_length=1000, unique=True)
    slug = models.SlugField(_('slug'), unique=True)
    facebook = models.CharField(_('facebook'), max_length=1000,null=True, blank=True)
    instagram = models.CharField(_('instagram'), max_length=1000,null=True, blank=True)
    telegram = models.CharField(_('telegram'), max_length=1000,null=True, blank=True)
    whatsapp = models.CharField(_('whatsapp'), max_length=1000,null=True, blank=True)

    discription = models.TextField(_('discription'), null=True, blank=True)
    image = models.ImageField(_('image'), upload_to='accounts/shop/images', null=True, blank=True)
                                 #height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    is_active = models.BooleanField(
        _('active'),
        default=False,
    )   
    class Meta:
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')
        unique_together = ['user', ]

    def __str__(self):
        return self.name


    # @property
    # def get_shopproducts(self):
    #     shopproducts = ShopProduct.objects.filter(shop=self)
    #     return shopproducts


class Email(models.Model):  #for email of users
    user = models.ForeignKey(
        'User', 
        verbose_name=_('user'), 
        on_delete=models.CASCADE,
        related_name='Email', 
        related_query_name='Email'
        )
                            #related_name='emails', related_query_name='email')
    subject = models.CharField(_('subject'), max_length=500)
    to = models.EmailField(_('to'))
    image = models.ImageField(_('image'), upload_to='accounts/email/images')
    body = models.CharField(_('subject'), max_length=2000)
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)
    draft = models.BooleanField(_('Draft'), default=True)
 
    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

    def __str__(self):
        return self.subject

    def get_email(self):
        return str(self.to)

