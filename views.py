from django.shortcuts import render
from datetime import datetime
# Create your views here.


def showinfo(request):
    if request.method == 'POST':
        # userA = request.POST.get("userA", None)
        text = request.POST.get('text',None)
        thattime=datetime.now()
        with open('messages.txt','a+') as f:
            f.write('{} : {}\n'.format(thattime.strftime("%Y-%m-%d %H:%M:%S"),text))
    return render(request,"index.html")