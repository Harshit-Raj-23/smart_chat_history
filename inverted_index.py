from utils import preprocessor

# Function to build inverted index dictionary
def build_inverted_index(messages):
    inverted_index = {}
    for i, msg in enumerate(messages):
        message = preprocessor(msg)
        for word in message:
            if word in inverted_index:
                inverted_index[word].add(i)
            else:
                inverted_index[word] = {i}
    return inverted_index

def search_query(query, inverted_index, messages):
    query_tokens = preprocessor(query)
    if not query_tokens:
        return [], []

    candidate_ids = set()
    for word in query_tokens:
        if word in inverted_index:
            candidate_ids.update(inverted_index[word])

    final_ids = list(candidate_ids)
    return final_ids, query_tokens
