from instagrapi import Client
from PIL import Image


app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

from werkzeug.utils import secure_filename

@app.route('/insta', methods=['POST'])
def insta():
    cl = Client()
    cl.login("username", "your_password")

    if 'photo' not in request.files:
        return "No file part"
    
    file = request.files['photo']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = secure_filename(file.filename)
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(photo_path)
        
        caption = request.form.get('caption', '')

        try:
            with Image.open(photo_path) as img:
                img.verify()  # This will check if the image is corrupted
            cl.photo_upload(photo_path, caption)
            return "Photo posted successfully!"
        except (IOError, SyntaxError) as e:
            return f"An error occurred while processing the image: {e}"
        except Exception as e:
            return f"An error occurred: {e}"
        