from django import forms

class ContactForm(forms.Form):
	"""For for creating a new message to an administrator.
		from_email: user types an email that will receive an answer from administrator
		subject: subject for the message
		message: actual body of the message """
	SUBJECT_CATEGORIES = (('[registration_problem]','I have a problem with creation of a new accout'),
		('[login_problem]','I have problem when logging to an existing account'),
		('[event_create_problem]','I have a problem when creating a new event'),
		('[event_join_problem]','I have a problem with joining an event'),
		('[other_problem]','I have other problem...'),)
	from_email = forms.EmailField(required=True)
	category = forms.CharField(widget=forms.Select(choices= SUBJECT_CATEGORIES))
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)