import sqlite3
import csv

DB_PATH = "leads.db"
CSV_OUTPUT = "leads_export.csv"

def export_leads_to_csv():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM leads")
        rows = cursor.fetchall()
        
        headers = [description[0] for description in cursor.description]
        
        with open(CSV_OUTPUT, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
            
        print(f"[SUCCESS] Exported {len(rows)} leads to {CSV_OUTPUT}")
    except Exception as e:
        print(f"[EXPORT ERROR]: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    export_leads_to_csv()
