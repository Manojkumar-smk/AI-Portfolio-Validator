from supabase import create_client, Client
from app.config import Config

def get_supabase_client() -> Client:
    url = Config.SUPABASE_URL
    key = Config.SUPABASE_KEY
    
    if not url or not key or "your_supabase_url" in url:
        print("Warning: SUPABASE_URL or SUPABASE_KEY not set or is invalid.")
        return None

    try:
        return create_client(url, key)
    except Exception as e:
        print(f"Error initializing Supabase client: {e}")
        return None

supabase: Client = get_supabase_client()
