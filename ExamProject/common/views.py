from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ExamProject.common.forms import EditTeamMemberForm, DeleteTeamMemberForm, AddTeamMemberForm
from ExamProject.common.models import TeamMember
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model


UserModel = get_user_model()


def homepage(request):
    return render(request, template_name='homepage.html')


def about_us(request):
    return render(request, template_name='about.html')


def contact_us(request):
    return render(request, template_name='contacts.html')


def team_information(request):
    all_members = TeamMember.objects.all()
    context = {
        'all_members': all_members,
    }
    return render(request, template_name='team/team.html', context=context)


@login_required
def team_control(request):
    all_members = TeamMember.objects.all()
    context = {
        'all_members': all_members,
    }
    return render(request, template_name='team/team-control.html', context=context)


@login_required
def add_team_member(request):
    if request.method == 'GET':
        form = AddTeamMemberForm()
    else:
        form = AddTeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team-control')
    context = {
        'form': form,
    }
    return render(request, 'team/team-control-add-member.html', context=context)


@login_required
def edit_team_member(request, pk):
    member = TeamMember.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditTeamMemberForm(instance=member)
    else:
        form = EditTeamMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team-control')
    context = {
        'form': form,
        'member': member,
    }
    return render(request, 'team/team-control-edit-member.html', context=context)


@login_required
def delete_team_member(request, pk):
    member = TeamMember.objects.get(pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('homepage')
    form = DeleteTeamMemberForm(instance=member)
    context = {
        'form': form,
    }
    return render(request, 'team/team-control-delete-member.html', context=context)


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)
