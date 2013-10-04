from django.contrib import admin
from scrumApp.models import *
import sys,inspect

def pred(c):
#    return inspect.isclass(c) and c.__module__ == pred.__module__
    return inspect.isclass(c)

for model in inspect.getmembers(sys.modules["scrumApp.models"], pred):
    print model
    admin.site.register(model[1])

