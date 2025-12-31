# this file is purely to help me code and learn

# HTTTP Methods Examples:
    # GET
    #     import requests
    #     response = requests.get("https://api.example.com/data")
    #     data = response.json()    

    # POST
    #     import requests
    #     payload = {'key1': 'value1', 'key2': 'value2'}
    #     response = requests.post("https://api.example.com/data", json=payload)
    #     data = response.json()    

    # PUT
    #     import requests   
    #     payload = {'key1': 'updated_value1'}  
    #     response = requests.put("https://api.example.com/data/1", json=payload)
    #     data = response.json()

    # DELETE    
    #     import requests
    #     response = requests.delete("https://api.example.com/data/1")
    #     print(response.status_code)

    # PATCH
    #     import requests   
    #     payload = {'key1': 'patched_value1'}
    #     response = requests.patch("https://api.example.com/data/1", json=payload)
    #     data = response.json()

    # The difference between PUT and PATCH:
    # PUT is used to update an entire resource, while PATCH is used to update a part of a resource.


# VIRTUAL ENVIRONMENT SETUP:
    # python -m venv env
    # source env/bin/activate  (Linux/Mac)
    # .\env\Scripts\Activate   (Windows powershell)
    # pip install -r requirements.txt

    # used to keep dependencies organized and isolated for each project.
    # to get out of the virtual environment, simply type 'deactivate' in the terminal.


# ENVIRONMENT VARIABLES:\
    # used to store sensitive information like API keys, database credentials, etc.
    # helps keep sensitive data out of the source code.

    # Example of using environment variables in Python:
    # import os
    # api_key = os.getenv("API_KEY")