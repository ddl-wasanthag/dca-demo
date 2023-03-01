df2 = df.loc[df["Culmen Depth (mm)"].notna()]
df2 = df2.loc[df2["Sex"].notna()]
df3 = df2[["Species", "Island", "Body Mass (g)", "Sex"]]
dfg = df3.groupby(["Species", "Island", "Sex"]).agg(Body_Mass__g__min=("Body Mass (g)", "min"), Body_Mass__g__mean=("Body Mass (g)", "mean"), Body_Mass__g__max=("Body Mass (g)", "max")).reset_index()
dfg