from app.services.supabase_client import supabase

def check_table():
    if not supabase:
        print("Supabase client not initialized.")
        return

    try:
        # Try to select from jobs table
        response = supabase.table("jobs").select("count", count="exact").execute()
        print("Jobs table exists. Count:", response.count)
    except Exception as e:
        print(f"Error accessing jobs table: {e}")

if __name__ == "__main__":
    check_table()
