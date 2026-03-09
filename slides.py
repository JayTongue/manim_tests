from manim import *
from manim_slides import Slide
import json
import numpy as np

config.media_dir = "./presentation_vids"
np.random.seed(42)

# class Intro(Slide):
#     def construct(self):
#         title = Text('Shortcuts the Long Way Around', font_size=56)
#         title.shift(UP*3)
        
#         bio = VGroup(map(lambda x: Text(x, font_size=24), ['Justin Tung',
#                                                           'Reference Librarian & Lecturer',
#                                                           'Univ. of Tex. School of Law']))
#         bio.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(LEFT*3)

#         self.next_slide()
#         self.play(Write(title))
#         self.next_slide()
#         self.play(FadeIn(bio))
#         self.next_slide()
#         self.play(map(FadeOut, [title, bio]))



# class Why(Slide):
#     def construct(self):
#         text_1 = Text('Why Does this Matter?', font_size=36)
#         text_1.move_to(ORIGIN)
        
#         text_2 = Text('1. Vendor Claims', font_size=24)
        
#         harvey_img = ImageMobject('exhibits/harvey_claims.png')
#         harvey_img.scale(0.8)

#         h_rect_1 = Rectangle(width=3.9, height=1, color=GREEN_D).set_z_index(1)
#         h_rect_1.next_to(harvey_img, UP, buff=-1.5) ; h_rect_1.shift(LEFT*1.65)
#         h_rect_2 = Rectangle(width=2.8, height=0.6, color=GREEN_D).set_z_index(1)
#         h_rect_2.next_to(harvey_img, RIGHT, buff=-3.2) ; h_rect_2.shift(DOWN*1.8)

#         lexis_img = ImageMobject('exhibits/lexis_claims.png')
#         lexis_img.scale(0.8)
#         l_rect_1 = Rectangle(width=2.7, height=0.8, color=GREEN_D).set_z_index(1)
#         l_rect_1.next_to(lexis_img, RIGHT, buff=-3.5) ; l_rect_1.shift(DOWN*1.05)
        

#         self.next_slide()
#         self.play(Write(text_1))
#         self.next_slide()
#         self.play(text_1.animate.shift(UP*2))
#         self.play(Write(text_2))
#         self.next_slide()
#         self.play(text_2.animate.shift(UP*3.5), FadeOut(text_1))
#         self.play(FadeIn(harvey_img))
#         self.next_slide()
#         self.play(FadeIn(h_rect_1))
#         self.next_slide()
#         self.play(FadeIn(h_rect_2))
#         self.next_slide()
#         self.play(map(FadeOut, [h_rect_1, h_rect_2, harvey_img]), FadeIn(lexis_img))
#         self.next_slide()
#         self.play(FadeIn(l_rect_1))
#         self.next_slide()
#         self.play(FadeOut(l_rect_1), FadeOut(lexis_img))

#         text_3 = Text('2. Developing Use Guidelines', font_size=24)

#         bullets = ['• Which tasks in my library or practice group can legal AI be used for?', 
#                    '• What is the best way of using legal AI to perform those tasks?', 
#                    '• What is the likely outcome of these use instances?', 
#                    '• Does the upsides of this use outweigh the downsides?']
#         bullets = VGroup(map(lambda x: Text(x, font_size=18), bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

#         self.play(text_2.animate.shift(DOWN*3.5), FadeIn(text_1.move_to(ORIGIN).shift(UP*2)))
#         self.next_slide()
#         self.play(Write(text_3.shift(DOWN*1)))
#         self.next_slide()
#         self.play(map(FadeOut, [text_1, text_2]), text_3.animate.shift(UP*4.5))

#         for bullet in bullets:
#             self.play(Write(bullet.shift(UP*1)))
#             self.next_slide()


class Methodology(Slide):
    def construct(self):
        prod_title = Text('Methodology', font_size=36)
        prods = Text('Products', font_size=36)
        products = ['Harvey', 'Westlaw CoCounsel 2.0', 'Lexis+ with Protégé']
        products = VGroup(map(lambda x: Text(x, font_size=24), products)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(prod_title))
        self.next_slide()
        self.play(TransformMatchingShapes(prod_title, prods)) 
        self.play(prods.animate.shift(UP*3.5), Write(products))
        self.next_slide()
        self.play(map(FadeOut, [prods, products])),

        def make_graph_line(start, end, buff=0.5):
            return Line(start=start.get_edge_center(DOWN)+DOWN*buff, end=end.get_edge_center(UP)+UP*buff)

        def draw_box(text, color=WHITE, buff=0.2):
            return SurroundingRectangle(text, color=color, buff=buff, fill_opacity=0)


        data_sources_title = Text('Data Sources', font_size=36)
        data_sources_title = VGroup(data_sources_title, draw_box(data_sources_title))
        ext_dat_text = Text('Existing Sources', font_size=24)
        ext_dat_text = VGroup(ext_dat_text, draw_box(ext_dat_text))
        ext_dat_text.shift(LEFT*2)
        synth_dat_text = Text('Synthesized Sources', font_size=24)
        synth_dat_text = VGroup(synth_dat_text, draw_box(synth_dat_text))
        synth_dat_text.shift(RIGHT*2)

        self.play(Write(data_sources_title))
        self.play(data_sources_title.animate.shift(UP*3.5), Write(ext_dat_text), Write(synth_dat_text))

        ext_line = make_graph_line(data_sources_title, ext_dat_text)
        synth_line = make_graph_line(data_sources_title, synth_dat_text)

        self.play(Create(ext_line), Create(synth_line))
        self.next_slide()

        self.play(map(lambda x: x.animate.shift(UP*3.5).shift(RIGHT*2), [data_sources_title, ext_dat_text, synth_dat_text, ext_line, synth_line]))
        self.play(map(lambda y: y.animate.set_opacity(0.3), [synth_line, synth_dat_text]))

        enron_text = Text('Enron Email \nData Set V2', font_size=24)
        enron_text = VGroup(enron_text, draw_box(enron_text)).shift(LEFT*2)
        contracts_text = Text('Material Contracts \nCorpus', font_size=24)
        contracts_text = VGroup(contracts_text, draw_box(contracts_text)).shift(RIGHT*2)

        enron_line = make_graph_line(ext_dat_text, enron_text)
        contracts_line = make_graph_line(ext_dat_text, contracts_text)

        self.play(map(Write, [enron_text, contracts_text]))
        self.play(map(Create, [enron_line, contracts_line]))
        self.next_slide()
        self.play(map(lambda x: x.animate.shift(UP*3.5).shift(RIGHT*2), [data_sources_title, 
                                                                     ext_dat_text, 
                                                                     synth_dat_text,
                                                                     ext_line,
                                                                     synth_line,
                                                                     enron_text,
                                                                     contracts_text,
                                                                     enron_line,
                                                                     contracts_line]))
        self.play(map(lambda y: y.animate.set_opacity(0.3), [contracts_text, contracts_line]))
        self.next_slide()

        enron_bullets = ['• Dataset created for Enron litigation by the Federal Energy Regulatory Commission',
                         '• Underwent many curration steps over time',
                         '• Difficult to find in its full form',
                         '• Full(?) version available from the Internet Archive',
                         '• Total Size: 258.9 GB']
        enron_bullets = VGroup(map(lambda x: Text(x, font_size=18), enron_bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(enron_bullets))
        self.next_slide()
        self.play(FadeOut(enron_bullets))
        self.play(map(lambda x: x.animate.shift(LEFT*4), [data_sources_title, 
                                                                     ext_dat_text, 
                                                                     synth_dat_text,
                                                                     ext_line,
                                                                     synth_line,
                                                                     enron_text,
                                                                     contracts_text,
                                                                     enron_line,
                                                                     contracts_line]))
        self.play(map(lambda x: x.animate.set_opacity(1), [contracts_line, contracts_text]))
        self.play(map(lambda x: x.animate.set_opacity(0.3), [enron_line, enron_text]))
        self.next_slide()

        contract_bullets = ['• Compiled by Peter Adelson and Prof Julian Nyarko in 2025', 
                             '• Contains commercial contracts and metadata from the SEC\'s EDGAR',
                             '• Coverage Date: 2000-2023',
                             '• Total Size: 156.2 GB']
        contract_bullets = VGroup(map(lambda x: Text(x, font_size=18), contract_bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(contract_bullets))
        self.next_slide()
        self.play(FadeOut(contract_bullets))
        self.play(map(lambda x: x.animate.set_opacity(1), [enron_line, enron_text]))
        self.play(map(lambda x: x.animate.shift(RIGHT*2), [data_sources_title, 
                                                                     ext_dat_text, 
                                                                     synth_dat_text,
                                                                     ext_line,
                                                                     synth_line,
                                                                     enron_text,
                                                                     contracts_text,
                                                                     enron_line,
                                                                     contracts_line]))
        
        def logify(bins):
            return np.log10(np.array(bins)+1).tolist()

        bins = json.load(open('data/file_sizes/bin_counts.json', 'r'))
        enron_graph = BarChart(values=logify(bins['lin']['enron']),
                                y_range=[0, 8],
                                y_length=5,
                                x_length=7,
                                bar_colors=[PURPLE_D],
                                x_axis_config={'include_ticks': False}
                            )
        enron_graph.y_axis.numbers.set_opacity(0)
        enron_graph.scale(0.5).shift(LEFT*2)
        contracts_graph = BarChart(values=logify(bins['lin']['contracts']),
                                y_range=[0, 8],
                                y_length=5,
                                x_length=7,
                                bar_colors=[BLUE_D],
                                x_axis_config={'include_ticks': False}
                            )
        contracts_graph.y_axis.numbers.set_opacity(0)
        contracts_graph.scale(0.5).shift(RIGHT*4)
        
        self.play(GrowFromEdge(enron_graph, DOWN), 
                  GrowFromEdge(contracts_graph, DOWN))
        self.next_slide()
        self.play(FadeOut(enron_graph), FadeOut(contracts_graph))
        enron_graph.change_bar_values(logify(bins['log']['enron']))
        contracts_graph.change_bar_values(logify(bins['log']['contracts']))
        self.play(GrowFromEdge(enron_graph, DOWN), GrowFromEdge(contracts_graph, DOWN))

        



# class AnovaGraph(Slide):
#     def construct(self):
#         with open('data/corp_avg_dict.json', 'r') as infile:
#             data = json.load(infile)
#         colors = [BLUE, RED, GREEN, YELLOW, PURPLE]

#         plot_axes = Axes(
#             x_range=[1, 3, 1],
#             y_range=[0, 7, 1],
#             x_length=9,
#             y_length=5.5,
#             axis_config={"font_size": 24},
#             x_axis_config={
#                 "scaling": LogBase(base=10),
#             },
#             y_axis_config={
#                 "numbers_to_include": np.arange(0, 8, 1),
#             },
#             tips=False,
#         )

#         custom_ticks = [10, 25, 50, 100, 250, 500]
#         tick_labels = VGroup(*[
#             MathTex(str(v), font_size=20).next_to(
#                 plot_axes.c2p(v, 0), DOWN, buff=0.2
#             )
#             for v in custom_ticks
#         ])

#         title = Title('Aggregated Performance by Corpus', include_underline=False, font_size=40)
#         y_label = plot_axes.get_y_axis_label("Correct\ Answers", edge=LEFT, direction=LEFT)
#         y_label.rotate(PI/2)
#         y_label.shift(LEFT * 0.5)
#         x_label = plot_axes.get_x_axis_label("File\ Set\ Size", edge=DOWN)
#         x_label.shift(DOWN * 0.9)
#         x_label.shift(LEFT * 2)
#         plot_labels = VGroup(x_label, y_label)

#         lines = VGroup()
#         for (label, points), color in zip(data.items(), colors):
#             xs = [int(k) for k in points.keys()]
#             ys = list(points.values())
#             line = plot_axes.plot_line_graph(
#                 x_values=xs,
#                 y_values=ys,
#                 line_color=color,
#                 add_vertex_dots=True,
#                 vertex_dot_radius=0.05,
#             )
#             lines.add(line)

#         legend_items = VGroup()
#         for (label, _), color in zip(data.items(), colors):
#             dot = Dot(color=color, radius=0.1)
#             text = Text(label, font_size=20, color=color)
#             text.next_to(dot, RIGHT, buff=0.15)
#             item = VGroup(dot, text)
#             legend_items.add(item)

#         legend_items.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
#         legend_box = SurroundingRectangle(legend_items, color=WHITE, buff=0.2)
#         legend = VGroup(legend_box, legend_items)
#         legend.to_corner(UR, buff=0.5)

#         self.next_slide()
#         self.play(Write(title))
#         self.play(Create(plot_axes), Create(plot_labels), Create(tick_labels), run_time=3)
#         self.next_slide()
#         self.play(Create(legend), Create(lines), run_time=10)
#         self.wait()



# class FTest(Slide):
#     def construct(self, ):
#         # Cluster 1: centered at (2, 3)
#         c1_x = np.random.normal(loc=2, scale=0.5, size=30)
#         c1_y = np.random.normal(loc=3, scale=0.5, size=30)

#         # Cluster 2: centered at (5, 3)
#         c2_x = np.random.normal(loc=5, scale=0.5, size=30)
#         c2_y = np.random.normal(loc=3, scale=0.5, size=30)

#         # print(c1_x, c1_y)
#         # print(c2_x, c2_y)
#         plot_axes = Axes(
#             x_range=[0, 7, 1],
#             y_range=[0, 6, 1],
#             x_length=9,
#             y_length=5.5,
#             axis_config={"font_size": 24},
#             tips=False,
#         )

#         cluster1_dots = VGroup(*[
#             Dot(plot_axes.c2p(x, y), color=BLUE, radius=0.05)
#             for x, y in zip(c1_x, c1_y)
#         ])

#         cluster2_dots = VGroup(*[
#             Dot(plot_axes.c2p(x, y), color=RED, radius=0.05)
#             for x, y in zip(c2_x, c2_y)
#         ])


#         f_formula = MathTex(r"F = \frac{}{}", font_size=36)
#         f_formula.to_edge(UP, buff=1.5) ; f_formula.shift(LEFT*3)

#         numerator = MathTex(r"variation\ between\ groups", font_size=36)
#         denominator = MathTex(r"variation\ within\ groups", font_size=36)
#         fraction_line = Line(LEFT, RIGHT, color=WHITE).scale(2)

#         fraction_line.next_to(f_formula, RIGHT, buff=0.7)
#         numerator.next_to(fraction_line, UP, buff=0.2)
#         denominator.next_to(fraction_line, DOWN, buff=0.2)

#         original1 = cluster1_dots.get_center()
#         original2 = cluster2_dots.get_center()

#         self.add(cluster1_dots, cluster2_dots)
#         self.next_slide()
#         self.add(fraction_line, f_formula,numerator, denominator)
#         self.next_slide()
#         self.play(FadeOut(cluster2_dots), 
#                 FadeOut(f_formula), 
#                 FadeOut(fraction_line), 
#                 FadeOut(numerator), 
#                 FadeOut(denominator),
#                 cluster1_dots.animate.shift(plot_axes.c2p(3.5, 3) - plot_axes.c2p(c1_x.mean(), c1_y.mean())),
#                 run_time = 3)
#         self.next_slide()
#         self.play(cluster1_dots.animate.scale(3), run_time=3)
#         self.wait()