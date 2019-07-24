from django import forms

from .models import Blog, Mentee, Mentor


class BlogForm(forms.ModelForm):
    """Form definition for Blog."""

    class Meta:
        """Meta definition for Blogform."""

        model = Blog
        fields = ('judul', 'foto', 'tanggal', 'comment', 'deskripsi')


class MenteeForm(forms.ModelForm):
    """Form definition for Mentee."""

    class Meta:
        """Meta definition for Menteeform."""

        model = Mentee
        fields = ('profil', 'nama', 'quotes')


class MentorForm(forms.ModelForm):
    """Form definition for Mentor."""

    class Meta:
        """Meta definition for Mentorform."""

        model = Mentor
        fields = ('profil', 'nama', 'quotes', 'experience')


