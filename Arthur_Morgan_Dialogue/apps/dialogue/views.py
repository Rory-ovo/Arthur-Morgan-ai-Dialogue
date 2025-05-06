import uuid

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Dialogue
import json

User = get_user_model()

# 获取用户对话记录
@login_required
@require_http_methods(["GET"])
def npc_dialogues(request):
    user = request.user
    dialogues = Dialogue.objects.filter(user=user).order_by('-created_at')
    data = [
        {
            "id": dialogue.id,
            "message": dialogue.message,
            "created_at": dialogue.created_at,
            "dify_id": dialogue.dify_id,
            "dify_name": dialogue.dify_name,
            "time": dialogue.time,
            "token": dialogue.token
        }
        for dialogue in dialogues
    ]
    return JsonResponse({"dialogues": data})

# 创建用户对话记录
@login_required
@csrf_exempt
@require_http_methods(["POST"])
def create_dialogue(request):
    try:
        data = json.loads(request.body)
        message = data.get("message")
        if not message:
            return JsonResponse({"error": "Message is required"}, status=400)

        dialogue = Dialogue.objects.create(
            id=str(uuid.uuid4())[:20],  # 生成一个唯一的对话 ID
            message=message,
            user=request.user,
            dify_id=data.get("dify_id"),
            dify_name=data.get("dify_name"),
            token=data.get("token", 0)
        )
        return JsonResponse({"id": dialogue.id, "message": dialogue.message}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

# 删除用户对话记录
@login_required
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_dialogue(request, dialogue_id):
    try:
        dialogue = Dialogue.objects.get(id=dialogue_id, user=request.user)
        dialogue.delete()
        return JsonResponse({"message": "Dialogue deleted successfully"}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Dialogue not found"}, status=404)
