from django.shortcuts import render
from Tree import Node
# Create your views here.

def index(request):
    return "Choose a tree"

def node(request, tree, event)
    tree = Node(tree, event)
    children = []
    for c in tree.children:
        children.append(Node(tree, c))
    context = {
        'tree': tree,
        'children': children,
    }



