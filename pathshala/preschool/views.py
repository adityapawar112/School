from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'preschool/index.html')

def about(request):
    return render(request, 'preschool/about.html')

def error404(request, exception):
    return render(request, 'preschool/404.html', status=404)

def appointment(request):
    return render(request, 'preschool/appointment.html')

def call_to_action(request):
    return render(request, 'preschool/call-to-action.html')

def classes(request):
    return render(request, 'preschool/classes.html')

def contact(request):
    return render(request, 'preschool/contact.html')

def facility(request):
    return render(request, 'preschool/facility.html')

def team(request):
    return render(request, 'preschool/team.html')

def testimonial(request):
    return render(request, 'preschool/testimonial.html')