from flask import Flask, render_template, request
from stories import generate_story_with_gpt4_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    prompt = request.form['prompt']
    # Call OpenAI GPT-4 API to generate story based on the prompt
    # Replace the following line with your actual code for generating the story
    story = generate_story_with_gpt4_api(prompt)
    return render_template('story.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)
