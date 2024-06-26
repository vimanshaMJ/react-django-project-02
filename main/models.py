from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "todolist", null = True)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    

# Item is related to todolist, actually part of todo list    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    
















# python manage.py makemigrations main
# making migrations is similar to like adding something to staging area(save changes and apply changes to project)
#     python manage.py migrate - apply changes to project

# IN CMD:   
#     python manage.py shell

# >>> from main.models import Item, ToDoList
# >>> t = ToDoList(name = "Vimsnsha\'s List")
# >>> t.save()
# >>> ToDoList.objects.all()
# <QuerySet [<ToDoList: Vimsnsha's List>]>
    
# >>> ToDoList.objects.get(id=1)
# <ToDoList: Vimsnsha's List>
# >>> ToDoList.objects.get(name = "Vimsnsha's List")
# <ToDoList: Vimsnsha's List>
    
# MAKE AN ITEM:
#     >>> t.item_set.all()
#     <QuerySet []>
#     >>> t.item_set.create(text="Go to the mall", complete=False)
#     <Item: Go to the mall>
#     >>> t.item_set.all()
#     <QuerySet [<Item: Go to the mall>]>
    


## To delete everything in database: delete every files in migration folder except __init__.py