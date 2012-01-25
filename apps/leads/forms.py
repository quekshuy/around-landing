
from django import forms
from models import ArdLead, ArdMerchantRequest

#--------------------------------------------------------------------------------  

class ArdMerchantRequestForm(forms.ModelForm):
    class Meta:
        model = ArdMerchantRequest

    name = forms.CharField(
            required=False,
            widget=forms.TextInput(attrs={ 'size': '34',
                'placeholder': 'Optional.'}))
    email = forms.EmailField(
            widget=forms.TextInput(attrs={ 'size': '34', 
                'placeholder': 'me@myemail.com'}))
    contact_number = forms.CharField(
            min_length=8,
            required=False,
            widget=forms.TextInput(attrs={ 
                'size': '34',
                'placeholder': "Optional. We promise not to tell."}))
    brand_name = forms.CharField(
            label="Who'd you like to see on around!",
            widget=forms.TextInput(attrs={ 'size': '34', 
                'placeholder': 'e.g. Acme Shoes' }))
    outlet_address = forms.CharField(
            label="Specific Location? (Just the Building or Street name is fine)",
            required=False,
            widget=forms.TextInput(attrs={ 'size': '34', 
                'placeholder': 'Optional.' }))


#--------------------------------------------------------------------------------  

class ArdLeadForm(forms.ModelForm):
    name = forms.CharField(
            widget=forms.TextInput(attrs={ 'size': '34' }))
    email = forms.EmailField(
            widget=forms.TextInput(attrs={ 'size': '34', 
                'placeholder': 'me@myemail.com'}))
    contact_number = forms.CharField(
            min_length=8,
            required=False,
            widget=forms.TextInput(attrs={ 
                'size': '34',
                'placeholder': "Optional. We won't tell anyone. Promise"}))
    brand_name = forms.CharField(
            label='Company Name',
            widget=forms.TextInput(attrs={ 'size': '34', 
                'placeholder': 'e.g. Acme Shoes' }))
    class Meta:
        model = ArdLead
        fields = ('name', 'email', 'contact_number', 'brand_name')

#--------------------------------------------------------------------------------  

class ArdLeadBasicsForm(forms.ModelForm):
    '''
        Form that keeps the basic info.
    '''
    name = forms.CharField(
            widget=forms.TextInput(attrs={ 'size': '40' }))
    email = forms.EmailField(
            widget=forms.TextInput(attrs={ 'size': '34', 
                'placeholder': 'me@myemail.com'}))
    contact_number = forms.CharField(
            widget=forms.TextInput(attrs={ 'size': '10' }))
    class Meta:
        model = ArdLead
        fields = ('name', 'email', 'contact_number')

#--------------------------------------------------------------------------------  

class ArdLeadMerchantForm(forms.ModelForm):
    '''
        Form for merchant info.
    '''
    brand_name = forms.CharField(
            widget=forms.TextInput(attrs={ 'placeholder': 'e.g. Subway' }))
    #mechanics_desc = forms.CharField(label='Promotion/Loyalty Program Mechanics',
            #help_text='E.g. one stamp for every $30 spent OR 15% OFF Bill and '
                      #'one loyalty stamp', widget=forms.Textarea(attrs={
                            #'cols': '30',
                            #'rows': '5',
                            #'placeholder': 'Optional. E.g. one stamp for every '
                                           #'$30 spent, 15% OFF Bill and one '
                                           #'loyalty stamp.'
                          #}),
                      #required=False)
    outlet_address = forms.CharField(
            widget=forms.TextInput(attrs={
                'placeholder': 'Optional. e.g. Junction 8, '
                               'Blk 206 Ang Mo Kio St 12, etc.',
                'size': '40' }), 
            required=False)
    class Meta:
        model = ArdLead
        fields = ('brand_name', 'mechanics_desc', 'outlet_address')

#--------------------------------------------------------------------------------  

class ArdLeadImagesForm(forms.ModelForm):
    '''
        Form for brand images.
    '''
    brand_image = forms.FileField(required=False)
    product_image = forms.FileField(required=False)

    class Meta:
        model = ArdLead
        fields = ('brand_image', 'product_image')

#--------------------------------------------------------------------------------  
