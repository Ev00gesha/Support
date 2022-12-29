from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Resuests, Answer


class SupportListView(ListView):
    model = Resuests
    template_name = 'home.html'


class MyAccountView(CreateView):
    model = Resuests
    template_name = 'my_account.html'
    fields = ['type_request', 'body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(MyAccountView, self).get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context


class AnswerView(CreateView):
    model = Answer
    fields = ['answer']
    template_name = 'answered.html'

    def form_valid(self, form):
        model = Resuests
        infos = str(self.request).split('/') 
        tmp = Resuests()
        for object in model.objects.all():
            if(object.id == int(infos[2])):
                tmp = object
        form.instance.request_id = tmp
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        model = Resuests
        context = super(AnswerView, self).get_context_data(**kwargs)
        context["objects"] = model.objects.all()
        infos = str(self.request).split('/')
        context["index"] = int(infos[2])
        return context


class RequestsView(ListView):
    model = Resuests
    template_name = 'my_account.html'


class AnswerListView(ListView):
    model = Answer
    template_name = 'print_answered.html'


class ReqUpdateView(UpdateView):
    model = Resuests
    fields = ['type_request', 'body']
    template_name = 'req_edit.html'


class ReqDeleteView(DeleteView):
    model = Resuests
    template_name = 'req_del.html'
    success_url = reverse_lazy('my_account')
