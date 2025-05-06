
from django.contrib import admin
from django.urls import path

from apps.dialogue.views import npc_dialogues, create_dialogue,delete_dialogue

urlpatterns = [
    path('npc_dialogues/', npc_dialogues, name='npc_dialogues'),

    # 创建用户对话记录
    path('create_dialogue', create_dialogue, name='create_dialogue'),

    # 删除用户对话记录
    path('dialogues/delete/<str:dialogue_id>/',delete_dialogue, name='delete_dialogue'),
]
