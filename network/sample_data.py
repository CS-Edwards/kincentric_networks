
def get_sample_ore():
    '''
    Input: None
    Return: Dict Array

    Two Generations of nuclear family model
    '''

    return [
        {"source": "Elaine", "target": "Lee", "relation":"parent"},
        {"source": "Elaine", "target": "Candace", "relation":"parent"},
        {"source": "Elaine", "target": "Basheen", "relation":"parent"},
        {"source": "Elaine", "target": "Lydia", "relation":"parent"},
        {"source": "Joseph", "target": "Lee", "relation":"parent"},
        {"source": "Joseph", "target": "Candace", "relation":"parent"},
        {"source": "Joseph", "target": "Basheen", "relation":"parent"},
        {"source": "Joseph", "target": "Lydia", "relation":"parent"},
        {"source": "Elaine", "target": "Joseph", "relation": "spouse"},
        {"source": "Joseph", "target": "Elaine", "relation": "spouse"},
        {"source": "Candace", "target": "Lee", "relation": "sibling"},
        {"source": "Lee", "target": "Candace", "relation": "sibling"},
    ]