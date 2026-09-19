from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Tag


def _resolve_tag(tag_name):
    """Recebe o texto digitado no campo de tag e devolve o Tag correspondente
    (reaproveitando um já existente com o mesmo nome, ou criando um novo).
    Devolve None se o campo vier vazio, já que uma nota pode não ter tag."""
    tag_name = (tag_name or '').strip()
    if not tag_name:
        return None
    tag, _ = Tag.objects.get_or_create(name=tag_name)
    return tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = _resolve_tag(request.POST.get('tag'))
        Note.objects.create(title=title, content=content, tag=tag)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})


def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('index')


def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.tag = _resolve_tag(request.POST.get('tag'))
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/edit.html', {'note': note})


def tags(request):
    all_tags = Tag.objects.all().order_by('name')
    return render(request, 'notes/tags.html', {'tags': all_tags})


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': tag.notes.all()})
