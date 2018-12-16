from django.shortcuts import render, HttpResponse


def home1(request):
"""!@brief Creates the render request for home1.html, the main page for Managing User Accounts.
"""
	context = {}
	return render(request, 'home1.html', context)

