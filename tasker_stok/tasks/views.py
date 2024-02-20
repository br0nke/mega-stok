from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from . import models

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'projects_count': models.Project.objects.count(),
        'tasks_count': models.Task.objects.count(),
        'user_count': models.get_user_model().objects.count(),
    }
    return render(request, 'tasks/index.html', context)

def task_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'tasks/task_list.html', {
        'task_list': models.Task.objects.all(),
    })

def task_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'tasks/task_detail.html', {
        'task': get_object_or_404(models.Task, pk=pk),
    })


class ProjectListView(generic.ListView):
    model = models.Project
    template_name = 'tasks/project_list.html'


class ProjectDetailView(generic.DetailView):
    model = models.Project
    template_name = 'tasks/project_detail.html'


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Project
    template_name = 'tasks/project_create.html'
    fields = ('name', )

    def get_success_url(self) -> str:
        messages.success(self.request, _('project created successfully').capitalize())
        return reverse('project_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)