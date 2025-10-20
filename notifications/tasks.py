from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@shared_task
def notify_task_assignment(task_id, assigned_user_id):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "tasks_group",
        {"type": "task_update", "message": f"Вам назначена задача ID: {task_id}"}
    )

@shared_task
def notify_task_deadline(task_id):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "tasks_group",
        {"type": "task_update", "message": f"Задача ID: {task_id} просрочена!"}
    )
    