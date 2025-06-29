import requests

# Make a GET request to the Open Notify API
response = requests.get("http://api.open-notify.org/astros")

# Check for a successful response
if response.status_code == 200:
    print("✅ Successfully retrieved data!\n")
    
    # Convert JSON data to a Python dictionary
    data = response.json()
    
    # Print total number of astronauts
    print(f"There are currently {data['number']} astronauts in space:\n")
    
    # Loop through and print each astronaut's name and spacecraft
    for person in data["people"]:
        print(f"{person['name']} aboard {person['craft']}")
else:
    print(f"❌ Failed to retrieve data. Status code: {response.status_code}")
