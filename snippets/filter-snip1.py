import io
import pandas as pd
from domino.data_sources import DataSourceClient

ds = DataSourceClient().get_datasource("Amazon-S3-DataSource")

data = io.BytesIO(ds.get("penguins_lter.csv"))
df = pd.read_csv(data)

df