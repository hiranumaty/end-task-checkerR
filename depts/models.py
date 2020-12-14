"""仮のテーブル"""
import uuid
from django.db import models
from django.utils import timezone
# Create your models here.
class Depts(models.Model):
    """部署テーブル(仮)"""
    class Meta:
        db_table = 'deploy'
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    deploy_name = models.CharField(verbose_name='部署名',max_length=30)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.deploy_name