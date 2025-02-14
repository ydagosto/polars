import polars as pl

pl.Config.set_tbl_cols(20)
pl.Config.set_tbl_rows(150)
pl.Config.set_tbl_hide_column_data_types(True)
pl.Config.set_ascii_tables()

df = pl.DataFrame({"v": range(20)})

# df = pl.DataFrame({"A": ["…"]})
print(df)