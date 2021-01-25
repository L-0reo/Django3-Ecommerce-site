from django.shortcuts import render
from .forms import AdresaForm
import smtplib
from email.message import EmailMessage
from .models import Item
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .Google import Create_Service
import base64
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def smania(request):
    return render(request, 'store/smania.html')


def home(request):
    return render(request, 'store/home.html')


def colier(request):
    if request.method == 'GET':
        return render(request, 'store/colier.html')
    else:
        formdata= AdresaForm(request.POST)

        coliere = Item.objects.get(title="colier")
        coliere.quantity -= int(str(formdata['cantitate'].value()))
        coliere.save()

        numesiprenume= formdata['nume'].value()
        judet= formdata['judet'].value()
        localitate= formdata['localitate'].value()
        strada= formdata['strada'].value()
        numar= formdata['numar'].value()
        bloc= formdata['bloc'].value()
        scara= formdata['scara'].value()
        ap= formdata['ap'].value()
        email_m= formdata['email'].value()
        telefon= formdata['telefon'].value()
        cantitate= formdata['cantitate'].value()

        email_content = ('Comanda noua de colier: \n' + ' \n' +  'Nume: ' + numesiprenume + '\n' + 'Judet: ' + judet + '\n' +'Localitatea: '
                            + localitate + '\n'+'Strada: '+ strada +
                                '\n'+ 'Numarul: ' + numar + '\n'+ 'Bloc: ' + bloc + '\n'+ 'Scara: ' + scara + '\n' + 'Apartament: ' +
                                    ap + '\n' + 'E-mail: ' + str(email_m) +
                                        '\n' + 'Telefon: ' + telefon + '\n' + 'Cantitate: ' + str(cantitate))


        os.chdir("C:/Users/Any1/Desktop/ecommerce-project/store")

        CLIENT_SECRET_FILE = 'client_secret.json'
        API_NAME = 'gmail'
        API_VERSION = 'v1'
        SCOPES = ['https://mail.google.com/']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        emailMsg = email_content
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = 'l.mihaly@outlook.com'
        mimeMessage['subject'] = 'Colier'
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

        return HttpResponseRedirect(reverse('success'))


def curea(request):

    if request.method == 'GET':
        return render(request, 'store/curea.html')
    else:
        formdata= AdresaForm(request.POST)

        curele = Item.objects.get(title="curea")
        curele.quantity -= int(str(formdata['cantitate'].value()))
        curele.save()

        numesiprenume= formdata['nume'].value()
        judet= formdata['judet'].value()
        localitate= formdata['localitate'].value()
        strada= formdata['strada'].value()
        numar= formdata['numar'].value()
        bloc= formdata['bloc'].value()
        scara= formdata['scara'].value()
        ap= formdata['ap'].value()
        email_m= formdata['email'].value()
        telefon= formdata['telefon'].value()
        cantitate= formdata['cantitate'].value()

        email_content = ('Comanda noua de curea: \n' + ' \n' +  'Nume: ' + numesiprenume + '\n' + 'Judet: ' + judet + '\n' +'Localitatea: '
                            + localitate + '\n'+'Strada: '+ strada +
                                '\n'+ 'Numarul: ' + numar + '\n'+ 'Bloc: ' + bloc + '\n'+ 'Scara: ' + scara + '\n' + 'Apartament: ' +
                                    ap + '\n' + 'E-mail: ' + str(email_m) +
                                        '\n' + 'Telefon: ' + telefon + '\n' + 'Cantitate: ' + str(cantitate))

        os.chdir("C:/Users/Any1/Desktop/ecommerce-project/store")

        CLIENT_SECRET_FILE = 'client_secret.json'
        API_NAME = 'gmail'
        API_VERSION = 'v1'
        SCOPES = ['https://mail.google.com/']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        emailMsg = email_content
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = 'l.mihaly@outlook.com'
        mimeMessage['Subject'] = 'Curea'
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

        return HttpResponseRedirect(reverse('success'))



def success(request):
    return render(request, 'store/success.html')

def adresa(request):
    return render(request, 'store/adresa.html')

    #send email without API

        # numesiprenume= formdata['nume'].value()
        # judet= formdata['judet'].value()
        # localitate= formdata['localitate'].value()
        # strada= formdata['strada'].value()
        # numar= formdata['numar'].value()
        # bloc= formdata['bloc'].value()
        # scara= formdata['scara'].value()
        # ap= formdata['ap'].value()
        # email_m= formdata['email'].value()
        # telefon= formdata['telefon'].value()
        # cantitate= formdata['cantitate'].value()
        #
        #
        # email = EmailMessage()
        # email['from'] = 'Python <lali099129@gmail.com>'
        # email['to'] = 'l.mihaly@outlook.com'
        # email['subject'] = 'Colier'
        #
        #
        #
        #
        # email.set_content('Comanda noua de colier: \n' + ' \n' +  'Nume: ' + numesiprenume + '\n' + 'Judet: ' + judet + '\n' +'Localitatea: '+
        #                 localitate + '\n'+'Strada: '+ strada +
        #                     '\n'+ 'Numarul: ' + numar + '\n'+ 'Bloc: ' + bloc + '\n'+ 'Scara: ' + scara + '\n' + 'Apartament: ' +
        #                         ap + '\n' + 'E-mail: ' + str(email_m) +
        #                             '\n' + 'Telefon: ' + telefon + '\n' + 'Cantitate: ' + str(cantitate) )
        #
        #
        # with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        #     smtp.ehlo()
        #     smtp.starttls()
        #     smtp.ehlo()
        #
        #     smtp.login('lali099129@gmail.com', 'linchkin09')   #username & password
        #     smtp.send_message(email)
