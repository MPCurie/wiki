from email import message
import django
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, content):
    title = util.get_entry(content)

    if not title:
        return  render(request, "encyclopedia/apology.html", {
            "message": "Not_Found"
        })

    return render(request, "encyclopedia/content.html", {
        "content" : title
    })
