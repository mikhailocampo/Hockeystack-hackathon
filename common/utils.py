import os
from supabase import create_client, Client
import pandas as pd


def init_supabase_client():
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    return supabase

def get_all_data(client: Client):
    response = client.table("clients").select("*").execute()
    return response.data

def convert_to_dataframe(data):
    return pd.DataFrame(data)

def get_all_data_as_dataframe(client: Client):
    data = get_all_data(client)
    return convert_to_dataframe(data)