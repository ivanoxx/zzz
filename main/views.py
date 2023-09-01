from django.shortcuts import render
from main.models import MyItem

def show_main(request):
    data_shopping_list = MyItem.objects.all()
    context = {
        'keranjang': data_shopping_list,
        'nama': 'Pak Bepe',
        'kelas': 'PBP Z'
    }

    return render(request, "main.html", context)