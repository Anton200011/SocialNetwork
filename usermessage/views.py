from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Message, Dialog, MessageText
from .forms import MessageSendForm
from users.models import CustomUser


# Create your views here.
def message_list(request, part1, part2):
    try:
        owner1 = CustomUser.objects.get(id=part1)
        owner2 = CustomUser.objects.get(id=part2)
        dialog = Dialog.objects.get(
            Q(participant1=owner1, participant2=owner2) | Q(participant1=owner2, participant2=owner1))
        messages = Message.objects.filter(dialog_id=dialog)
    except CustomUser.DoesNotExist:
        return HttpResponse(status=404)
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    except Dialog.DoesNotExist:
        new_dialog = Dialog.create(owner1, owner2)
        new_dialog.save()
        messages = Message.objects.filter(dialog_id=new_dialog)
        return render(request, 'usermessages/messageList.html',
                      {'messages': messages, 'dialog': new_dialog, 'form': MessageSendForm})
    return render(request, 'usermessages/messageList.html',
                  {'messages': messages, 'dialog': dialog, 'form': MessageSendForm})


def dialog_list(request, owner_id):
    try:
        owner = CustomUser.objects.get(id=owner_id)
        dialog = Dialog.objects.filter(Q(participant1=owner) | Q(participant2=owner))
    except CustomUser.DoesNotExist:
        return HttpResponse(status=404)
    except Dialog.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'usermessages/dialogList.html',
                  {'dialogs': dialog})


@require_POST
def send_message(request, sen_id, rec_id):
    message_form = MessageSendForm(request.POST)
    owner1 = CustomUser.objects.get(id=sen_id)
    owner2 = CustomUser.objects.get(id=rec_id)
    dialog = Dialog.objects.get(
        Q(participant1=owner1, participant2=owner2) | Q(participant1=owner2, participant2=owner1))
    if message_form.is_valid():
        cd = message_form.cleaned_data
        new_text = MessageText.create(cd.get('mess_text'))
        new_text.save()
        new_message = Message.create(dialog, owner1, owner2, new_text)
        new_message.save()
        return redirect('message:message_list', part1=sen_id, part2=rec_id)
    else:
        return HttpResponse(status=404)


def remove_message(request, mess_id, part1, part2):
    try:
        message = Message.objects.get(id=mess_id)
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    # if request.method == 'DELETE':
    message.delete()
    # return HttpResponse(status=204)
    return redirect('message:message_list', part1=part1, part2=part2)


def remove_dialog(request, sen_id, rec_id):
    try:
        owner1 = CustomUser.objects.get(id=sen_id)
        owner2 = CustomUser.objects.get(id=rec_id)
        dialog = Dialog.objects.get(
            Q(participant1=owner1, participant2=owner2) | Q(participant1=owner2, participant2=owner1))
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    except Dialog.DoesNotExist:
        return HttpResponse(status=404)
    dialog.delete()
    # return HttpResponseRedirect(redirect('message:dialogs', owner_id=owner1.id))
    return redirect('message:dialogs', owner_id=sen_id)
