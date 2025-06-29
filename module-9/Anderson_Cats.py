import requests

# Step 1: Test the connection to the API
url = "https://catfact.ninja/fact"
response = requests.get(url)

# Step 2: Output the raw response (just the status code)
print(" Testing API connection...")
print(f"Status Code: {response.status_code}\n")

# Step 3: Print the raw (unformatted) JSON response
print(" Raw API Response:")
print(response.text)
print()

# Step 4: Print the formatted JSON response
if response.status_code == 200:
    data = response.json()
    print(" Formatted Output:")
    print(f"Cat Fact: {data['fact']}")
    print(f"Length: {data['length']} characters")
else:
    print("Failed to retrieve data.")
