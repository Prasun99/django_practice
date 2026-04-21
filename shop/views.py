from django.http import HttpResponse

def home(request):
  return HttpResponse("Shop home page")
def products(request):
  return HttpResponse ("Shop Prodcuts page")