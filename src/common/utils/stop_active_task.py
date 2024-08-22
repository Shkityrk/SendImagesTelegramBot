__all__ = [
    "stop_active_task",
]

# Хранение активных задач для каждого пользователя
active_tasks = {}
async def stop_active_task(user_id):
    if user_id in active_tasks:
        task = active_tasks[user_id]
        if not task.done():
            task.cancel()
        del active_tasks[user_id]