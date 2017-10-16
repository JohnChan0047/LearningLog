from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from datetime import datetime

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from apps.utils.mixin_utils import LoginRequiredMixin


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            topics = Topic.objects.filter(user=request.user).order_by('add_time')
            return render(request, 'index.html', {
                'topics': topics,
            })
        else:
            return render(request, 'index.html', {})


# class TopicsView(LoginRequiredMixin, View):
#     def get(self, request):
#         topics = Topic.objects.filter(user=request.user).order_by('add_time')
#         return render(request, 'topics.html', {
#             'topics': topics,
#         })


class TopicView(LoginRequiredMixin, View):
    def get(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        if topic.user != request.user:
            raise Http404
        entries = Entry.objects.filter(topic=topic).order_by('-add_time')
        return render(request, 'topic.html', {
            'topic': topic,
            'entries': entries,
        })


class AddNewTopicView(LoginRequiredMixin, View):
    def get(self, request):
        topic_form = TopicForm
        return render(request, 'new_topic.html', {
            'topic_form': topic_form,
        })

    def post(self, request):
        topic_form = TopicForm({'name': request.POST.get('topic', '')})
        if topic_form.is_valid():
            new_topic = topic_form.save(commit=False)
            new_topic.user = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:index'))
        else:
            return render(request, 'new_topic.html', {
                'topic_form': topic_form,
            })


class AddNewEntryView(LoginRequiredMixin, View):
    def get(self, request, topic_id):
        entry_form = EntryForm
        topic = Topic.objects.get(id=topic_id)
        return render(request, 'new_entry.html', {
            'entry_form': entry_form,
            'topic': topic,
        })

    def post(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            new_entry = entry_form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
        else:
            return render(request, 'new_entry.html', {
                'entry_form': entry_form,
                'topic': topic,
            })


class EditEntryView(LoginRequiredMixin, View):
    def get(self, request, entry_id):
        entry = Entry.objects.get(id=entry_id)
        topic = entry.topic
        if topic.user != request.user:
            raise Http404
        entry_form = EntryForm(instance=entry)
        return render(request, 'edit_entry.html', {
            'entry': entry,
            'entry_form': entry_form,
            'topic': topic,
        })

    def post(self, request, entry_id):
        entry = Entry.objects.get(id=entry_id)
        topic = entry.topic
        if topic.user != request.user:
            raise Http404
        entry_form = EntryForm(instance=entry, data=request.POST)
        if entry_form.is_valid():
            entry_form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
        else:
            return render(request, 'edit_entry.html', {
                'entry': entry,
                'entry_form': entry_form,
                'topic': topic,
            })