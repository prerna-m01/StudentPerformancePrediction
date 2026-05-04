
from flask import Flask, request, render_template
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask App
application = Flask(__name__)

app = application


# Home Route
@app.route('/')
def index():
    return render_template('index.html')


# Prediction Route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    # If user opens the page directly
    if request.method == 'GET':
        return render_template('home.html')

    # If form is submitted
    try:
        # Collect form data
        data = CustomData(
            gender=request.form.get('gender'),

            race_ethnicity=request.form.get('ethnicity'),

            parental_level_of_education=request.form.get(
                'parental_level_of_education'
            ),

            lunch=request.form.get('lunch'),

            test_preparation_course=request.form.get(
                'test_preparation_course'
            ),

            # Correct mapping
            reading_score=float(
                request.form.get('reading_score')
            ),

            writing_score=float(
                request.form.get('writing_score')
            )
        )

        # Convert input data into DataFrame
        pred_df = data.get_data_as_data_frame()

        print("Input DataFrame")
        print(pred_df)

        print("Before Prediction")

        # Load prediction pipeline
        predict_pipeline = PredictPipeline()

        print("Mid Prediction")

        # Predict result
        results = predict_pipeline.predict(pred_df)

        print("After Prediction")

        # Render result on UI
        return render_template(
            'home.html',
            results=round(results[0], 2)
        )

    except Exception as e:
        print("Error:", e)

        return render_template(
            'home.html',
            results="Something went wrong"
        )


# Run Application
if __name__ == "__main__":
    app.run(host="0.0.0.0")
