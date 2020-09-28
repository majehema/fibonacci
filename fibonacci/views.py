from django.shortcuts import render

from fibonacci.fibonacci import calc_seq


def home(request, pk):
    title = calc_seq(int(pk))

    context = {
        "form_title": title,
    }

    return render(request, "home.html", context)
