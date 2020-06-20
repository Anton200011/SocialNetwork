from django.db import models
from users.models import CustomUser


# Create your models here.
class FriendList(models.Model):
    # владелец этого списка друзей
    owner = models.OneToOneField(CustomUser, related_name='friend_list', on_delete=models.CASCADE)

    def __str__(self):
        return 'FriendList {}'.format(self.id)

    @classmethod
    def create(cls, owner):
        friend_list = cls(owner=owner)
        return friend_list


class Friend(models.Model):
    # Привязка к конкретному френдлисту
    f_list_id = models.ForeignKey(FriendList, related_name='friends', on_delete=models.CASCADE)
    # id друга
    friend_id = models.ForeignKey(CustomUser, related_name='friend', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('f_list_id', 'friend_id'),)

    def __str__(self):
        return '{}'.format(self.id)

    @classmethod
    def create(cls, f_list_id, friend_id):
        order_item = cls(f_list_id=f_list_id, friend_id=friend_id)
        return order_item
