import polars as pl

def frame(a,b):
    data = {"a": a, "b": b}
    df = pl.DataFrame(data)
    return df
