from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
db = SQLAlchemy(app)

# Database Model
class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.note}"

# Create database
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/notes')
def notes():
    # Query all notes from the database
    all_notes = FormData.query.all()
    return render_template('notes.html', notes=all_notes)


@app.route('/submit', methods=['POST'])
def submit():
    note = request.form['note']
    new_entry = FormData(note=note)
    db.session.add(new_entry)
    db.session.commit()
    print(f"Added entry with ID: {new_entry.id}")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
