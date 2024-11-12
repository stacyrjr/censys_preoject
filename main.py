import os
from censys.search import CensysHosts
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Initialize Censys API client
api_id = os.getenv("CENSYS_API_ID")
api_secret = os.getenv("CENSYS_API_SECRET")
censys_client = CensysHosts(api_id, api_secret)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is in a templates folder


def search():
    # Define your query to search for hosts with HTTP service
    query = request.args.get('query', '')
    
    # Perform search with a per_page limit of 5 results per page
    results_list = censys_client.search(query=query, per_page=5, pages=10)
    response = []
    # Iterate through each result
    for result in results_list:
        for host in result:
            # Get IP address for the host
            ip = host.get("ip")
            
            # Get the list of services for this host
            services = host.get("services", [])
            
            # Append the IP and the number of services to results
            response.append({"ip": ip, "num_services": len(services)})

    return response


@app.route('/search', methods=['GET'])
def search_results():
    # Call the search function and get the results
    results = search()
    
    # Return the results as JSON
    return jsonify({"results": results})

# Run the search function
if __name__ == "__main__":
    app.run(debug=True, port=8080)
