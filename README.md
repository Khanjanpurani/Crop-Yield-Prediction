# Crop Yield Prediction

Crop Yield Prediction is a project that uses machine learning to predict crop yields from a dataset. It also generates NDVI images to visualize crop health, aiding in agricultural decision-making.

## Project Description

Crop Yield Prediction is a project that leverages machine learning and satellite imagery to predict crop yields. It uses the Sentinel-2 dataset for NDVI (Normalized Difference Vegetation Index) image generation and a Decision Tree algorithm for yield prediction. The NDVI images provide a visual representation of crop health, while the yield prediction aids in agricultural decision-making.

## Table of Contents

1. Installation
2. Usage
3. Machine Learning Model

## Installation

1. **Clone the repository**: Start by cloning the repository to your local machine.

\```bash
git clone https://github.com/Khanjanpurani/Crop-Yield-Prediction.git
\```

2. **Install Jupyter Notebook**: If you haven’t installed Jupyter Notebook on your machine, you can do so using the following command:

\```bash
pip install notebook
\```

3. **Google Earth Engine API**: This project uses the Google Earth Engine API. You need to sign up for a Google Earth Engine account here. Once you have an account, you can authenticate the Earth Engine API using the following command in your terminal:

\```bash
earthengine authenticate
\```

## Usage

1. **Open the project in Jupyter Notebook**: Navigate to the project directory and launch Jupyter Notebook.

\```bash
cd crop-yield-prediction
jupyter notebook
\```

2. **Run the notebooks**: Open the `.ipynb` files and run the cells in order. These notebooks contain the code for data preprocessing, NDVI image generation, and crop yield prediction.

3. **Predict Crop Yields**: The project uses a Decision Tree algorithm for yield prediction. After training the model with the provided dataset, you can use it to predict crop yields.

4. **Generate NDVI Images**: The project uses the Sentinel-2 dataset and the Google Earth Engine API to generate NDVI images. These images provide a visual representation of crop health.

## Machine Learning Model

The crop yield prediction is done using a Decision Tree algorithm. Decision Trees are a type of Supervised Machine Learning where the data is continuously split according to a certain parameter.
