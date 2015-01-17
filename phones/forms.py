from django import forms

class UpdatePhoneForm(forms.Form):
    model_number = forms.CharField(max_length=200)
    ram = forms.CharField(max_length=100)
    processor = forms.CharField(max_length=200)
    manufacturer = forms.CharField(max_length=200)
    system = forms.CharField(max_length=200)
    screen_size = forms.CharField(max_length=200)
    screen_resolution = forms.CharField(max_length=100, required=False)
    battery_capacity = forms.CharField(max_length=100, required=False)
    talk_time = forms.CharField(max_length=100, required=False)
    camera_megapixels = forms.CharField(max_length=100, required=False)
    price = forms.CharField(max_length=100, required=False)
    weight = forms.CharField(max_length=100, required=False)
    storage_options = forms.CharField(max_length=100, required=False)
    dimensions = forms.CharField(max_length=100, required=False)
