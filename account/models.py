import uuid

from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
# Create your models here.

class UserManager(BaseUserManager):
    """Managerクラス"""
    use_in_migrations = True
    def _create_user(self,user_id,email,password,**extra_fields):
        #createUserの正しい記法の調査(user = self.modelの意味)
        email_normalized = self.normalize_email(email)
        user = self.model(username=user_id,email=email_normalized,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,user_id,email,password,**extra_fields):
        extra_fields.setdefault('is_admin',False)
        extra_fields.setdefault('is_department',True)
        return self._create_user(user_id,email,password,**extra_fields)
    def create_superuser(self,user_id,email,password,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_department',True)
        return self._create_user(user_id,email,password,**extra_fields)
class User(AbstractBaseUser,PermissionsMixin):
    """拡張ユーザーモデル"""
    class Meta:
        db_table = 'users'
        verbose_name = 'ログインユーザー'
        verbose_name_plural = 'ログインユーザー'
    user_id = models.UUIDField(verbose_name='ユーザーID',primary_key=True, default=uuid.uuid4, editable=True,unique=True)
    is_department = models.BooleanField(verbose_name='部門長権限',default=False)
    is_admin = models.BooleanField(verbose_name='管理者権限',default=False)
    email = models.EmailField(verbose_name='メールアドレス',blank=False,)
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['is_admin','is_department']
    
    objects = UserManager()

    def __str__(self):
        """表示の変更"""
        return self.user_id
    
    