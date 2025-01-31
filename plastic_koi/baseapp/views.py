from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from database import Database

db = Database()
# Create your views here.
def landpage(request) :
    return render(request, "baseapp/landpage.html")

def map(request) :
    data = db.find_all_post()
    return render(request, "baseapp/map.html", {"data" : data})

def upload(request) :
    if request.method == "POST" :
        name = request.POST.get("name")
        des = request.POST.get("des")
        l = request.POST.get("location")
        l = l.split()
        loc = []
        for ele in l :
            loc.append(float(ele))
        upload_url = "nai"
        print(request.FILES)
        if "image" in request.FILES :
            image = request.FILES["image"]
            fs = FileSystemStorage()
            try:
                filename = fs.save(image.name, image)
                upload_url = fs.url(filename)
                db.insert_new_post(name, des, loc, upload_url)
                return redirect("baseapp:map")
            except Exception as e:
                return JsonResponse({"error": f"Internal Server Error: {e}"})            
        return JsonResponse({"Done" : "Uploaded done"}, status=200)
    return render(request, "baseapp/upload.html")