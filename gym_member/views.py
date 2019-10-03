from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Member


class MemberList(ListView):
    model = Member


class MemberDetail(DetailView):
    model = Member


class MemberCreate(CreateView):
    model = Member
    # Field must be same as the model attribute
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('member_list')


class MemberUpdate(UpdateView):
    model = Member
    # Field must be same as the model attribute
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('member_list')


class MemberDelete(DeleteView):
    model = Member
    success_url = reverse_lazy('member_list')

