import polars as pl

data = {
    "name": ["Alex", "Maria", "John", "Sara"],
    "score": [85, 92, 70, 96]
}

df = pl.DataFrame(data)
high_scores = df.filter(pl.col("score") > 80)

print(high_scores)