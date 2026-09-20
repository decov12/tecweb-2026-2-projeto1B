from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Tag


def _resolve_tags(tags_text):
    """Recebe o texto digitado no campo de tags (separadas por vírgula) e
    devolve uma lista de objetos Tag, reaproveitando tags já existentes com
    o mesmo nome e criando as que ainda não existem. Nomes vazios/repetidos
    são ignorados. Devolve lista vazia se o campo vier em branco, já que uma
    nota pode não ter nenhuma tag."""
    tags_text = tags_text or ''
    nomes = [n.strip() for n in tags_text.split(',')]
    nomes_unicos = []
    for nome in nomes:
        if nome and nome not in nomes_unicos:
            nomes_unicos.append(nome)

    tags = []
    for nome in nomes_unicos:
        tag, _ = Tag.objects.get_or_create(name=nome)
        tags.append(tag)
    return tags


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note.objects.create(title=title, content=content)
        note.tags.set(_resolve_tags(request.POST.get('tags')))
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
        note.save()
        note.tags.set(_resolve_tags(request.POST.get('tags')))
        return redirect('index')
    else:
        tags_atuais = ', '.join(tag.name for tag in note.tags.all())
        return render(request, 'notes/edit.html', {'note': note, 'tags_atuais': tags_atuais})


def tags(request):
    all_tags = Tag.objects.all().order_by('name')
    return render(request, 'notes/tags.html', {'tags': all_tags})


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': tag.notes.all()})
