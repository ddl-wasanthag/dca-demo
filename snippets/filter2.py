df = df.loc[df["Culmen Length (mm)"].notna()]
df = df[["Species", "Region", "Body Mass (g)", "Sex"]]
dfg = df.groupby(["Species", "Region", "Sex"]).agg(Body_Mass__g__min=("Body Mass (g)", "min"), Body_Mass__g__mean=("Body Mass (g)", "mean"), Body_Mass__g__max=("Body Mass (g)", "max")).reset_index()
dfg