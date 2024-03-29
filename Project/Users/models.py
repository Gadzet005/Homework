from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.urls import reverse


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, nickname, password, **extra_fields):
        '''
        Создает и сохраняет пользователя с введенными email,
        именем пользователя и паролем.
        '''
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, nickname, password, **extra_fields)

    def create_superuser(self, email, nickname, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, nickname, password, **extra_fields)

    def actived(self):
        return self.get_queryset().filter(is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта', unique=True)

    nickname = models.CharField('Имя пользователя', max_length=50)
    birthday_date = models.DateField('День рождения', null=True, blank=True)

    is_staff = models.BooleanField(
        'Статус персонала', default=False,
        help_text='Определяет доступ пользователя к админ панели',
        )
    is_active = models.BooleanField('Активен', default=True)

    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        return reverse('users:user_details', kwargs={'user_id': self.pk})
