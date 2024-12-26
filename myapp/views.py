from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
# Create your views here.
def main(request):
    if request.POST:
        model = Person()
        model.first_name = request.POST.get('first_name','')
        model.last_name = request.POST.get('last_name','')
        model.company = request.POST.get('company', '')
        model.email = request.POST.get('email', '')
        model.phone = request.POST.get('area_code', '') + request.POST.get('phone', '')
        model.course_type = request.POST.get('course_type', '')
        model.subject = request.POST.get('subject', '')
        model.exist = request.POST.get('exist', '')
        model.save()
        return redirect('register', pk=model.pk) # Ma'lumotlarni ko'rsatish uchun yangi ko'rinishga yo'naltirish return render(request, 'index.html')('display_data', pk=model.pk) # Ma'lumotlarni ko'rsatish uchun yangi ko'rinishga yo'naltirish
    return render(request, 'index.html')

def register(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'register.html', {'person': person})



# def register(request):
#     if request.POST:
#
#         print(request.POST)
#     return render(request,'register.html')