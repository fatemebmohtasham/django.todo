from django.shortcuts import render,redirect
from.models import list
from.form import listform
# Create your views here.
def listtodo(request):
  lists=list.objects.all()
  if request.method == 'POST':
    tasks=list.objects.create(
      body=request.POST.get('body')
    )
    lists=list.objects.all()
    return redirect('list-todo')
  context={'lists':lists}
  return render(request,'base/list.html',context)

def deletetask(request,pk):
  task=list.objects.get(id=pk)
  if request.method == 'POST':
    task.delete()
    return redirect('list-todo')
  return render(request,'base/delete.html',{'obj':task})

def edittask(request,pk):
  task=list.objects.get(id=pk)
  form=listform(instance=task)
  if request.method == 'POST':
    form=listform(request.POST,instance=task)
    if form.is_valid():
      form.save()
      return redirect('list-todo')
  context={'form':form}  
  return render(request,'base/edit.html',context)