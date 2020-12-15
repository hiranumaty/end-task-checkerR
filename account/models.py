import uuid

from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,user_id,email,password,**extra_fields):
        #createUserの正しい記法の調査(user = self.modelの意味)
        email_normalized = self.normalize_email(email)
        user = self.model(username=user_id,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,user_id,password,**extra_fields):
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(user_id,email,password,**extra_fields)
    def create_superuser(self,userid,password,**extra_fields):
        extra_fields.setdefault('is_proper', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(user_id,email,password,**extra_fields)
class User(AbstractBaseUser,PermissionsMixin):

    user_id = models.UUIDField(verbose_name='ユーザーID',primary_key=True, default=uuid.uuid4, editable=False)
    is_admin = models.BooleanField(verbose_name='管理者権限',default=False)
    email = models.EmailField(verbose_name='メールアドレス',blank=False,)
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_id','is_admin']
    
    objects = UserManager()

    def __str__(self):
        return self.user_id
    
    class Meta:
        verbose_name = 'ログインユーザー'
        verbose_name_plural = 'ログインユーザー'