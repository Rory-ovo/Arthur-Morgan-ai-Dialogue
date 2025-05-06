from django.conf import settings
from django.db import models


class Dialogue:

    class meta:
        db_table = 'dialogue'
        verbose_name = '聊天记录'

    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(primary_key=True, max_length=20, blank=False, null=False, verbose_name='对话id')
    message = models.TextField(blank=False, null=False, verbose_name='对话内容')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户id')
    dify_id = models.CharField(max_length=255, blank=True, null=True)
    dify_name = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    token = models.IntegerField(blank=True, null=True, default=0)



    def __str__(self):
        return f"{self.user} : {self.message}"