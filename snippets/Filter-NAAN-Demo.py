df2 = df.loc[df["Culmen Depth (mm)"].notna()]
df2 = df2.loc[df2["Sex"].notna()]
df2 = df2[["Species", "Region", "Island", "Sex", "Body Mass (g)"]]
dfg = df2.groupby(["Species", "Region", "Island", "Sex"]).agg(Body_Mass__g__mean=("Body Mass (g)", "mean"), Body_Mass__g__min=("Body Mass (g)", "min"), Body_Mass__g__max=("Body Mass (g)", "max")).reset_index()
dfg