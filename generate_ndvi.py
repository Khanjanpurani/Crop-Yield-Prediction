
import ee

ee.Authenticate()
ee.Initialize(project='calm-velocity-422406-d5')


def generate_ndvi(longitude, latitude, start_date, end_date):
    try:
        # Ensure the coordinates are numbers and within valid ranges
        longitude = float(longitude)
        latitude = float(latitude)
        if not (-180 <= longitude <= 180) or not (-90 <= latitude <= 90):
            raise ValueError("Longitude must be between -180 and 180, and latitude must be between -90 and 90.")

        # Create an Earth Engine geometry point
        point = ee.Geometry.Point([longitude, latitude])

        # Define a smaller region of interest around the point
        region = point.buffer(1000).bounds().getInfo()['coordinates']

        # Filter the image collection for the point and date range, and sort by cloud coverage
        data = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED").filterBounds(point)
        image = data.filterDate(start_date, end_date).sort("CLOUD_COVERAGE_ASSESSMENT").first()

        # Check if image is None (no images in collection)
        if image is None:
            raise ValueError("No images found in the specified date range and location.")

        # Calculate NDVI
        ndvi = image.normalizedDifference(['B8', 'B4'])

        # Generate a URL for the NDVI image with specified dimensions and visualization parameters
        ndvi_url = ndvi.getThumbUrl({
            'region': region,
            'dimensions': 512,
            'format': 'png',
            'min': 0.0,
            'max': 1.0,
            'palette': ['blue', 'yellow', 'green', 'darkgreen', 'black']
        })

        return ndvi_url
    except Exception as e:
        # Log the error and re-raise it
        print(f"An error occurred in generate_ndvi: {e}")
        raise
