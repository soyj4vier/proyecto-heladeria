from django import forms
from django.core.exceptions import ValidationError
import datetime
from aplicacion.models import Cliente, MovimientoPuntos
from aplicacion2.models import Producto, Promocion

class ClienteForm(forms.ModelForm):
    run = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EJ: 123456789'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre'}))
    apellido_paterno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese apellido paterno'}))
    apellido_materno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese apellido materno'}))
    puntos = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ej: +0000'}))

    class Meta:
        model = Cliente
        fields = '__all__'

    def limpiar_run(self):
        run = str(self.cleaned_data['run']).replace('.', '').replace('-', '')
        try:
            run = int(run)
        except ValueError:
            raise ValueError("El RUN debe contener solo números después de limpiarlo.")
        return run

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()

        for palabra in nombre.split():
            if not palabra.isalpha():
                raise ValidationError("El nombre solo puede contener letras y espacios.")

        return nombre.lower()

    def clean_apellido_paterno(self):
        apellido = self.cleaned_data.get('apellido_paterno', '').strip()
        for palabra in apellido.split():
            if not palabra.isalpha():
                raise ValidationError("El apellido solo puede contener letras y espacios.")
        return apellido.lower()

    def clean_apellido_materno(self):
        apellido = self.cleaned_data.get('apellido_materno', '').strip()
        for palabra in apellido.split():
            if not palabra.isalpha():
                raise ValidationError("El apellido solo puede contener letras y espacios.")
        return apellido.lower()

    def clean_puntos(self):
        puntos = self.cleaned_data['puntos']
        if puntos < 0:
            raise forms.ValidationError("Los puntos deben ser cero o positivos.")
        return puntos    

class MovimientoPuntosForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    puntos = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: +10 o -10'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción breve'}))
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="Seleccione un cliente",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = MovimientoPuntos
        fields = '__all__'

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        minima = datetime.date(2000,1,1)
        maxima = datetime.date.today()

        if fecha:
            if fecha < minima or fecha > maxima:
                raise forms.ValidationError("La fecha debe estar entre los 2000 y hoy")
        return fecha
    
    def clean_puntos(self):
        puntos = self.cleaned_data['puntos']
        if puntos == 0:
            raise forms.ValidationError("Los puntos no pueden ser cero.")
        return puntos

class PromocionForm(forms.ModelForm):
    TIPO_DESCUENTO_CHOICES = [
        ('porcentual', 'Porcentual'),
        ('dinero', 'Resta en dinero'),
    ]

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la promoción'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'}))
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    activo = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    tipo_descuento = forms.ChoiceField(choices=TIPO_DESCUENTO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    codigo_promocional = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código promocional'}))
    valor_descuento = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor del descuento'}))

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre.lower()
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        return descripcion.lower()
    
    def clean_fecha_ini(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')

        minima = datetime.date(2000,1,1)
        maxima = datetime.date(2100,1,1)

        if fecha_inicio:
            if fecha_inicio < minima or fecha_inicio > maxima:
                raise forms.ValidationError("La fecha debe estar entre los 2000 y posterior")
        return fecha_inicio
    
    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data.get('fecha_fin')

        minima = datetime.date(2000,1,1)
        maxima = datetime.date(2100,1,1)

        if fecha_fin:
            if fecha_fin < minima or fecha_fin > maxima:
                raise forms.ValidationError("La fecha debe estar entre los 2000 y posterior")
        return fecha_fin

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                raise forms.ValidationError("La fecha de finalización no puede ser anterior a la fecha de inicio.")
        return cleaned_data
    
    class Meta:
        model = Promocion
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'activo', 'tipo_descuento', 'codigo_promocional', 'valor_descuento']

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de producto'}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese precio en pesos'}))

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre.lower()

    class Meta:
        model = Producto
        fields = '__all__'