from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task


@require_http_methods(["GET"])
def task_list(request):
    """Return all tasks as JSON."""
    tasks = Task.objects.all()
    data = [
        {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'created_at': task.created_at.isoformat(),
            'updated_at': task.updated_at.isoformat(),
        }
        for task in tasks
    ]
    return JsonResponse({'tasks': data})


@csrf_exempt
@require_http_methods(["POST"])
def task_create(request):
    """Create a new task."""
    try:
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get('title', ''),
            description=data.get('description', ''),
        )
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'created_at': task.created_at.isoformat(),
        }, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@require_http_methods(["GET"])
def task_detail(request, task_id):
    """Get a specific task by ID."""
    task = get_object_or_404(Task, id=task_id)
    return JsonResponse({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at.isoformat(),
        'updated_at': task.updated_at.isoformat(),
    })


@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def task_update(request, task_id):
    """Update a task."""
    task = get_object_or_404(Task, id=task_id)
    try:
        data = json.loads(request.body)
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'completed' in data:
            task.completed = data['completed']
        task.save()
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'updated_at': task.updated_at.isoformat(),
        })
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def task_delete(request, task_id):
    """Delete a task."""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return JsonResponse({'message': 'Task deleted'}, status=204)


@require_http_methods(["GET"])
def hello(request):
    """Simple hello endpoint."""
    return JsonResponse({'message': 'Todo API is running!'})
