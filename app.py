from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
client = OpenAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_images', methods=['POST'])
def generate_images():
    prompt = request.form['prompt']
    model = request.form['model']
    size = request.form['size']
    num_images = int(request.form['num_images'])
    quality = request.form['quality'] if 'quality' in request.form else 'standard'

    images = []
    try:
        for i in range(num_images):
            response = client.images.generate(
                model=model,
                prompt=prompt,
                size=size,
                quality=quality,
                n=1,
            )
        for data in response.data:
            image_url = data.url
            images.append(image_url)
    except Exception as e:
        error_message = str(e)
        return render_template('index.html', error=error_message)

    return render_template('index.html', images=images)
