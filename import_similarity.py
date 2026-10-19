
import os
import getpass
import pandas as pd
from neo4j import GraphDatabase

# Konfigurasi Neo4j
URI = "neo4j://127.0.0.1:7687"
USER = "neo4j"

PASSWORD = os.getenv("NEO4J_PASSWORD") or getpass.getpass(
    "Masukkan password Neo4j: "
)

# Membaca file CSV hasil similarity
df = pd.read_csv("data/similarity_user.csv")

# Menyiapkan data
rows = [
    {
        "user1": int(row.user1),
        "user2": int(row.user2),
        "similarity": float(row.similarity)
    }
    for row in df.itertuples(index=False)
]

# Menghubungkan Python dengan Neo4j
driver = GraphDatabase.driver(
    URI,
    auth=(USER, PASSWORD)
)

# Membuat relationship SIMILAR_TO
query = """
UNWIND $rows AS row
MATCH (u1:Visitor {visitorid: row.user1})
MATCH (u2:Visitor {visitorid: row.user2})
MERGE (u1)-[r:SIMILAR_TO]->(u2)
SET r.similarity = row.similarity
"""

try:
    driver.verify_connectivity()

    with driver.session(database="neo4j") as session:
        result = session.run(query, rows=rows)
        result.consume()

    print("Impor similarity berhasil!")
    print("Jumlah pasangan pada CSV:", len(rows))

finally:
    driver.close()
