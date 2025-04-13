# housing-mlops-deployment

## Housing Price Prediction - MLOps Workflow

This repository demonstrates a simple MLOps workflow for predicting housing prices based on features like area and bedrooms. The model is trained using linear regression and deployed using a lightweight Gradio web app.

## Repository Contents

- `Housing.csv`: The dataset used for training the model.
- `train.py`: A script to train the linear regression model and save it as `model.pkl`.
- `app.py`: A Gradio script that loads the trained model and provides a simple web interface for predictions.
- `README.md`: Documentation for the project.

## Usage Instructions

To run this project, you will need Python installed on your local machine. Follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/<your-username>/housing-mlops-basic.git
cd housing-mlops-basic
pip install pandas scikit-learn joblib gradio
python train.py
python app.py
