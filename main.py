from datetime import datetime
import uuid

class Notifications:
    _cnt = 0
    def __init__(self, message: str, time_to_send: datetime, sent_at: datetime = None):
        Notifications._cnt += 1
        self.id = Notifications._cnt
        self.user_id = str(uuid.uuid4())
        self.message = message
        self.time_to_send = time_to_send
        self.sent_at = sent_at

class Scheduler:
    def __init__(self):
        self.scheduler_lst = []

    def schedule(self, notifications: Notifications):
        dct_data = {
            "id": notifications.id,
            "user_id": notifications.user_id,
            "message": notifications.message,
            "time_to_send": notifications.time_to_send,
            "sent_at": notifications.sent_at
        }
        self.scheduler_lst.append(dct_data)

    def run_pending(self):
        for notification_data in self.scheduler_lst:
            if not notification_data["sent_at"]:
                self.send_notification(notification_data)
                notification_data["sent_at"] = datetime.now()

    def send_notification(self, notification_data):
        print(f"Send notification {notification_data}")


notification = Notifications("Test", datetime(2025, 11, 14, 16, 30), )
notification_2 = Notifications("Test 2", datetime(2025, 11, 14, 16, 35), )
scheduler = Scheduler()
scheduler.schedule(notification)
scheduler.schedule(notification_2)
scheduler.run_pending()

for i in scheduler.scheduler_lst:
    print(i)
