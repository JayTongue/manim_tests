from manim import *
from manim_slides import Slide
import json
import numpy as np
import math
import copy
import random

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
        # prod_title = Text('Methodology', font_size=36)
        # prods = Text('Products', font_size=36)
        # products = ['Harvey', 'Westlaw CoCounsel 2.0', 'Lexis+ with Protégé']
        # products = VGroup(map(lambda x: Text(x, font_size=24), products)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # self.play(Write(prod_title))
        # self.next_slide()
        # self.play(TransformMatchingShapes(prod_title, prods)) 
        # self.play(prods.animate.shift(UP*3.5), Write(products))
        # self.next_slide()
        # self.play(map(FadeOut, [prods, products])),

        def make_graph_line(start, end, buff=0.5):
            return Line(start=start.get_edge_center(DOWN)+DOWN*buff, end=end.get_edge_center(UP)+UP*buff)

        def draw_box(text, color=WHITE, buff=0.2):
            return SurroundingRectangle(text, color=color, buff=buff, fill_opacity=0)


        # data_sources_title = Text('Data Sources', font_size=36)
        # data_sources_title = VGroup(data_sources_title, draw_box(data_sources_title))
        # ext_dat_text = Text('Existing Sources', font_size=24).shift(LEFT*2)
        # ext_dat_box = draw_box(ext_dat_text)
        # # ext_dat_text = VGroup(ext_dat_text, draw_box(ext_dat_text))
        # synth_dat_text = Text('Synthesized Sources', font_size=24).shift(RIGHT*2)
        # synth_dat_box = draw_box(synth_dat_text)
        # # synth_dat_text = VGroup(synth_dat_text, draw_box(synth_dat_text))

        # self.play(Write(data_sources_title))
        # self.play(data_sources_title.animate.shift(UP*3.5), 
        #           Write(ext_dat_text), 
        #           Create(ext_dat_box),
        #           Write(synth_dat_text),
        #           Create(synth_dat_box))

        # ext_line = make_graph_line(data_sources_title, ext_dat_box)
        # synth_line = make_graph_line(data_sources_title, synth_dat_box)

        # self.play(Create(ext_line), Create(synth_line))
        # self.next_slide()

        # self.play(map(lambda x: x.animate.shift(UP*3.5).shift(RIGHT*2), [data_sources_title, 
        #                                                                  ext_dat_text, 
        #                                                                  ext_dat_box,
        #                                                                  synth_dat_text,
        #                                                                  synth_dat_box, 
        #                                                                  ext_line, 
        #                                                                  synth_line]))
        # self.play(map(lambda y: y.animate.set_opacity(0.3), [synth_line, 
        #                                                      synth_dat_text]))

        # enron_text = Text('Enron Email \nData Set V2', font_size=24).shift(LEFT*2)
        # enron_box = draw_box(enron_text)
        # # enron_text = VGroup(enron_text, draw_box(enron_text))
        # contracts_text = Text('Material Contracts \nCorpus', font_size=24).shift(RIGHT*2)
        # contracts_box = draw_box(contracts_text)
        # # contracts_text = VGroup(contracts_text, draw_box(contracts_text))

        # enron_line = make_graph_line(ext_dat_box, enron_box)
        # contracts_line = make_graph_line(ext_dat_box, contracts_box)

        # self.play(map(Write, [enron_text, contracts_text]))
        # self.play(map(Create, [enron_line, contracts_line, enron_box, contracts_box]))
        # self.next_slide()
        # self.play(map(lambda x: x.animate.shift(UP*3.3).shift(RIGHT*2), [data_sources_title, 
        #                                                              ext_dat_text, 
        #                                                              ext_dat_box,
        #                                                              synth_dat_text,
        #                                                              synth_dat_box,
        #                                                              ext_line,
        #                                                              synth_line,
        #                                                              enron_text,
        #                                                              enron_box,
        #                                                              contracts_text,
        #                                                              contracts_box,
        #                                                              enron_text,
        #                                                              enron_line,
        #                                                              contracts_line]))
        # self.play(map(lambda y: y.animate.set_opacity(0.3), [contracts_text,  
        #                                                      contracts_line]), 
        #                                                      contracts_box.animate.set_fill(0))

        # enron_bullets = ['• Dataset created for Enron litigation by the Federal Energy Regulatory Commission',
        #                  '• Underwent many curration steps over time',
        #                  '• Difficult to find in its full form',
        #                  '• Full(?) version available from the Internet Archive',
        #                  '• Total Size: 258.9 GB']
        # enron_bullets = VGroup(map(lambda x: Text(x, font_size=18), enron_bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # self.play(Write(enron_bullets))
        # self.next_slide()
        # self.play(FadeOut(enron_bullets))
        # self.play(map(lambda x: x.animate.shift(LEFT*4), [data_sources_title, 
        #                                                              ext_dat_text, 
        #                                                              ext_dat_box,
        #                                                              synth_dat_text,
        #                                                              synth_dat_box,
        #                                                              ext_line,
        #                                                              synth_line,
        #                                                              enron_text,
        #                                                              enron_box,
        #                                                              contracts_text,
        #                                                              contracts_box,
        #                                                              enron_line,
        #                                                              contracts_line]))
        # self.play(map(lambda x: x.animate.set_opacity(1), [contracts_line, 
        #                                                    contracts_text]), 
        #                                                    contracts_box.animate.set_fill(0), 
        #         map(lambda x: x.animate.set_opacity(0.3), [enron_line, enron_text]))

        # contract_bullets = ['• Compiled by Peter Adelson and Prof Julian Nyarko in 2025', 
        #                      '• Contains commercial contracts and metadata from the SEC\'s EDGAR',
        #                      '• Coverage Date: 2000-2023',
        #                      '• Total Size: 156.2 GB']
        # contract_bullets = VGroup(map(lambda x: Text(x, font_size=18), contract_bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # self.play(Write(contract_bullets))
        # self.next_slide()
        # self.play(FadeOut(contract_bullets))
        # self.play(map(lambda x: x.animate.set_opacity(1), [enron_line, 
        #                                                    enron_text]), 
        #                                                    enron_box.animate.set_fill(0))
        # self.play(map(lambda x: x.animate.shift(RIGHT*2), [data_sources_title, 
        #                                                              ext_dat_text, 
        #                                                              ext_dat_box,
        #                                                              synth_dat_text,
        #                                                              synth_dat_box,
        #                                                              ext_line,
        #                                                              synth_line,
        #                                                              enron_text,
        #                                                              enron_box,
        #                                                              contracts_text,
        #                                                              contracts_box,
        #                                                              enron_line,
        #                                                              contracts_line]))
        
        # def logify(bins):
        #     return np.log10(np.array(bins)+1).tolist()

        # bins = json.load(open('data/file_sizes/bin_counts.json', 'r'))
        # enron_graph = BarChart(values=logify(bins['lin']['enron']),
        #                         y_range=[0, 8],
        #                         y_length=5,
        #                         x_length=7,
        #                         bar_colors=[PURPLE_D],
        #                         x_axis_config={'include_ticks': False}
        #                     )
        # enron_graph.y_axis.numbers.set_opacity(0)
        # enron_graph.scale(0.5).shift(LEFT*1.5)
        # contracts_graph = BarChart(values=logify(bins['lin']['contracts']),
        #                         y_range=[0, 8],
        #                         y_length=5,
        #                         x_length=7,
        #                         bar_colors=[BLUE_D],
        #                         x_axis_config={'include_ticks': False}
        #                     )
        # contracts_graph.y_axis.numbers.set_opacity(0)
        # contracts_graph.scale(0.5).shift(RIGHT*3)

        # big_line = Line(LEFT*3, RIGHT*3).shift(DOWN*2.5)
        # ticks = VGroup([Line(UP*0.1, DOWN*0.1).shift(LEFT*j).shift(DOWN*2.5)  for j in [i-3 for i in range(6,-1,-1)]])
        # updated_tick_pos = [math.log(i, 10)*7.1-3 for i in range(1, 8)]

        # lin_text = Text('Linear Scale', font_size=18).shift(DOWN*2)
        # log_text = Text('Log Scale', font_size=18).shift(DOWN*2)
        # log_norm_text = Text('Lognormal Distribution', font_size=24).shift(DOWN*3)

        # self.play(GrowFromEdge(enron_graph, DOWN), 
        #           GrowFromEdge(contracts_graph, DOWN),)
        # self.next_slide()
        # self.play(Write(lin_text), Create(big_line), Create(ticks))
        # self.next_slide()
        # self.play(TransformMatchingShapes(lin_text, log_text), 
        #           map(lambda n: ticks[n].animate.move_to(np.array([updated_tick_pos[n], -2.5, 0])), 
        #               [i for i in range(7)]))
        # self.play(FadeOut(enron_graph), FadeOut(contracts_graph))
        # enron_graph.change_bar_values(logify(bins['log']['enron']))
        # contracts_graph.change_bar_values(logify(bins['log']['contracts']))
        # self.play(GrowFromEdge(enron_graph, DOWN), GrowFromEdge(contracts_graph, DOWN))
        # self.next_slide()
        # self.play(Write(log_norm_text))

        # log_normal_formula = MathTex(r"X", r"=", r"e^{", r"\mu", r"+", r"\sigma", r"Z", r"}")

        # mu_label = Text("mean", font_size=18)
        # sigma_label = Text("standard\ndeviation", font_size=18)
        # z_label = Text("normal random\nvariable", font_size=18)

        # # position labels
        # mu_label.next_to(log_normal_formula.get_part_by_tex(r"\mu"), UP, buff=1)
        # sigma_label.next_to(log_normal_formula.get_part_by_tex(r"\sigma"), DOWN*0.5, buff=1.5).shift(LEFT*0.5)
        # z_label.next_to(log_normal_formula.get_part_by_tex("Z"), DOWN*0.5, buff=2).shift(RIGHT*1.5)

        # # draw lines from formula to labels
        # mu_line = Line(log_normal_formula.get_part_by_tex(r"\mu").get_top(), mu_label.get_bottom(), buff=0.2)
        # sigma_line = Line(log_normal_formula.get_part_by_tex(r"\sigma").get_bottom(), sigma_label.get_top(), buff=0.2)
        # z_line = Line(log_normal_formula.get_part_by_tex("Z").get_bottom(), z_label.get_top(), buff=0.2)

        # enron_params = VGroup(
        #     MathTex(r"\mu = 9.0723", font_size=30),
        #     MathTex(r"\sigma = 1.8434", font_size=30)
        # ).arrange(DOWN, aligned_edge=LEFT).shift(UP*1.8).shift(LEFT*3)

        # contracts_params = VGroup(
        #     MathTex(r"\mu = 10.866", font_size=30),
        #     MathTex(r"\sigma = 1.4167", font_size=30)
        # ).arrange(DOWN, aligned_edge=LEFT).shift(UP*1.8).shift(RIGHT*3)

        # avg_params = VGroup(
        #     MathTex(r"\mu = 9.96915", font_size=30),
        #     MathTex(r"\sigma = 1.63005", font_size=30)
        # ).arrange(DOWN, aligned_edge=LEFT).shift(UP*1.8)
        
        # self.next_slide()
        # self.play(map(FadeOut, [enron_graph, contracts_graph, log_text, ticks, big_line]))
        # self.play(log_norm_text.animate.shift(UP*1.5), Write(log_normal_formula))
        # self.next_slide()
        # self.play(Create(mu_line), Write(mu_label), log_norm_text.animate.shift(DOWN*1))
        # self.play(Create(sigma_line), Write(sigma_label))
        # self.play(Create(z_line), Write(z_label))
        # self.next_slide()
        # self.play(map(FadeOut, [mu_line, mu_label, sigma_line, sigma_label, z_line, z_label]), 
        #           Write(enron_params), Write(contracts_params), log_norm_text.animate.shift(UP*1))
        # self.next_slide()
        # self.play(enron_params.animate.shift(RIGHT*3), contracts_params.animate.shift(LEFT*3))
        # self.play(TransformMatchingShapes(enron_params, avg_params), FadeOut(contracts_params))

        # func = MathTex(r"X = e^{9.97 + 1.63 Z}")

        # self.next_slide()
        # self.play(TransformMatchingShapes(log_normal_formula, func), FadeOut(avg_params))
        # self.next_slide()
        # self.play(func.animate.shift(DOWN*1), FadeOut(log_norm_text))
        # self.play(map(lambda x: x.animate.shift(LEFT*4).shift(DOWN*7), [data_sources_title, 
        #                                                         ext_dat_text, 
        #                                                         ext_dat_box,
        #                                                         synth_dat_text,
        #                                                         synth_dat_box,
        #                                                         ext_line,
        #                                                         synth_line,
        #                                                         enron_text,
        #                                                         enron_box,
        #                                                         contracts_text,
        #                                                         contracts_box,
        #                                                         enron_line,
        #                                                         contracts_line]))
        # self.play(map(FadeOut, [enron_box, 
        #                       enron_line, 
        #                       enron_text, 
        #                       contracts_box, 
        #                       contracts_line, 
        #                       contracts_text])) 
        # self.play(synth_dat_text.animate.set_opacity(1), 
        #           synth_line.animate.set_opacity(1), 
        #           ext_dat_text.animate.set_opacity(0.3), 
        #           ext_line.animate.set_opacity(0.3))
        
        # markov_text = Text('Markov Text', font_size=24).shift(RIGHT*3)
        # markov_box = draw_box(markov_text)
        # random_text = Text('Random Text', font_size=24)
        # random_box = draw_box(random_text)
        # zeros_text = Text('Zeros', font_size=24).shift(LEFT*3)
        # zeros_box = draw_box(zeros_text)
        
        # self.next_slide()
        # self.play(func.animate.shift(UP*3.7),
        #           map(lambda x: x.animate.shift(UP*3.5), [data_sources_title, 
        #                                                         ext_dat_text, 
        #                                                         ext_dat_box,
        #                                                         synth_dat_text,
        #                                                         synth_dat_box,
        #                                                         ext_line,
        #                                                         synth_line,
        #                                                         func]))
        
        # self.play(map(Write, [markov_text, random_text, zeros_text]))
        # markov_line = make_graph_line(func, markov_box)
        # random_line = make_graph_line(func, random_box)
        # zeros_line = make_graph_line(func, zeros_box)
        # self.play(map(Create, [markov_box, markov_line,
        #                        random_box, random_line, 
        #                        zeros_box, zeros_line]))
        # self.next_slide()
        # self.play(map(lambda x: x.animate.shift(UP*3.5).shift(RIGHT*3), [data_sources_title, 
        #                                                         ext_dat_text, 
        #                                                         ext_dat_box,
        #                                                         synth_dat_text,
        #                                                         synth_dat_box,
        #                                                         ext_line,
        #                                                         synth_line,
        #                                                         func,
        #                                                         markov_text,
        #                                                         markov_box,
        #                                                         markov_line,
        #                                                         random_text,
        #                                                         random_box,
        #                                                         random_line,
        #                                                         zeros_text,
        #                                                         zeros_box,
        #                                                         zeros_line]))
        # self.play(map(lambda x: x.animate.set_opacity(0.3), [random_text, random_line, markov_text, markov_line]))

        # zeros_samp =  Text('00000000000\n00000000000\n00000000000\n00000000000', font_size=24)
        # random_samp = Text('26c1e3ae1d4\n7faf7b4579b\n353ab30e6d8\nba0c6d9e6fa', font_size=24)

        # self.next_slide()
        # self.play(Write(zeros_samp))
        # self.next_slide()
        # self.play(map(lambda x: x.animate.shift(LEFT*3), [data_sources_title, 
        #                                                         ext_dat_text, 
        #                                                         ext_dat_box,
        #                                                         synth_dat_text,
        #                                                         synth_dat_box,
        #                                                         ext_line,
        #                                                         synth_line,
        #                                                         func,
        #                                                         markov_text,
        #                                                         markov_box,
        #                                                         markov_line,
        #                                                         random_text,
        #                                                         random_box,
        #                                                         random_line,
        #                                                         zeros_text,
        #                                                         zeros_box,
        #                                                         zeros_line,
        #                                                         zeros_samp]))
        # self.play(Write(random_samp), 
        #           map(lambda x: x.animate.set_opacity(0.3), [zeros_text, zeros_line]),
        #           map(lambda x: x.animate.set_opacity(1), [random_text, random_line]))

        # phrase = MarkupText('"the real difference between the test of happiness\nand the test of will is simply that the test of\nhappiness is a test and the other isn\'t"', font_size=24)
        # phrase_orig = copy.deepcopy(phrase)

        # arrow = CurvedArrow(start_point=phrase.get_top() + LEFT * 3 + UP*0.1,
        #                     end_point=phrase.get_top() + LEFT * 2.5 + UP*0.1,
        #                     angle=-PI/3,
        #                     tip_length=0.15)

        # self.next_slide()
        # self.play(map(FadeOut, [zeros_samp, random_samp]))
        # self.play(map(lambda x: x.animate.set_opacity(0.3), [random_text, random_line]),
        #           map(lambda x: x.animate.set_opacity(1), [markov_text, markov_line])) 
        # self.play(map(lambda x: x.animate.shift(LEFT*3), [data_sources_title, 
        #                                                         ext_dat_text, 
        #                                                         ext_dat_box,
        #                                                         synth_dat_text,
        #                                                         synth_dat_box,
        #                                                         ext_line,
        #                                                         synth_line,
        #                                                         func,
        #                                                         markov_text,
        #                                                         markov_box,
        #                                                         markov_line,
        #                                                         random_text,
        #                                                         random_box,
        #                                                         random_line,
        #                                                         zeros_text,
        #                                                         zeros_box,
        #                                                         zeros_line]))
        # self.next_slide()
        # self.play(Write(phrase))
        # self.next_slide()
        # self.play(Create(arrow))
        # self.next_slide()

        # chain_0 = MarkupText("{\n'the': {'real': 1},\n}", font_size=24).shift(RIGHT*3)
        # self.play(phrase.animate.shift(LEFT*3), arrow.animate.shift(LEFT*3), Write(chain_0))
        # self.next_slide()
        # chain_1 = MarkupText("{\n'the': {'real': 1},\n'real': {'difference': 1},\n}", font_size=24).shift(RIGHT*3)
        # self.play(arrow.animate.shift(RIGHT*0.6))
        # self.play(chain_0.animate.become(chain_1.move_to(chain_0)))
        # self.next_slide()
        # chain_2 = MarkupText("{\n'the': {'real': 1},\n'real': {'difference': 1},\n'difference': {'between': 1}\n}", font_size=24).shift(RIGHT*3)
        # self.play(arrow.animate.shift(RIGHT*1.3))
        # self.play(chain_0.animate.become(chain_2.move_to(chain_0)))
        # chain_3 = MarkupText("{\n'the': {'real': 1},\n'real': {'difference': 1},\n'difference': {'between': 1},\n'between': {'the'}\n}", font_size=24).shift(RIGHT*3)
        # self.play(arrow.animate.shift(RIGHT*1.4))
        # self.play(chain_0.animate.become(chain_3.move_to(chain_0)))
        # self.next_slide()
        # chain_4 = MarkupText("{\n'the': {'real': 1, 'test': 1},\n'real': {'difference': 1},\n'difference': {'between': 1},\n'between': {'the'}\n}", font_size=24).shift(RIGHT*3)
        # self.play(arrow.animate.shift(RIGHT*0.6))
        # self.play(chain_0.animate.become(chain_4.move_to(chain_0)))
        # self.next_slide()
        # chain_full = MarkupText('{"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n"of": {"happiness": 2, "will": 1},\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}}', font_size=22)
        # self.play(FadeOut(arrow), chain_0.animate.become(chain_full.move_to(chain_0)).shift(UP*0.5))

        # phrase_und = MarkupText('"<u>the real</u> difference between <u>the test</u> of happiness\nand <u>the test</u> of will is simply that <u>the test</u> of\nhappiness is a test and <u>the other</u> isn\'t"', font_size=24)

        # chain_und_0 = MarkupText('<u>{"the": {"real": 1, "test": 3, "other": 1}</u>,\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n"of": {"happiness": 2, "will": 1},\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}}', font_size=22)
        # gen_0 = MarkupText('the . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)
        # chain_und_1 = MarkupText('{"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n<u>"test": {"of": 3, "and": 1}</u>,\n"of": {"happiness": 2, "will": 1},\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}}', font_size=22)
        # gen_1 = MarkupText('the test . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)
        # chain_und_2 = MarkupText('{"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n<u>"of": {"happiness": 2, "will": 1}</u>,\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}}', font_size=22)
        # gen_2 = MarkupText('the test of . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)
        # chain_und_3 = MarkupText('{"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n"of": {"happiness": 2, "will": 1},\n<u>"happiness": {"and": 1, "is": 1}</u>,\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}}', font_size=22)
        # gen_3 = MarkupText('the test of happiness . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)
        # chain_und_4 = MarkupText('{"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n"of": {"happiness": 2, "will": 1},\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n<u>"is": {"simply": 1, "a": 1}</u>,\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}}', font_size=22)
        # gen_4 = MarkupText('the test of happiness is . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)

        # self.next_slide()
        # self.play(phrase.animate.become(phrase_und.move_to(phrase)), chain_0.animate.become(chain_und_0.move_to(chain_0)))
        # self.next_slide()
        # self.play(Write(gen_0), phrase.animate.become(phrase_orig.move_to(phrase)))
        # self.next_slide()
        # self.play(TransformMatchingShapes(gen_0, gen_1), chain_0.animate.become(chain_und_1.move_to(chain_0)))
        # self.next_slide()
        # self.play(TransformMatchingShapes(gen_1, gen_2), chain_0.animate.become(chain_und_2.move_to(chain_0)))
        # self.next_slide()
        # self.play(TransformMatchingShapes(gen_2, gen_3), chain_0.animate.become(chain_und_3.move_to(chain_0)))
        # self.next_slide()
        # self.play(TransformMatchingShapes(gen_3, gen_4), chain_0.animate.become(chain_und_4.move_to(chain_0)))

        # self.next_slide()
        # self.play(map(FadeOut, [gen_4, chain_0, phrase]))
        # markov_bullets = ['• Published by Andrey Markov in 1906',
        #                   '• Developed to prove that the law of large numbers applied to dependent values',
        #                   '• Trained on the United States Reports (1754-2014)']
        # markov_bullets = VGroup(map(lambda x: Text(x, font_size=18), markov_bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        # self.play(Write(markov_bullets))
        # self.next_slide()
        # self.play(FadeOut(markov_bullets))
        # self.play(map(lambda x: x.animate.shift(RIGHT*5).shift(DOWN*7), [data_sources_title, 
        #                                                         ext_dat_text, 
        #                                                         ext_dat_box,
        #                                                         synth_dat_text,
        #                                                         synth_dat_box,
        #                                                         ext_line,
        #                                                         synth_line,
        #                                                         func,
        #                                                         markov_text,
        #                                                         markov_box,
        #                                                         markov_line,
        #                                                         random_text,
        #                                                         random_box,
        #                                                         random_line,
        #                                                         zeros_text,
        #                                                         zeros_box,
        #                                                         zeros_line]))
        # self.play(map(FadeOut, [func, 
        #                         markov_text, markov_box, markov_line,
        #                         random_text, random_box, random_line,
        #                         zeros_text, zeros_box, zeros_line]),
        #         map(lambda x: x.animate.set_opacity(1), [ext_line, ext_dat_text]))
        # self.play(map(FadeOut, [ext_dat_text, ext_dat_box, ext_line, synth_dat_text, synth_dat_box, synth_line]))
        # self.play(FadeOut(data_sources_title))

        clues_text = Text('What to ask the AI?', font_size=36).shift(UP*3.5)
        clues_box = draw_box(clues_text)

        self.play(Write(clues_text), Create(clues_box))

        retrieval = Text('• Simple Retrieval', font_size=24)
        formal = Text('• Formal Logic', font_size=24)
        informal = Text('• Informal Logic', font_size=24)

        types = VGroup([retrieval, formal, informal]).arrange(DOWN, aligned_edge=LEFT, buff=1)

        self.play(Write(types))
        self.next_slide()
        self.play(types.animate.shift(LEFT*4))
        clue_box = Rectangle(width=8.5, height=2.2, fill_color="#222222", fill_opacity=1, stroke_width=0).shift(RIGHT*2.3).shift(UP*1.5)
        qa_box = Rectangle(width=8.5, height=2.2, fill_color="#222222", fill_opacity=1, stroke_width=0).shift(RIGHT*2.3).shift(DOWN*1.5)
        self.play(formal.animate.set_opacity(0.3), informal.animate.set_opacity(0.3), Create(clue_box), Create(qa_box))

        retrieval_clue = Text('clue: "{x} met with {y} on {date}."', font_size=24).shift(RIGHT*2.5).shift(UP*1.5)
        retrieval_qa = Text('question: "When did {y} meet with {x}?"\nanswer:  "{y} met with {x} on {date}"', font_size=24).shift(RIGHT*2.5).shift(DOWN*1.5)
        formal_clue = Text('clues: "{x} and {y} do not both know of {topic}."\n        "{y} knows of {topic}."', font_size=24).shift(RIGHT*2.5).shift(UP*1.5)
        formal_qa = Text('question: "Does {x} know of {topic}?"\nanswer:  "no"', font_size=24).shift(RIGHT*2.5).shift(DOWN*1.5)
        informal_clue = Text('clues: "There is substantial evidence proving {topic}."\n        "{x} considers all available evidence when\n        making assessments."', font_size=24).shift(RIGHT*2.5).shift(UP*1.5)
        informal_qa = Text('question: "Does {x} believe {topic}?",\nanswer:  "Likely"', font_size=24).shift(RIGHT*2.5).shift(DOWN*1.5)

        self.play(Write(retrieval_clue), Write(retrieval_qa))
        self.next_slide()
        self.play(TransformMatchingShapes(retrieval_clue, formal_clue), 
                  TransformMatchingShapes(retrieval_qa, formal_qa), 
                  types[1].animate.set_opacity(1), types[0].animate.set_opacity(0.3))
        self.next_slide()
        self.play(TransformMatchingShapes(formal_clue, informal_clue), 
                  TransformMatchingShapes(formal_qa, informal_qa), 
                  types[2].animate.set_opacity(1), types[1].animate.set_opacity(0.3))
        
        names = MarkupText('"names": [\n        "Havelock Vetinari",\n        "Sam Vimes",\n        "Ziarenko Javid",\n        "Sheeana Brugh",\n        "Alef Burzmali",\n        "Ammel Brodrig",\n        "Glawen Curr",\n        "Preem Palver",\n        "Lewis Pirenne",\n        "Manuel Belgrano",\n        "Bernardo Velazco"\n        ...', font_size=22).shift(LEFT*5)
        # topics = MarkupText('"topics": \n"the confidential communication",\n"the spillover event",\n"the uncontrolled chain reactions",\n"the disfavorable documentation",\n"the boss\' temper",\n"the executive drama",\n"the mass layoffs",\n"the new allegations"\n...', font_size=18).shift(LEFT*3.5)

        self.next_slide()
        self.play(FadeOut(types))
        self.play(Write(names))

        informal_clue_filled = Text('clues: "There is substantial evidence proving the {topic}."\n        "Galwen Curr considers all available evidence when\n        making assessments."', font_size=24).shift(RIGHT*2.5).shift(UP*1.5)
        informal_qa_filled = Text('question: "Does Galwen Curr believe the {topic}?",\nanswer:  "Likely"', font_size=24).shift(RIGHT*2.5).shift(DOWN*1.5)

        self.next_slide()
        self.play(TransformMatchingShapes(informal_clue, informal_clue_filled), 
                  TransformMatchingShapes(informal_qa, informal_qa_filled))

        fileline_0 = Rectangle(width=0.5, height=6, fill_color='PURPLE_E', fill_opacity=1, stroke_width=0).shift(LEFT*4.3)
        fileline_1 = Rectangle(width=0.5, height=4, fill_color='BLUE_E', fill_opacity=1, stroke_width=0).shift(LEFT*5)

        self.next_slide()
        self.play(FadeOut(names))
        self.play(Create(fileline_0))
        line_0 = Line(start=LEFT*0.25, end=RIGHT*0.25, color=WHITE).shift(LEFT*4.3).shift(UP*2.3)
        line_0_arrow = Arrow(start=informal_clue_filled.get_left(), end=line_0.get_right(), color='WHITE')
        self.play(Create(line_0), Create(line_0_arrow))
        self.next_slide()

        self.play(Create(fileline_1))
        line_1 = Line(start=LEFT*0.25, end=RIGHT*0.25, color='WHITE').shift(LEFT*5).shift(DOWN*0.8)
        line_1_arrow = Arrow(start=informal_clue_filled.get_left(), end=line_1.get_right(), color='WHITE')
        self.play(Create(line_1), Create(line_1_arrow))
        self.next_slide()

        self.play(map(FadeOut, [line_0, line_0_arrow, 
                                line_1, line_1_arrow, 
                                fileline_0, fileline_1, 
                                clue_box, informal_clue_filled,
                                qa_box, informal_qa_filled]))

        def make_blob(n_points, center, color):
            base_radius = math.cbrt(n_points*0.01)
            angles = np.random.uniform(0, 2*np.pi, n_points)
            radii = np.sqrt(np.random.uniform(0, 1, n_points)) * base_radius
            x = center[0] + radii * np.cos(angles)
            y = center[1] + radii * np.sin(angles)

            label = Text(str(n_points), font_size=24).move_to([center[0], center[1] + base_radius+0.2, 1])
            # print(f"n={n_points}, base_radius={base_radius}, label_y={center[1] + base_radius + 0.2}")
            return VGroup(*[Dot(point=[xi, yi, 0], color=color, radius=0.03) for xi, yi in zip(x, y)], label)
    
        blob_10 = make_blob(10, (5, 2), 'GREEN_D')
        blob_25 = make_blob(25, (3.75, 1), 'GREEN_D')
        blob_50 = make_blob(50, (1.55, 1.5), 'GREEN_D')
        blob_100 = make_blob(100, (-0.7, 1), 'GREEN_D')
        blob_250 = make_blob(250, (-3.5, 1.9), 'GREEN_D')
        blob_500 = make_blob(500, (-5, -2), 'GREEN_D')
        label_500 = Text("500", font_size=24).move_to([-5, -2 + math.cbrt(5) + 0.2, 0])

        self.play(Create(blob_10))
        self.play(Create(blob_25))
        self.play(Create(blob_50))
        self.play(Create(blob_100))
        self.play(Create(blob_250))
        # self.play(Create(blob_500), Write(label_500))
        self.play(Create(blob_500))

        def make_orange(blobject):
            idxs = [random.randint(0, len(blobject)-2) for _ in range(6)]
            self.play(*[blobject[idx].animate.set_color(ORANGE) for idx in idxs], run_time=0.2)

        for blobject in [blob_10, blob_25, blob_50, blob_100, blob_250, blob_500]:
            make_orange(blobject)

        self.next_slide()
        self.play(*[FadeOut(VGroup(*blob[:-1])) for blob in [blob_10, blob_25, blob_50, blob_100, blob_250, blob_500]])
        
        labels = VGroup(*[blob[-1] for blob in [blob_10, blob_25, blob_50, blob_100, blob_250, blob_500]])
        self.play(labels.animate.arrange(DOWN, aligned_edge=LEFT).shift(LEFT*4))
        self.next_slide()
        grid = VGroup(*[labels.copy() for _ in range(5)])
        grid.arrange(RIGHT, buff=0.5)
        grid_box = draw_box(grid)
        grid.add(grid_box)  # add box to grid so it transforms with it
        grid.shift(DOWN*1)
        corp_names = VGroup(map(lambda x: Text(x, font_size=24), ["Enron", 
                                                              "Contracts", 
                                                              "Zeros", 
                                                              'Random', 
                                                              'Markov'])).arrange(DOWN, aligned_edge=RIGHT, buff=1)
        corp_names.rotate(-PI/2).next_to(grid, UP, buff=0.2)

        self.play(FadeOut(labels), *[FadeIn(grid[i]) for i in range(5)])
        self.play(FadeIn(corp_names))
        self.next_slide()

        three_grids = VGroup(*[grid.copy().scale(0.6) for _ in range(3)]).shift(UP*2)
        three_grids.arrange(RIGHT, buff=1)
        self.play(FadeOut(corp_names))
        self.play(Transform(grid, three_grids[0]), *[FadeIn(three_grids[i]) for i in range(1, 3)])

        
    
        


# class AnovaGraph(Slide):
#     def construct(self):
#         with open('data/corp_avg_dict.json', 'r') as infile:
#             data = json.load(infile)
#         colors = [BLUE, RED, GREEN, YELLOW, PURPLE]

#         plot_axes = Axes(
#             x_range=[1, 3, 1],
#             y_range=[0, 7, 1],
#             x_length=9
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