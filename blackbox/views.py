from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum

from blackbox.models import Fine, UserFineHistoric
from django.contrib.auth.models import User


def index(request):
    return render(request, 'base/index.html')

def fines(request):
    fines = Fine.objects.all()
    test = Fine.objects.filter(users__pk=1)
    print(test)
    context = {
        'fines': fines,
    }
    return render(request, 'fines/list.html', context)

def users(request):
    users = User.objects.all()
    users_list = []
    for user in users:
        try:
            user_fine_historic = user.userfinehistoric.total_payment
        except User.userfinehistoric.RelatedObjectDoesNotExist:
            user_fine_historic = 0
        # user_fine_historic = user.userfinehistoric.total_payment if user.userfinehistoric.total_payment else 0
        users_list.append({
            'id': user.id,
            'name': user.username,
            'fined': user.fine_set.aggregate(Sum('cost'))['cost__sum'],
            'total': user_fine_historic
        })
    context = {
        'users': users_list,
    }
    return render(request, 'users/list.html', context)

def payment(request, user_id):
    user = User.objects.get(pk=user_id)
    user_fine = user.fine_set.aggregate(Sum('cost'))['cost__sum']
    try:
        if user_fine:
            user_fine_historic = UserFineHistoric.objects.get(users_id=user_id)
            user_fine_historic.total_payment = user_fine_historic.total_payment + user_fine
            user_fine_historic.save()
    except UserFineHistoric.DoesNotExist:
        user_fine_historic = UserFineHistoric(total_payment=user_fine, users=user)
        user_fine_historic.save()
    user.fine_set.clear()
    return HttpResponseRedirect(reverse('users'))
