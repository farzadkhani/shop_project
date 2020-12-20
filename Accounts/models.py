 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, image,password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            image=image,
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, image, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, image, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, image, password, **extra_fields)

    

class User(AbstractBaseUser, PermissionsMixin):
    #username_validator = UnicodeUsernameValidator()

    #id =models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), blank=True)
    mobile = models.IntegerField( 
        _('mobile number is like 09127770077'), 
        max_length=11, 
        unique=True, 
        db_index=True
        )
    first_name = models.CharField(_('first name'), max_length=150,)
    last_name = models.CharField(_('last name'), max_length=150)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    image = models.ImageField(_('image'), upload_to='accounts/user/images', blank=True)


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
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

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile', 'first_naem', 'last_name']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    #def get_short_name(self):
    #    """Return the short name for the user."""
    #    return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    #return the full_name to show in admin list
    def __str__(self):
        return self.get_full_name()   


class Address():
    #id =models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    city = models.CharField(_('city name'), max_length=300)
    street = models.CharField(_('street name'), max_length=1000)
    plak = models.IntegerField(_('plak number'), max_length=50)
    zip_code = models.IntegerField(_('zip code number'), max_length=10)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        unique_together = [['user', 'city', 'street', 'allay', 'zip_code']]

    def __str__(self):
        return self.user


class Shop():
    #id =models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    slug = models.SlugField(_('slug'))
    name = models.CharField(_('name'), max_length=1000)
    discription = models.CharField(_('discription'))
    image = models.ImageField(_('image'), upload_to='accounts/shop/images')

    class Meta:
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')

    def __str__(self):
        return self.name


class Email():
    #id =models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    subject = models.CharField(_('subject'))
    image = models.ImageField(_('image'), upload_to='accounts/email/images')
    body = models.CharField(_('subject'))

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

    def __str__(self):
        return self.subject

