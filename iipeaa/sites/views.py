from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"index.html")

def Contact(request):
    return render(request,"contact.html")

def Blog(request):
    return render(request,"blog.html")

def Event(request):
    return render(request,"event.html")

def About2(request):
    return render(request,"about2.html")

def Instructor(request):
    return render(request,"instructor.html")

def Index2(request):
    return render(request,"index2.html")

def Index3(request):
    return render(request,"index3.html")

def Instructor2(request):
    return render(request,"instructor2.html")

def Instructor_details(request):
    return render(request,"instructor-details.html")

def Event_single(request):
    return render(request,"event-single.html")

def Erreur(request):
    return render(request,"404.html")

def Courses(request):
    return render(request,"courses.html")

def Courses_sidebar(request):
    return render(request,"courses-sidebar.html")

def Single_course(request):
    return render(request,"single-course.html")

def Blog_full(request):
    return render(request,"blog-full.html")

def Blog_standard(request):
    return render(request,"blog-standard.html")

def Blog_single(request):
    return render(request,"blog-single.html")

def About(request):
    return render(request,"about.html")

def home(request):
    # Récupérer le nombre de visiteurs depuis le middleware
    nb_visitors = request.visitor_count

    # Passer le nombre de visiteurs au template
    context = {'nb_visitors': nb_visitors}
    return render(request, 'home.html', context)