from flask import Flask, request, jsonify
import your_scraping_script  # Replace with your actual script name

app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    search_term = data.get('searchTerm')
    
    # Call your scraping script function here with the search term
    # For example: results = your_scraping_script.search(search_term)
    # Replace the above line with actual function call from your script
    
    # For demonstration, I'll just return the search term
    results = {"searchTerm": search_term, "results": []} 
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)