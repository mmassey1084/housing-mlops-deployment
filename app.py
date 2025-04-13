import gradio as gr
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load("model.pkl")

# Define the prediction function
def predict_price(area, bedrooms):
    input_df = pd.DataFrame([[area, bedrooms]], columns=["area", "bedrooms"])
    prediction = model.predict(input_df)
    return round(prediction[0], 2)

# Create the Gradio interface
interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Area (sq ft)"),
        gr.Number(label="Number of Bedrooms")
    ],
    outputs=gr.Number(label="Predicted Price"),
    title="House Price Predictor",
    description="Enter the area and number of bedrooms to predict the house price."
)

# Launch the app
interface.launch()
