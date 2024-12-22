from django.shortcuts import render
from celery_django.celery import add
from app.tasks import sub
from celery.result import AsyncResult
# Create your views here.


### Enquue Task Using delay function
# def index(request):
#     print("Results")
#     result1=add.delay(10,20)
#     print("Result 1",result1)

#     result2=sub.delay(80,10)
#     print("Result 2",result2)
#     return render(request,"home.html")


## Enque Task Using apply_async function
# def index(request):
#     print("Results")
#     result1=add.apply_async(args=[10,20])
#     print("Result 1",result1)

#     result2=sub.apply_async(args=[80,10])
#     print("Result 2",result2)
#     return render(request,"home.html")


## Display  Addition Value after Task Execution
def index(request):
    result=add.delay(10,30)
    return render(request,"home.html",{'result':result})



def check_result(request,task_id):
    result=AsyncResult(task_id)
    return render(request,"result.html",{'result':result})





def about(request):
    print("Results")
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")