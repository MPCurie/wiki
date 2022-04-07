from audioop import reverse
from email import message
import django
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, entry):
    content = util.get_entry(entry)

    if not content:
        return  render(request, "encyclopedia/apology.html", {
            "message": "Not_Found",
        })

    return render(request, "encyclopedia/content.html", {
        "content" : content,
    })

def search(request):
    entry = request.POST['entry']
    return redirect(reverse('encyclopedia:entry', kwargs={'entry': entry}))
    
    