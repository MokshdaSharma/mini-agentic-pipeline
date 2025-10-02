import pandas as pd

class Actor:
    def __init__(self):
        self.csv_path = "data/prices.csv"
        self.df = pd.read_csv(self.csv_path)

    def run_tool(self, tool, query):
        if tool == "csv_lookup":
            # Very simple demo: lookup by 'item' column
            for _, row in self.df.iterrows():
                if row["item"].lower() in query.lower():
                    return f"{row['item']} costs {row['price']}"
            return "Item not found in CSV."
        return "Unknown tool."
