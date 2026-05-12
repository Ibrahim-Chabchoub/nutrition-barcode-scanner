import cv2 as cv
from pyzbar.pyzbar import decode
import requests
camera = cv.VideoCapture(0)
code = None
while True:
    success, frame = camera.read()
    cv.imshow("scanner", frame)
    barcodes = decode(frame)
    if barcodes:
        raw_data = barcodes[0].data
        code = raw_data.decode()
        print("Barcode : ", code)
        break
    if cv.waitKey(1) == ord("q"):
        break
camera.release()
cv.destroyAllWindows()
if not code:
    print("no barcode detected")
else:
    url = f"https://world.openfoodfacts.org/api/v2/product/{code}.json"
    headers = {
        "User-Agent": "IbrahimNutritionApp/1.0"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    product = data.get("product")
    if not product:
        print("product not found")
    else:
        nutriments = product.get("nutriments", {})
        print("Calories:", nutriments.get("energy-kcal_100g"), "kcal")
        print("Protein:", nutriments.get("proteins_100g"), "g")
        print("Fat:", nutriments.get("fat_100g"), "g")
        print("Carbs:", nutriments.get("carbohydrates_100g"), "g")
        print(" Sugar:", nutriments.get("sugars_100g"), "g")
