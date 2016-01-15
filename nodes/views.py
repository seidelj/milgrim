from django.shortcuts import render
from Tree import Node
from models import Constants, Path
# Create your views here.

def index(request):

    context = {
        'trees': Constants.trees,
        'event': 0,
    }
    return render(request, "nodes/index.html", context)

def node(request, tree, event):
    event = int(event)
    treeObj = Node(tree, event)
    children = []
    path = Path.objects.get(name=tree)
    for c in treeObj.children:
        children.append(Node(tree, c))
    context = {
        'parent': treeObj,
        'parentMeters': path.get_parent_meters(event),
        'meters': path.get_meters(event),
        'children': children,
    }

    return render(request, "nodes/node.html", context)


