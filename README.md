
#PetTinder
 
Welcome to Pet Tinder, a minimalist web app built with Flask that allows you to browse, filter, and maintain a pet’s collection!  PetPal has a minimal interface for adding pets, filtering them by various attributes, and tagging your favorites, whether you're a pet enthusiast searching for new furry friends or a pet adoption company owner. I'm thrilled to present to you this project, which marries usability with functionality in a playful manner to illustrate how Flask can produce dynamic web sites with zero overhead.
 
I started this project as a way to learn how Flask handled routing and templating in the context of actual use cases like filtering lists and uploading files.  It's been kept uncomplicated, using only the core features without getting complicated with external databases (at least, not yet!).  Below is an overview of PetPal functionality, description of the main file, and my thoughts on the design choices I made.
 
Pet Tinder allows users to:
 
• See a list of pets and name, breed, price, location, and photo.
 
• Search for pets using a simple form by type, zone, and max price.
 
• Store "Like" or "Favorite" pets in separate lists (though these are now in-memory).
 
• Add new pets and upload an image to save to the server with a form.
 
• After activities have been done, return to the top pet list.
 
• It is easy to test and modify since the application runs in debug mode locally.
 
• It dynamically renders HTML pages using Jinja2 templating and Flask's development server.
 
• Even though it's a small project, it is a solid foundation for anyone who is willing to further develop it, e.g., by adding a database or user authentication.
 
 
App.py File Analysis
 
The main Python file that defines the Flask app and all its routes is named PetPal.
 
It accomplishes the following:
 
Setup: Initializes a directory for uploading pet photos (static/images), sets up the Flask app, and initializes empty lists (pets, liked_pets, favorite_pets, filtered_pets) to store pet data in memory.
 
Paths:
 
• / (index): Shows the current list of filtered pets on the home page.
 
• User actions to like, favorite, or dislike a pet by ID are routed through /like/<int:pet_id>, /favorite/<int:pet_id>, and /dislike/<int:pet_id>, which returns a redirect to the index.  (Note: "dislike" at the moment only does a redirect; there is an opportunity for further development.)
 
• /Filter (POST): Modifies filtered_pets and filters the pet list according to form data (price, type, and zone).
 
• /Add pet (GET/POST): Displays an add form of a pet (GET) and processes the form data (POST), adding the new pet to the list of pets and saving the photo when uploaded.
 
Execution: It is run with debug mode enabled when run directly.
 
It is concise but straightforward, employing Flask's request handling as well as routes. Breaking it into numerous modules (like routes and models) was the idea, but it would be harder to share and maintain one document with the size of the project.
 
templates/index.html
 
• loops through pets (sent as filtered_pets) with Jinja2 to display each pet's details (name, type, price, zone, and image).
 
• have links or buttons which are linked with the corresponding routes for liking, favoring, or disliking pets.
 
• has a filter form which is directed to the /filter.
 
 Templates/add_pet.html page.
 
"Add Pet" plus name, type, description, price, zone, and picture is by this file.
 
POST request to /add pet to add a pet catalog.
 
images/static/ (Directory)
 
a directory of photos with uploaded pet images.  For convenient access in the templates, the application stores files here with their original names (e.g., <img src=\\\"{{url_for ('static', filename='images/' + pet.image) }}\\\">).
 
 
Design Decisions and Considerations
 
One design decision was to avoid using a database and keep the pet information in RAM (lists such as pets and filtered_pets). I also thought of employing a light-weight ORM such as SQLAlchemy or embedding SQLite, but in-memory storage was faster to implement and did not involve third-party dependency.  The next evolutionary step would be to utilize a database, but it comes at the expense of losing data upon server restart.  That is sufficient for testing.
 
Also, rather than employing a more complex solution such as a cloud storage system, I chose to store photos in a static/images directory. This preserves the app's self-sufficiency and simplicity on the local machine.  I did have trouble with filename collisions, however; if two users upload dog.jpg, one will overwrite the other.  Prefixing filenames with timestamps or UUIDs could be a future fix.
 
For simplicity and ease of understanding, the filtering in /filter utilizes list comprehension, but under the assumption that everything from the form is valid (e.g., price is numeric).  Because Flask debug mode helps detect problems when developing, I considered adding more robust validation but decided against it.
 
Finally, clicking on the "like," "favorite," and "dislike" buttons merely adds pets to lists or redirects without giving any information.  To remain server-side and Flask-centric, I remained with redirects although I thought about generating a confirmation page or updating the user interface dynamically (e.g., with JavaScript).  It could be fun to introduce client-side interactivity!
 
 
