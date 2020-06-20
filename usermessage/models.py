from django.db import models
from users.models import CustomUser


# Create your models here.
class Dialog(models.Model):
    # дата написания сообщения
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # Участник1 диалога
    participant1 = models.ForeignKey(CustomUser, related_name='participant1', on_delete=models.CASCADE)
    participant2 = models.ForeignKey(CustomUser, related_name='participant2', on_delete=models.CASCADE)
    # дата обновления сообщения (дата обновления текста сообщения)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Dialog {}'.format(self.id)

    @classmethod
    def create(cls, participant1, participant2):
        order_item = cls(participant1=participant1, participant2=participant2)
        return order_item


class MessageText(models.Model):
    # текст сообщения
    message_text = models.TextField(max_length=255, blank=True, default="")
    # дата написания сообщения
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # дата обновления сообщения (дата обновления текста сообщения)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message_text

    @classmethod
    def create(cls, mess_text):
        text = cls(message_text=mess_text)
        return text


class Message(models.Model):
    # Привязка к конкретному диалогу
    dialog_id = models.ForeignKey(Dialog, related_name='messages', on_delete=models.CASCADE)
    # пользователь, который отправил сообщение
    sender = models.ForeignKey(CustomUser, related_name='message_sender', on_delete=models.CASCADE)
    # пользователь, который получил сообщение
    recipient = models.ForeignKey(CustomUser, related_name='message_recipient', on_delete=models.CASCADE)
    # Текст сообщения
    text = models.ForeignKey(MessageText, related_name="m_text", on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '{}'.format(self.id)

    @classmethod
    def create(cls, dialog_id, sender, recipient, text):
        order_item = cls(dialog_id=dialog_id, sender=sender, recipient=recipient, text=text)
        return order_item
