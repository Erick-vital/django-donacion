from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse 
import stripe
# Create your views here.

stripe.api_key = "sk_test_51Hgi2qJDGVw77WwFXGaCqPClMZC9vsx7DbJ2su7VKlnttOSJ0k11rjS84q5L0nt5qt8YSmbz9SFLwB4fvkhmMp8G00fqFL8NQw" 

def index(request):
    return render(request, 'index.html') 

def cargo(request):

    #al enviar el form, imprime los datos 
    if request.method == 'POST':
        print('data: ', request.POST)

        monto = int(request.POST['monto']) * 100

        """ al enviar el form creamos el 'customer'
        que tendra dos atributos que tomaremos de los datos
        de nuestro formulario 'request.POST'
        """
        cliente = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['nick-name'],
            source = request.POST['stripeToken']
        )
        
        #crea un cargo a la targeta introducida
        stripe.Charge.create(
            customer = cliente,
            amount = monto,
            currency = 'USD',
            description = 'donacion'
        )

    #redirige a la vista 'exito_vista' con el monto donado
    return redirect(reverse('exito', args=[monto]))

def exito_vista(request, args):
    monto = args

    return render(request, 'exito.html', {'monto':monto})


    
