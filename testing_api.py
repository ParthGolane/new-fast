import requests

BASE_URL = "http://127.0.0.1:8000"

def call_read_root():
    response = requests.get(f"{BASE_URL}/")
    return response.json()

def call_read_item(item_id: int, query: str = None):
    params = {"q": query} if query else {}
    response = requests.get(f"{BASE_URL}/items/{item_id}", params=params)
    return response.json()



# Example usage
print("Calling read_root():", call_read_root())
print("Calling read_item(1):", call_read_item(1))
print("Calling read_item(2, 'sample_query'):", call_read_item(2, "sample_query"))

# Call the POST method to create an item
def call_create_item(item: dict):
    response = requests.post(f"{BASE_URL}/items/", json=item)
    return response.json()

item_data = {
    "name": "Sample Item",
    "price": 19.99,
    "is_offer": True  # This must match the model (boolean)
}
print("Calling create_item():", call_create_item(item_data))
