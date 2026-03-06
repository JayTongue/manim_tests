from manim import *
from manim_slides import Slide
import json
import numpy as np

config.media_dir = "./presentation_vids"
np.random.seed(42)

class Why(Slide):
    def construct(self):
        text_1 = Text('Why Does this Matter?', font_size=36)
        text_1.move_to(ORIGIN)
        
        text_2 = Text('1. Vendor Claims', font_size=24)
        text_3 = Text('2. Developing Guidelines', font_size=24)
        
        img = ImageMobject('exhibits/harvey_claims.png')
        img.scale(2)
        

        self.next_slide()
        self.play(Write(text_1))
        self.play(text_1.animate.shift(UP*2))
        self.next_slide()
        self.play(FadeIn(img))


class AnovaGraph(Slide):
    def construct(self):
        with open('data/corp_avg_dict.json', 'r') as infile:
            data = json.load(infile)
        colors = [BLUE, RED, GREEN, YELLOW, PURPLE]

        plot_axes = Axes(
            x_range=[1, 3, 1],
            y_range=[0, 7, 1],
            x_length=9,
            y_length=5.5,
            axis_config={"font_size": 24},
            x_axis_config={
                "scaling": LogBase(base=10),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 8, 1),
            },
            tips=False,
        )

        custom_ticks = [10, 25, 50, 100, 250, 500]
        tick_labels = VGroup(*[
            MathTex(str(v), font_size=20).next_to(
                plot_axes.c2p(v, 0), DOWN, buff=0.2
            )
            for v in custom_ticks
        ])

        title = Title('Aggregated Performance by Corpus', include_underline=False, font_size=40)
        y_label = plot_axes.get_y_axis_label("Correct\ Answers", edge=LEFT, direction=LEFT)
        y_label.rotate(PI/2)
        y_label.shift(LEFT * 0.5)
        x_label = plot_axes.get_x_axis_label("File\ Set\ Size", edge=DOWN)
        x_label.shift(DOWN * 0.9)
        x_label.shift(LEFT * 2)
        plot_labels = VGroup(x_label, y_label)

        lines = VGroup()
        for (label, points), color in zip(data.items(), colors):
            xs = [int(k) for k in points.keys()]
            ys = list(points.values())
            line = plot_axes.plot_line_graph(
                x_values=xs,
                y_values=ys,
                line_color=color,
                add_vertex_dots=True,
                vertex_dot_radius=0.05,
            )
            lines.add(line)

        legend_items = VGroup()
        for (label, _), color in zip(data.items(), colors):
            dot = Dot(color=color, radius=0.1)
            text = Text(label, font_size=20, color=color)
            text.next_to(dot, RIGHT, buff=0.15)
            item = VGroup(dot, text)
            legend_items.add(item)

        legend_items.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend_box = SurroundingRectangle(legend_items, color=WHITE, buff=0.2)
        legend = VGroup(legend_box, legend_items)
        legend.to_corner(UR, buff=0.5)

        self.next_slide()
        self.play(Write(title))
        self.play(Create(plot_axes), Create(plot_labels), Create(tick_labels), run_time=3)
        self.next_slide()
        self.play(Create(legend), Create(lines), run_time=10)
        self.wait()


class FTest(Slide):
    def construct(self, ):
        # Cluster 1: centered at (2, 3)
        c1_x = np.random.normal(loc=2, scale=0.5, size=30)
        c1_y = np.random.normal(loc=3, scale=0.5, size=30)

        # Cluster 2: centered at (5, 3)
        c2_x = np.random.normal(loc=5, scale=0.5, size=30)
        c2_y = np.random.normal(loc=3, scale=0.5, size=30)

        # print(c1_x, c1_y)
        # print(c2_x, c2_y)
        plot_axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 6, 1],
            x_length=9,
            y_length=5.5,
            axis_config={"font_size": 24},
            tips=False,
        )

        cluster1_dots = VGroup(*[
            Dot(plot_axes.c2p(x, y), color=BLUE, radius=0.05)
            for x, y in zip(c1_x, c1_y)
        ])

        cluster2_dots = VGroup(*[
            Dot(plot_axes.c2p(x, y), color=RED, radius=0.05)
            for x, y in zip(c2_x, c2_y)
        ])


        f_formula = MathTex(r"F = \frac{}{}", font_size=36)
        f_formula.to_edge(UP, buff=1.5) ; f_formula.shift(LEFT*3)

        numerator = MathTex(r"variation\ between\ groups", font_size=36)
        denominator = MathTex(r"variation\ within\ groups", font_size=36)
        fraction_line = Line(LEFT, RIGHT, color=WHITE).scale(2)

        fraction_line.next_to(f_formula, RIGHT, buff=0.7)
        numerator.next_to(fraction_line, UP, buff=0.2)
        denominator.next_to(fraction_line, DOWN, buff=0.2)

        original1 = cluster1_dots.get_center()
        original2 = cluster2_dots.get_center()

        self.add(cluster1_dots, cluster2_dots)
        self.next_slide()
        self.add(fraction_line, f_formula,numerator, denominator)
        self.next_slide()
        self.play(FadeOut(cluster2_dots), 
                FadeOut(f_formula), 
                FadeOut(fraction_line), 
                FadeOut(numerator), 
                FadeOut(denominator),
                cluster1_dots.animate.shift(plot_axes.c2p(3.5, 3) - plot_axes.c2p(c1_x.mean(), c1_y.mean())),
                run_time = 3)
        self.next_slide()
        self.play(cluster1_dots.animate.scale(3), run_time=3)
        self.wait()
