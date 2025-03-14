from django.views.generic import (
    ListView,
    DetailView
)

from .models import Entry

class EntryListView(ListView):
    model = Entry
    # returns all entries ordered by PK in ASC order
    queryset = Entry.objects.all().order_by("-date_created")  

class EntryDetailView(DetailView):
    model = Entry