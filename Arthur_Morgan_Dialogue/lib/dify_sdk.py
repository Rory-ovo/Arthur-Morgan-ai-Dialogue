from django.contrib.sites import requests

from apps import user

dify_workflows = [
    {
        "name": "亚瑟对话",
        "nodes": [
            {
                "id": "851439c5-8532-4a30-adb7-8cec67904deb",
                "type": "start",
                "content": {
                    "type": "text",
                    "text": "开始对话"
                },
                "workflow_url": "http://127.0.0.1/v1/chat-messages",
                "api_key": "app-2robtnipufoJKqdPYPD04jLv",
                "response_mode": "blocking"
            },
        ]
    }
 ]


def dify_running(name, query,conversation_id=None):
    dify_workflow = {}
    for workflow in dify_workflows:
        if workflow['name'] == name:
            dify_workflow = workflow
            break
        else:
            dify_workflow = None
    if dify_workflow is None:
        return {"status": "error", "message": "未找到工作流"}

    headers = {
        "Authorization": f"Bearer {dify_workflows['api_key']}",
        "Content-Type": "application/json"
    }

    data = {
        "conversation_id": conversation_id,
        "workflow_id": dify_workflow['id'],
        "user": "Rory",
        "input_type": "text",
        "input": {"text": query}
    }

    try:
        response = requests.post(dify_workflows["workflow_url"], headers=headers, json=data),
        if response.status_code == 200:
            response_data = response.json()
            return dify_workflows["workflow_url"], response_data
        else:
            print("Error:", response.status_code, response.text)
            return {"error": f"Failed to create dialogue, status code: {response.status_code}"}
    except  Exception as e:
            print("Error:", str(e))


