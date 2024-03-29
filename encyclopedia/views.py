from audioop import reverse
from email import message
import django
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe

from . import util

import random
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def content(request, entry):
    content = util.get_entry(entry)

    if not content:
        return render(request, "encyclopedia/apology.html", {
            "message": "Not_Found",
        })

    return render(request, "encyclopedia/content.html", {
        "content": mark_safe(markdown2.markdown(content)),
        "title": entry,
    })


def search(request):
    entry = request.POST['entry']
    return redirect(reverse('encyclopedia:entry', kwargs={'entry': entry}))

    
def create_page(request):
    titles = util.list_entries()

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        if not title:
            return render(request, "encyclopedia/new_page.html", {
                "error_message": "The title can't be empty",
            }) 

        if title not in titles:
            with open(f"entries/{title}.md", 'w+') as f:
                f.write(content)
            return render(request, "encyclopedia/new_page.html", {
                "success_message": "Successful!",
            }) 
        else:
            return render(request, "encyclopedia/new_page.html", {
                "error_message": "The file already exist",
            }) 

    return render(request, "encyclopedia/new_page.html")


def edit_page(request, entry):
    content = util.get_entry(entry)

    if request.method == 'POST':
        title = request.POST['title']

        with open(f"entries/{title}.md", 'a') as f:
            f.write(content)
        return redirect(reverse('encyclopedia:entry', kwargs={'entry': title}))

    return render(request, "encyclopedia/edit_page.html", {
        "title": entry,
        "content": content,
    })


def random_page(request):
    titles = util.list_entries()
    random_title = random.choice(titles)
    return redirect(reverse('encyclopedia:entry', kwargs={'entry': random_title}))