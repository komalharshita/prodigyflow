# web_search.py
class WebSearchTool:
    def __init__(self, api_client=None):
        self.client = api_client  # replace with actual client

    def search(self, query, top_k=5):
        """
        Return list of dicts: [{'title':..., 'url':..., 'snippet':...}, ...]
        This is a stub: in production, call Google/Bing or a crawler.
        """
        # Example stub result
        return [
            {"title": f"Result {i} for {query}", "url": f"https://example.com/{i}", "snippet": "Short summary"}
            for i in range(1, top_k+1)
        ]
