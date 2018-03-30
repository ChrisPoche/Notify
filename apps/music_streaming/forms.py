from django import forms

class UploadForm(forms.Form):
    trackfile = forms.FileField(label='MP3 to upload')

    artistname = forms.CharField(label='Artist Name', required=False)
    artistdesc = forms.CharField(label='Artist Description', required=False)

    albumname = forms.CharField(label='Album Name', required=False)
    albumyear = forms.IntegerField(label='Release Year', required=False)

    trackname = forms.CharField(label='Track Name', required=False)
    tracknumber = forms.IntegerField(label='Track Number', required=False)
    tracklength = forms.IntegerField(label='Track Length (in seconds)', required=False)

    confirmationbox = forms.BooleanField(label='Check to confirm data and upload file', required=False)