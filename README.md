# Emergency Vehicle Detector

This project is a web application for detecting emergency vehicles using an image classification model trained with EfficientNetB0. The application allows users to upload images and get predictions on whether the image contains an emergency vehicle.

## Features

- Upload an image file.
- The application preprocesses the image and predicts if it contains an emergency vehicle.
- Displays the uploaded image along with the prediction result.

## Setup

### Prerequisites

- Python 3.8 or higher

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/emergency-vehicle-detector.git
    cd emergency-vehicle-detector
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Download or place your trained model file (`efficientnet_b0_model.h5`) in the project directory.**

### Running the Application

1. **Start the Flask app:**

    ```sh
    python app.py
    ```

2. **Open your browser and go to:**

    ```
    http://127.0.0.1:5000/
    ```

3. **Upload an image to see the prediction.**

## File Structure

- `app.py`: Main Flask application file.
- `static/`: Static files such as CSS and uploaded images.
- `templates/`: HTML templates.
- `requirements.txt`: List of dependencies.
- `README.md`: Project overview and setup instructions.

## Screenshots

![Screenshot](path/to/your/screenshot.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The [TensorFlow](https://www.tensorflow.org/) library for providing the tools to build and train the model.
- The [Flask](https://flask.palletsprojects.com/) framework for making web development easy and fun.
