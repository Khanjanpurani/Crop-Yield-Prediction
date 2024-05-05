from flask import Flask, request, jsonify
from flask_cors import CORS
from generate_ndvi import generate_ndvi

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/generate-ndvi', methods=['POST'])
def handle_generate_ndvi():
    try:
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        start_date = request.form['startDate']
        end_date = request.form['endDate']

        ndvi_image_url = generate_ndvi(longitude, latitude, start_date, end_date)
        return jsonify({'ndviImageUrl': ndvi_image_url})
    except Exception as e:
        app.logger.error(f"An error occurred in handle_generate_ndvi: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5001)
