from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404, HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


# Create your views here.
