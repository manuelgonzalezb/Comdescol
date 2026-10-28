from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'tu_secreto'

# Configuración del servidor de correo
app.config['MAIL_SERVER'] = 'gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'manuel.gonzalezb.164@gmail.com'
app.config['MAIL_PASSWORD'] = 'ingemetalero2009'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('.','contact.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['name']
    email = request.form['email']
    mensaje = request.form['mensaje']
    telefono = request.form['phone']
    mantener_informado = request.form['2']

    msg = Message("Nuevo mensaje de " + nombre,
                  sender=email,
                  recipients=["manuel.gonzalezb.164@gmail.com"])
    msg.body = f"Nombre: {nombre}\nEmail: {email}\nMensaje:\n{mensaje}\nTelefono:\n{telefono} \nQuiere mantenerse informado:\n{mantener_informado}"

    try:
        mail.send(msg)
        flash('Correo enviado exitosamente.')
    except Exception as e:
        flash('Error al enviar el correo. Intenta nuevamente.')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
