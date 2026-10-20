"""Flask web application for recognizing handwritten digits."""

# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_result

# Instantiating flask app
app = Flask(__name__)

# Home route
@app.route("/")
def main():
    """Render the homepage for the image recognition app."""
    return render_template("index.html")

# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """Process an uploaded image and return a prediction."""

    print("DEBUG: Prediction route was reached!")

    # Check if the request has a valid photo before the try
    if 'file' not in request.files:
        return render_template(
            "result.html",
            err="File cannot be processed."
        )

    try:
        img = preprocess_img(request.files['file'].stream)
        pred = predict_result(img)
        return render_template("result.html", predictions=str(pred))

    except (ValueError, TypeError, OSError):
        error = "File cannot be processed."
        return render_template("result.html", err=error)

# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
