from django import forms
from proyecto_app.models import Descripcion, Productos, Usuarios

# class Product_form(forms.Form):
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     SKU = forms.CharField(max_length=30)
#     active = forms.BooleanField()

class Usuarios_form(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

class Productos_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

class Descripcion_form(forms.ModelForm):
    class Meta:
        model = Descripcion
        fields = '__all__'