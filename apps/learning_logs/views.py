from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})


class TopicsView(View):
    def get(self, request):
        topics = Topic.objects.all().order_by('add_time')
        return render(request, 'topics.html', {
            'topics': topics,
        })


class TopicView(View):
    def get(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        entries = Entry.objects.filter(topic=topic).order_by('-add_time')
        return render(request, 'topic.html', {
            'topic': topic,
            'entries': entries,
        })


class AddNewTopicView(View):
    def get(self, request):
        topic_form = TopicForm
        return render(request, 'new_topic.html', {
            'topic_form': topic_form,
        })

    def post(self, request):
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            topic_form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        else:
            return render(request, 'new_topic.html', {
                'topic_form': topic_form,
            })


class AddNewEntryView(View):
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