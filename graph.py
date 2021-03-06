import json

from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.commons.utils import JsCode
from pyecharts.options.global_options import InitOpts, TitleOpts

categories = []

with open("/home/riko/temp/result.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links = j
c = (
    Graph(init_opts=opts.InitOpts(page_title="S1-拳宇宙"))
    .add(
        "",
        nodes,
        links,
        categories,
        repulsion=40000,
        edge_length=[1500,1000],
        is_draggable = False,
        layout = 'force',
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(
            is_show=False,
            # formatter='{c}'
            ),
        tooltip_opts=opts.TooltipOpts(
            is_show=True
        )
        # edge_symbol='arrow',
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="S1-拳宇宙",
        subtitle="物以类聚，人以群分"),
        )
    .render("/home/riko/temp/label.html")
)
