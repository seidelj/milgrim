from django.shortcuts import render
from Tree import Node
from models import Constants
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
    for c in treeObj.children:
        children.append(Node(tree, c))
    context = {
        'tree': tree,
        'children': children,
    }

    return render(request, "nodes/node.html", context)


