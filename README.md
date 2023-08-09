# Fireplot Generator

This script processes GeoJSON data related to fire incidents and generates a bar plot showing the number of fire incidents per year. The GeoJSON data is expected to contain information about the location and attributes of fire incidents.

## Getting Started

Follow these steps to use the script:

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/your-username/fire-plot.git

Install the required Python packages using pip:
    pip install -r requirements.txt

Run the script using the following command:

    python fireplot_generator.py -p path/to/your/geojson/file.json

GeoJSON Data

    The script expects GeoJSON data containing information about fire incidents. The data should include attributes such as "Year" and "FireCount". For this example, a sample dataset is provided within the script.
Example Output

    The script generates a bar plot showing the number of fire incidents per year. The x-axis represents the years, and the y-axis represents the number of fire incidents.