# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income
from datetime import datetime


# Create your views here.
@csrf_exempt
def submit_expense(request):
    """ submit an expense"""
    # TODO; validate data. user mightbe fake
    this_token = request.POST['token']

    if 'date' not in request.POST:
        now = datetime.now()  # TODO: user might want to submit the data herself

    this_user = User.objects.filter(token__token=this_token).get()
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=now)

    return JsonResponse({
        'status': 'ok',
    }, encoder=json.JSONEncoder)
