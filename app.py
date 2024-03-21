from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

def search_data(query):
    with open('data.txt', 'r') as file:
        data = file.readlines()
    matching_lines = [line.strip() for line in data if query in line.lower()]
    return matching_lines

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_email', methods=['GET'])
def send_email():
    if request.method == 'GET':
        name = request.args.get('name')
        email = request.args.get('email')
        message = request.args.get('message')

        to_email = "mustaqueestandarjunior@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = "Nova mensagem do formulário de contato"
        msg.attach(MIMEText(f"Nome: {name}\nE-mail: {email}\nMensagem:\n{message}", 'plain'))

        try:
            server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
            server.starttls()
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            server.sendmail(email, to_email, msg.as_string())
            server.quit()

            return render_template('contact.html', message="Sua mensagem foi enviada com sucesso!", success=True)
        except Exception as e:
            return render_template('contact.html', message=f"Desculpe, houve um problema ao enviar sua mensagem: {str(e)}", success=False)
        
# Rota para a pesquisa
@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        query = request.json.get('query')
        matching_lines = search_data(query)    
        # Retornar os resultados da pesquisa
        return redirect(url_for('results', query=query, matching_lines=matching_lines))

# Rota para os resultados da pesquisa
@app.route('/results')
def results():
    query = request.args.get('query')
    matching_lines = search_data(query)
    return render_template('results.html', query=query, matching_lines=matching_lines)


if __name__ == '__main__':
    app.run(debug=True)
