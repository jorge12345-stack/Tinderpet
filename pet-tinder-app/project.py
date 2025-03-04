from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Ruta para almacenar imágenes
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Lista vacía de mascotas
pets = []

liked_pets = []
favorite_pets = []
filtered_pets = pets

@app.route('/')
def index():
    return render_template("index.html", pets=filtered_pets)

@app.route('/like/<int:pet_id>')
def like_pet(pet_id):
    liked_pets.append(filtered_pets[pet_id])
    return redirect(url_for('index'))

@app.route('/favorite/<int:pet_id>')
def favorite_pet(pet_id):
    favorite_pets.append(filtered_pets[pet_id])
    return redirect(url_for('index'))

@app.route('/dislike/<int:pet_id>')
def dislike_pet(pet_id):
    return redirect(url_for('index'))

@app.route('/filter', methods=['POST'])
def filter_pets():
    global filtered_pets
    selected_zone = request.form.get('zone')
    selected_type = request.form.get('type')
    selected_price = request.form.get('price')
    
    filtered_pets = [p for p in pets if (selected_zone == "All" or p["zone"] == selected_zone) and
                                         (selected_type == "All" or p["type"] == selected_type) and
                                         (selected_price == "All" or p["price"] <= int(selected_price))]
    
    return redirect(url_for('index'))

# Ruta para agregar nuevas mascotas
@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        pet_type = request.form['type']
        description = request.form['description']
        price = request.form['price']
        zone = request.form['zone']
        image = request.files['image']
        
        # Guardar la imagen
        if image:
            image_filename = image.filename
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
        
        new_pet = {
            'name': name,
            'type': pet_type,
            'description': description,
            'price': int(price),
            'zone': zone,
            'image': image_filename
        }
        pets.append(new_pet)
        return redirect(url_for('index'))
    
    return render_template("add_pet.html")

if __name__ == '__main__':
    app.run(debug=True)
