from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)

messages = []

# Sample project data
projects = [
    {
        "title": "Nexus Logistic Solutions - Course Delivery Optimization",
        "date": "Aug 2024 - Dec 2024",
        "description": "Led a team of 4 to analyze in-person vs. virtual course delivery data, building statistical models to improve learning outcomes. Delivered a 20% boost in course allocation efficiency using Tableau dashboards for regional trend visualization.",
        "tools": "Python, Tableau, Statistical Modeling",
        "file": "nexus_logistics.pdf"
    }
]

# Certificate data
certificates = [
    {
        "title": "Data Analysis with Python Certification",
        "issuer": "FreeCodeCamp",
        "date": "Feb 14 2025",  # Adjust to the actual completion date if known
        "url": "https://www.freecodecamp.org/certification/gsilayo15/data-analysis-with-python-v7"  # External link
    }
    # Add more certificates here (with 'file' for local PDFs or 'url' for external links)
]

@app.route('/')
def home():
    return render_template('index.html', messages=messages, projects=projects, certificates=certificates)

@app.route('/resume')
def view_resume():
    return send_file('static/resume.pdf', as_attachment=False)

@app.route('/project/<filename>')
def download_project(filename):
    return send_file(f'static/projects/{filename}', as_attachment=False)

@app.route('/certificate/<filename>')
def view_certificate(filename):
    return send_file(f'static/certificates/{filename}', as_attachment=False)  # Still available for local files

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    messages.append({'name': name, 'email': email, 'message': message})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)