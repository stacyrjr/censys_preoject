DESCRIPTON

This project provides a web-based interface to search for IPv4 hosts using 
the Censys API. Users can input a query, retrieve search results, and load 
additional results by clicking a "Load More" button. Each result includes 
an IP address and a count of services running on that host.

SETUP
1) Git clone the project!

2) Install the required packages to run the project.
    The following commands wiil install the package you need
   ```
    pip install flask 
    pip install censys 
    pip install python-dotenv
   ```

4) Create a Censys search account at [Censys Search API](https://search.censys.io/api).

5) Go to your account page under the API Tab and copy the API ID and the Secret key.
   These are your API credentials
   
6) Create a .env file in the project’s root directory to store your Censys API credentials:
   The file should contain this, but with you ID and Key
  ```
   CENSYS_API_ID=<your_api_id_here>
   CENSYS_API_SECRET=<your_api_secret_here>
  ```

At this point your project structure should look like this:

```
your_clone_root_dir/
├── main.py  # Flask app, and Censys API code
├── .env     # Your Censys API credentials
└── templates/
    └── index.html # HTML file with JavaScript for search and pagination
```

RUNNING THE PROJECT
1) Start the Flask application:
    In a terminal, navigate to the project directory and run `python main.py`

2) Open a web browser and navigate to `localhost:8080`

EXAMPLE QUERY - Testing the application

While the project is running enter: 
`services.service_name: HTTP`
into the input field and hit search

This will return five {IP, Number of services} pairs with an option to load five more 
until results of the search are exhausted. When exhausted an alert will pop up
letting the user know there are no more results and the load more button will disappear

This is an example pair:
`1.1.1.1 - Protocols: 12`

For errors the user will be notified by alert, or an output to the browser console.
This runs on a template which should make it safe from attacks with bad characters.
