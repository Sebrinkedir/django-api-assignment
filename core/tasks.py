from celery import shared_task

@shared_task
def send_post_notification(post_id):
    print(f"📬 Sending notification for post ID: {post_id}")
    # Simulate email logic here (we’ll improve later)
    return f"Notification sent for post {post_id}"
