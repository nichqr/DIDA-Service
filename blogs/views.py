from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def hello(request):
#    return HttpResponse("<h2>Hello World</h2>")

# Create your views here.

#def home(request):
#    return render(request,'home.html')

def hello(request):
    return render(request,'index.html')



def dashboard(request):
    return render(request,'dashboard.html')

#เดินทางไปเครื่องบิน
def createForm(request):
    return render(request,'Form.html')

def addBlog(request):

    idcard=request.POST['idcard']
    name=request.POST['name']
    tel=request.POST['tel']      

    return render(request,'Form2.html',
    {

        'name':name,
        'tel':tel,
        'idcard':idcard

    })

def addBlog2(request):

    name=request.POST['name']
    tel=request.POST['tel']
    province1=request.POST['province1']
    districts1=request.POST['districts1']
    subdistrict1=request.POST['subdistrict1']
    province2=request.POST['province2']
    districts2=request.POST['districts2']
    subdistrict2=request.POST['subdistrict2']      

    return render(request,'result.html',
    {

        'name':name,
        'tel':tel,
        'province1':province1,
        'districts1':districts1,
        'subdistrict1':subdistrict1,
        'province2':province2,
        'districts2':districts2,
        'subdistrict2':subdistrict2

    })

