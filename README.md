# nutrition-barcode-scanner
Barcode scanner in Python using OpenCV and Open Food Facts API to display nutritional information in real time.

## Features
- Real-time barcode scanning
- Automatic camera closing after detection
- Nutritional information display
- API integration

- 
## Technologies Used
- Python
- OpenCV
- pyzbar
- requests
- Open Food Facts API

- ## How It Works
1. The webcam opens
2. The barcode is scanned
3. The barcode number is extracted
4. the camera shuts down
5. The program sends a request to the API
6. Nutritional values are displayed in the terminal ( calories / proteins / fat / carbs / sugar)

## Installation

Install the required libraries:

```bash
pip install opencv-python pyzbar requests
```

## Run the Program

Run the Python file:

```bash
python main.py
```

## Future Improvements
- GUI interface
- Product images
- Scan history
- Health score system
