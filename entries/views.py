from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView,
)

from .models import Entry

# Read Views, No Form Handling
class EntryListView(ListView):
    model = Entry
    # returns all entries ordered by PK in ASC order
    queryset = Entry.objects.all().order_by("-date_created")  

class EntryDetailView(DetailView):
    model = Entry


# SMessage Storage
class EntryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Entry created successfully."

class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Entry successfully updated."

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Entry deleted successfully."

    def delete(self, request, *args, **kwargs):
        message.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)