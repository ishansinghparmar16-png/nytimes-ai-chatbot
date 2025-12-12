"""
NY Times Article Search API integration.
"""
import requests
from typing import List, Dict, Optional
from config import settings


class NYTArticle:
    """Represents a NY Times article with relevant metadata."""
    
    def __init__(self, article_data: Dict):
        self.headline = article_data.get("headline", {}).get("main", "No headline")
        self.abstract = article_data.get("abstract", "")
        self.lead_paragraph = article_data.get("lead_paragraph", "")
        self.web_url = article_data.get("web_url", "")
        self.pub_date = article_data.get("pub_date", "")
        self.news_desk = article_data.get("news_desk", "")
        self.section_name = article_data.get("section_name", "")
        self.snippet = article_data.get("snippet", "")
        
    def to_dict(self) -> Dict:
        """Convert article to dictionary format."""
        return {
            "headline": self.headline,
            "abstract": self.abstract,
            "lead_paragraph": self.lead_paragraph,
            "web_url": self.web_url,
            "pub_date": self.pub_date,
            "news_desk": self.news_desk,
            "section_name": self.section_name,
            "snippet": self.snippet,
        }
    
    def get_summary_text(self) -> str:
        """Get a combined summary text for the article."""
        parts = [
            f"Title: {self.headline}",
            f"Published: {self.pub_date}",
        ]
        
        if self.abstract:
            parts.append(f"Abstract: {self.abstract}")
        elif self.lead_paragraph:
            parts.append(f"Content: {self.lead_paragraph}")
        elif self.snippet:
            parts.append(f"Snippet: {self.snippet}")
            
        parts.append(f"URL: {self.web_url}")
        
        return "\n".join(parts)


class NYTSearchTool:
    """Tool for searching NY Times articles."""
    
    def __init__(self):
        self.api_key = settings.nyt_api_key
        self.base_url = settings.nyt_api_base_url
        
    def search_articles(
        self,
        query: str,
        filters: Optional[Dict] = None,
        begin_date: Optional[str] = None,
        end_date: Optional[str] = None,
        max_results: int = None
    ) -> List[NYTArticle]:
        """
        Search for articles in the NY Times archive.
        
        Args:
            query: Search query string
            filters: Optional filters like {"news_desk": "Science"}
            begin_date: Start date in YYYYMMDD format
            end_date: End date in YYYYMMDD format
            max_results: Maximum number of articles to return
            
        Returns:
            List of NYTArticle objects
        """
        if max_results is None:
            max_results = settings.max_articles_to_fetch
            
        endpoint = f"{self.base_url}/articlesearch.json"
        
        params = {
            "q": query,
            "api-key": self.api_key,
            "sort": "relevance",
        }
        
        # Add optional filters
        if filters:
            if "news_desk" in filters:
                params["fq"] = f'news_desk:("{filters["news_desk"]}")'
                
        if begin_date:
            params["begin_date"] = begin_date
            
        if end_date:
            params["end_date"] = end_date
            
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            docs = data.get("response", {}).get("docs", [])
            
            # Convert to NYTArticle objects and limit results
            articles = [NYTArticle(doc) for doc in docs[:max_results]]
            
            return articles
            
        except requests.exceptions.RequestException as e:
            print(f"Error calling NY Times API: {e}")
            return []
        except Exception as e:
            print(f"Error processing NY Times response: {e}")
            return []
    
    def format_articles_for_llm(self, articles: List[NYTArticle]) -> str:
        """Format articles in a readable format for LLM processing."""
        if not articles:
            return "No articles found."
        
        formatted = []
        for i, article in enumerate(articles, 1):
            formatted.append(f"\n--- Article {i} ---")
            formatted.append(article.get_summary_text())
            
        return "\n".join(formatted)

