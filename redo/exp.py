from scholarly import scholarly

# Define a function to search for an author and get their Google Scholar URL
def get_scholar_profile(name):
    try:
        # Search for the author by name
        search_query = scholarly.search_author(name)
        # Attempt to get the first author in the search results
        author = next(search_query)

        # Print the author's information
        # print(author)

        # Print the Google Scholar URL
        return f"https://scholar.google.com/citations?user={author['scholar_id']}"

    except StopIteration:
        # If no authors are found, print an error message
        return None

# Example usage with a nonsense query
print(get_scholar_profile('Mauricio Alvarez'))

# Example usage with a valid query
print(get_scholar_profile('ma yi'))
