from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import FriendList, Friend
from users.models import CustomUser
from collections import OrderedDict
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.
class FriendView(LoginRequiredMixin, UserPassesTestMixin, generic.View):
    login_url = reverse_lazy('login')
    model = CustomUser
    model2 = FriendList
    model3 = Friend

    def test_func(self):
        try:
            f_list = self.model2.objects.get(owner=CustomUser.objects.get(id=self.kwargs['owner_id']))
        except self.model2.DoesNotExist:
            new_f_list = self.model2.create(CustomUser.objects.get(id=self.kwargs['owner_id']))
            new_f_list.save()
            return True
            # return HttpResponse(status=404)
        return f_list.owner.id == self.request.user.id

    def get(self, *args, **kwargs):
        try:
            owner = self.model.objects.get(id=self.request.user.id)
            friends_list = self.model2.objects.get(owner=owner)
            friends = self.model3.objects.filter(f_list_id=friends_list)
        except self.model.DoesNotExist:
            return HttpResponse(status=404)
        except self.model2.DoesNotExist:
            return HttpResponse(status=404)
        except self.model3.DoesNotExist:
            return HttpResponse(status=404)
        return render(self.request, 'friendlist/list.html', {'friends': friends})


@require_POST
def add_friend(request, user_id, owner_id):
    try:
        friend = CustomUser.objects.get(id=user_id)
        owner = CustomUser.objects.get(id=owner_id)
        friends_list = FriendList.objects.get(owner=owner)
    except Friend.DoesNotExist:
        return HttpResponse(status=404)
    except CustomUser.DoesNotExist:
        return HttpResponse(status=404)
    except FriendList.DoesNotExist:
        # return HttpResponse(status=404)
        friends_list = FriendList.create(owner)
        friends_list.save()
    print(friends_list)
    new_friend = Friend.create(friends_list, friend)
    new_friend.save()
    # return HttpResponse(status=200)
    return redirect('friendlist:friend_list', owner_id=owner_id)


def delete_friend(request, user_id, owner_id):
    try:
        friend = CustomUser.objects.get(id=user_id)
        owner = CustomUser.objects.get(id=owner_id)
        friends_list = FriendList.objects.get(owner=owner)
    except Friend.DoesNotExist:
        return HttpResponse(status=404)
    except CustomUser.DoesNotExist:
        return HttpResponse(status=404)
    except FriendList.DoesNotExist:
        return HttpResponse(status=404)
        # if request.method == 'DELETE':
        # cart = Cart(request)
    del_friend = Friend.objects.get(f_list_id=friends_list, friend_id=friend)
    del_friend.delete()
    # return HttpResponse(status=204)
    # return render(request, 'friendlist/list.html', {'friends': Friend.objects.filter(f_list_id=friends_list)})
    return redirect('friendlist:friend_list', owner_id=owner_id)
