from django import forms

from ExamProject.common.models import TeamMember


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'


class AddTeamMemberForm(TeamMemberForm):
    pass


class EditTeamMemberForm(TeamMemberForm):
    pass


class DeleteTeamMemberForm(TeamMemberForm):
    pass
