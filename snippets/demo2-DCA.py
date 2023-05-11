from solara.express import CrossFilteredFigurePlotly
import plotly.express as px

_base_var_1 = px.scatter_3d(df2, x="Species", y="Island", z="Culmen Length (mm)", color="Sex")
_base_var_1.update_layout(margin=dict(l=0, r=0, t=40 if _base_var_1.layout.title.text else 20, b=0))
var_1 = CrossFilteredFigurePlotly(_base_var_1)

var_1