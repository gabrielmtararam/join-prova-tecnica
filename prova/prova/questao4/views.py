import logging
import time
from datetime import datetime

import string
from django.utils.crypto import get_random_string
from django.shortcuts import render
import random
from django.db.models import Count




def questao4(request):

    context = {

    }
    return render(request, "questao4/questao4.html", context=context)
