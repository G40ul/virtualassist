from googlesearch import search

def perform_web_search(query, num_results=5):
    results = []
    
    # Perform Google search
    for result in search(query, num=num_results, stop=num_results):
        results.append(result)

    if results:
        return results
    else:
        return "No results found."

# Example usage
# print(perform_web_search("What is AI?"))
