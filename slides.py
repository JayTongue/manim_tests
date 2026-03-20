from manim import *
from manim_slides import Slide
import json
import numpy as np
import math
import copy
import random
from itertools import combinations
import pandas as pd
import random

config.media_dir = "./presentation_vids"
# config.disable_caching = True
np.random.seed(42)

def draw_box(text, color=WHITE, buff=0.2):
    return SurroundingRectangle(text, color=color, buff=buff, fill_opacity=0)

class a_Intro(Slide):
    def construct(self):
        title = Text('Shortcuts the Long Way Around', font_size=56)
        title.shift(UP*1)
        
        bio = VGroup(map(lambda x: Text(x, font_size=24), ['Justin Tung',
                                                          'Reference Librarian & Lecturer',
                                                          'Univ. of Tex. School of Law']))
        bio.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        bio.next_to(title, DOWN, buff=1).shift(LEFT*3)

        self.next_slide()
        self.play(Write(title))
        self.next_slide()
        self.play(FadeIn(bio))
        self.next_slide()
        self.play(map(FadeOut, [title, bio]))



class b_Why(Slide):
    def construct(self):
        warning = Text('A warning to the math phobic...', font_size=36)
        self.play(Write(warning))
        self.next_slide()
        self.play(FadeOut(warning))
        text_1 = Text('I. What is this project\nand why does it matter?', font_size=36)
        text_1.move_to(ORIGIN)
        
        text_2 = Text('1. Vendor Claims', font_size=24)
        
        harvey_img = ImageMobject('exhibits/harvey_claims.png')
        harvey_img.scale(0.8)

        h_rect_1 = Rectangle(width=3.9, height=1, color=GREEN_D).set_z_index(1)
        h_rect_1.next_to(harvey_img, UP, buff=-1.5) ; h_rect_1.shift(LEFT*1.65)
        h_rect_2 = Rectangle(width=2.8, height=0.6, color=GREEN_D).set_z_index(1)
        h_rect_2.next_to(harvey_img, RIGHT, buff=-3.2) ; h_rect_2.shift(DOWN*1.8)

        lexis_img = ImageMobject('exhibits/lexis_claims.png')
        lexis_img.scale(0.8)
        l_rect_1 = Rectangle(width=2.7, height=0.8, color=GREEN_D).set_z_index(1)
        l_rect_1.next_to(lexis_img, RIGHT, buff=-3.5) ; l_rect_1.shift(DOWN*1.05)
        

        self.play(Write(text_1))
        self.next_slide()
        self.play(text_1.animate.shift(UP*2))
        self.play(Write(text_2))
        self.next_slide()
        self.play(text_2.animate.shift(UP*3.5), FadeOut(text_1))
        self.play(FadeIn(harvey_img))
        self.next_slide()
        self.play(FadeIn(h_rect_1))
        self.next_slide()
        self.play(FadeIn(h_rect_2))
        self.next_slide()
        self.play(map(FadeOut, [h_rect_1, h_rect_2, harvey_img]), FadeIn(lexis_img))
        self.next_slide()
        self.play(FadeIn(l_rect_1))
        self.next_slide()
        self.play(FadeOut(l_rect_1), FadeOut(lexis_img))

        text_3 = Text('2. Developing Use Guidelines', font_size=24)

        bullets = ['• Which tasks in my library or practice group can legal AI be used for?', 
                   '• What is the best way of using legal AI to perform those tasks?', 
                   '• What is the likely outcome of these use instances?', 
                   '• Do the upsides of this use outweigh the downsides?']
        bullets = VGroup(map(lambda x: Text(x, font_size=24), bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(text_2.animate.shift(DOWN*3.5), FadeIn(text_1.move_to(ORIGIN).shift(UP*2)))
        self.next_slide()
        self.play(Write(text_3.shift(DOWN*1)))
        self.next_slide()
        self.play(map(FadeOut, [text_1, text_2]), text_3.animate.shift(UP*4.5))

        for bullet in bullets:
            self.play(Write(bullet.shift(UP*1)))
            self.next_slide()


class c_Methodology(Slide, ThreeDScene):
    def construct(self):
        prod_title = Text('II. Methodology', font_size=36)
        prod_title = VGroup(prod_title, draw_box(prod_title))
        prods = Text('Products', font_size=36)
        prods = VGroup(prods, draw_box(prods))
        products = ['Harvey', 'Westlaw CoCounsel 2.0', 'Lexis+ with Protégé']
        products = VGroup(map(lambda x: Text(x, font_size=24), products)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(prod_title))
        self.next_slide()
        self.play(TransformMatchingShapes(prod_title, prods, transform_mismatches=True)) 
        self.play(prods.animate.shift(UP*3.5), Write(products))
        self.next_slide()
        self.play(map(FadeOut, [prods, products])),

        def make_graph_line(start, end, buff=0.5):
            return Line(start=start.get_edge_center(DOWN)+DOWN*buff, end=end.get_edge_center(UP)+UP*buff)

        data_sources_title = Text('Files for Upload', font_size=36)
        data_sources_title = VGroup(data_sources_title, draw_box(data_sources_title))
        ext_dat_text = Text('Existing Data', font_size=24).shift(LEFT*2)
        ext_dat_box = draw_box(ext_dat_text)
        # ext_dat_text = VGroup(ext_dat_text, draw_box(ext_dat_text))
        synth_dat_text = Text('Synthesized Data', font_size=24).shift(RIGHT*2)
        synth_dat_box = draw_box(synth_dat_text)
        # synth_dat_text = VGroup(synth_dat_text, draw_box(synth_dat_text))

        self.play(Write(data_sources_title))
        self.next_slide()
        self.play(data_sources_title.animate.shift(UP*3.5), 
                  Write(ext_dat_text), 
                  Create(ext_dat_box),
                  Write(synth_dat_text),
                  Create(synth_dat_box))

        ext_line = make_graph_line(data_sources_title, ext_dat_box)
        synth_line = make_graph_line(data_sources_title, synth_dat_box)

        self.play(Create(ext_line), Create(synth_line))
        self.next_slide()

        self.play(map(lambda x: x.animate.shift(UP*3.5).shift(RIGHT*2), [data_sources_title, 
                                                                         ext_dat_text, 
                                                                         ext_dat_box,
                                                                         synth_dat_text,
                                                                         synth_dat_box, 
                                                                         ext_line, 
                                                                         synth_line]))
        self.play(map(lambda y: y.animate.set_opacity(0.3), [synth_line, 
                                                             synth_dat_text]))

        enron_text = Text('Enron Email \nData Set V2', font_size=24).shift(LEFT*2)
        enron_box = draw_box(enron_text)
        # enron_text = VGroup(enron_text, draw_box(enron_text))
        contracts_text = Text('Material Contracts \nCorpus', font_size=24).shift(RIGHT*2)
        contracts_box = draw_box(contracts_text)
        # contracts_text = VGroup(contracts_text, draw_box(contracts_text))

        enron_line = make_graph_line(ext_dat_box, enron_box)
        contracts_line = make_graph_line(ext_dat_box, contracts_box)

        self.play(map(Write, [enron_text, contracts_text]))
        self.play(map(Create, [enron_line, contracts_line, enron_box, contracts_box]))
        self.next_slide()
        self.play(map(lambda x: x.animate.shift(UP*3.3).shift(RIGHT*2), [data_sources_title, 
                                                                     ext_dat_text, 
                                                                     ext_dat_box,
                                                                     synth_dat_text,
                                                                     synth_dat_box,
                                                                     ext_line,
                                                                     synth_line,
                                                                     enron_text,
                                                                     enron_box,
                                                                     contracts_text,
                                                                     contracts_box,
                                                                     enron_text,
                                                                     enron_line,
                                                                     contracts_line]))
        self.play(map(lambda y: y.animate.set_opacity(0.3), [contracts_text,  
                                                             contracts_line]), 
                                                             contracts_box.animate.set_fill(0))

        enron_bullets = ['• Dataset created for Enron litigation by the Federal Energy Regulatory Commission',
                         '• Underwent many curation steps over time',
                         '• Difficult to find in its full form',
                         '• Full(?) version available from the Internet Archive',
                         '• Total Size: 3,424,192 files; 258.9 GB']
        enron_bullets = VGroup(map(lambda x: MarkupText(x, font_size=18), enron_bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(enron_bullets))
        self.next_slide()
        self.play(FadeOut(enron_bullets))
        self.play(map(lambda x: x.animate.shift(LEFT*4), [data_sources_title, 
                                                                     ext_dat_text, 
                                                                     ext_dat_box,
                                                                     synth_dat_text,
                                                                     synth_dat_box,
                                                                     ext_line,
                                                                     synth_line,
                                                                     enron_text,
                                                                     enron_box,
                                                                     contracts_text,
                                                                     contracts_box,
                                                                     enron_line,
                                                                     contracts_line]))
        self.play(map(lambda x: x.animate.set_opacity(1), [contracts_line, 
                                                           contracts_text]), 
                                                           contracts_box.animate.set_fill(0), 
                map(lambda x: x.animate.set_opacity(0.3), [enron_line, enron_text]))

        contract_bullets = ['• Compiled by Peter Adelson and Prof Julian Nyarko in 2025', 
                             '• Contains commercial contracts and metadata from the SEC\'s EDGAR',
                             '• Coverage Date: 2000-2023',
                             '• Total Size: 1,038,766 files; 156.2 GB']
        contract_bullets = VGroup(map(lambda x: MarkupText(x, font_size=18), contract_bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(contract_bullets))
        self.next_slide()
        self.play(FadeOut(contract_bullets))
        self.play(map(lambda x: x.animate.set_opacity(1), [enron_line, 
                                                           enron_text]), 
                                                           enron_box.animate.set_fill(0))
        self.play(map(lambda x: x.animate.shift(RIGHT*2), [data_sources_title, 
                                                                     ext_dat_text, 
                                                                     ext_dat_box,
                                                                     synth_dat_text,
                                                                     synth_dat_box,
                                                                     ext_line,
                                                                     synth_line,
                                                                     enron_text,
                                                                     enron_box,
                                                                     contracts_text,
                                                                     contracts_box,
                                                                     enron_line,
                                                                     contracts_line]))
        
        def logify(bins):
            return np.log10(np.array(bins)+1).tolist()

        bins = json.load(open('data/file_sizes/bin_counts.json', 'r'))
        enron_lin_graph = BarChart(values=logify(bins['lin']['enron']),
                                y_range=[0, 8],
                                y_length=5,
                                x_length=7,
                                bar_colors=[PURPLE_D],
                                x_axis_config={'include_ticks': False}
                            )
        enron_lin_graph.y_axis.numbers.set_opacity(0)
        enron_lin_graph.scale(0.5).shift(LEFT*1.5)
        contracts_lin_graph = BarChart(values=logify(bins['lin']['contracts']),
                                y_range=[0, 8],
                                y_length=5,
                                x_length=7,
                                bar_colors=[BLUE_D],
                                x_axis_config={'include_ticks': False}
                            )
        contracts_lin_graph.y_axis.numbers.set_opacity(0)
        contracts_lin_graph.scale(0.5).shift(RIGHT*3)

        enron_log_graph = BarChart(values=logify(bins['log']['enron']),
                                y_range=[0, 8],
                                y_length=5,
                                x_length=7,
                                bar_colors=[PURPLE_D],
                                x_axis_config={'include_ticks': False}
                            )
        enron_log_graph.y_axis.numbers.set_opacity(0)
        enron_log_graph.scale(0.5).shift(LEFT*1.5)
        contracts_log_graph = BarChart(values=logify(bins['log']['contracts']),
                                y_range=[0, 8],
                                y_length=5,
                                x_length=7,
                                bar_colors=[BLUE_D],
                                x_axis_config={'include_ticks': False}
                            )
        contracts_log_graph.y_axis.numbers.set_opacity(0)
        contracts_log_graph.scale(0.5).shift(RIGHT*3)

        big_line = Line(LEFT*3, RIGHT*3).shift(DOWN*2.5)
        ticks = VGroup([Line(UP*0.1, DOWN*0.1).shift(LEFT*j).shift(DOWN*2.5)  for j in [i-3 for i in range(6,-1,-1)]])
        updated_tick_pos = [math.log(i, 10)*7.1-3 for i in range(1, 8)]

        lin_text = Text('Linear Scale', font_size=18).shift(DOWN*2)
        log_text = Text('Log Scale', font_size=18).shift(DOWN*2)
        log_norm_text = Text('Lognormal Distribution', font_size=24).shift(DOWN*3)

        self.play(GrowFromEdge(enron_lin_graph, DOWN), 
                  GrowFromEdge(contracts_lin_graph, DOWN),)
        self.next_slide()
        self.play(Write(lin_text), Create(big_line), Create(ticks))
        self.next_slide()
        self.play(TransformMatchingShapes(lin_text, log_text), 
                  map(lambda n: ticks[n].animate.move_to(np.array([updated_tick_pos[n], -2.5, 0])), 
                      [i for i in range(7)]))
        self.play(TransformMatchingShapes(enron_lin_graph, enron_log_graph), 
                  TransformMatchingShapes(contracts_lin_graph, contracts_log_graph))
        # enron_graph.change_bar_values(logify(bins['log']['enron']))
        # contracts_graph.change_bar_values(logify(bins['log']['contracts']))
        # self.play(GrowFromEdge(enron_log_graph, DOWN), GrowFromEdge(contracts_log_graph, DOWN))
        self.next_slide()
        self.play(Write(log_norm_text))

        log_normal_formula = MathTex(r"X", r"=", r"e^{", r"\mu", r"+", r"\sigma", r"Z", r"}")

        mu_label = Text("mean", font_size=18)
        sigma_label = Text("standard\ndeviation", font_size=18)
        z_label = Text("normal random\nvariable", font_size=18)

        # position labels
        mu_label.next_to(log_normal_formula.get_part_by_tex(r"\mu"), UP, buff=1)
        sigma_label.next_to(log_normal_formula.get_part_by_tex(r"\sigma"), DOWN*0.5, buff=1.5).shift(LEFT*0.5)
        z_label.next_to(log_normal_formula.get_part_by_tex("Z"), DOWN*0.5, buff=2).shift(RIGHT*1.5)

        # draw lines from formula to labels
        mu_line = Line(log_normal_formula.get_part_by_tex(r"\mu").get_top(), mu_label.get_bottom(), buff=0.2)
        sigma_line = Line(log_normal_formula.get_part_by_tex(r"\sigma").get_bottom(), sigma_label.get_top(), buff=0.2)
        z_line = Line(log_normal_formula.get_part_by_tex("Z").get_bottom(), z_label.get_top(), buff=0.2)

        enron_params = VGroup(
            MathTex(r"\mu = 9.0723", font_size=30),
            MathTex(r"\sigma = 1.8434", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP*1.8).shift(LEFT*3)

        contracts_params = VGroup(
            MathTex(r"\mu = 10.866", font_size=30),
            MathTex(r"\sigma = 1.4167", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP*1.8).shift(RIGHT*3)

        avg_params = VGroup(
            MathTex(r"\mu = 9.96915", font_size=30),
            MathTex(r"\sigma = 1.63005", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP*1.8)
        
        self.next_slide()
        self.play(map(FadeOut, [enron_log_graph, contracts_log_graph, log_text, ticks, big_line]))
        self.play(log_norm_text.animate.shift(UP*1.5), Write(log_normal_formula))
        self.next_slide()
        self.play(Create(mu_line), Write(mu_label), log_norm_text.animate.shift(DOWN*1))
        self.play(Create(sigma_line), Write(sigma_label))
        self.play(Create(z_line), Write(z_label))
        self.next_slide()
        self.play(map(FadeOut, [mu_line, mu_label, sigma_line, sigma_label, z_line, z_label]), 
                  Write(enron_params), Write(contracts_params), log_norm_text.animate.shift(UP*1))
        self.next_slide()
        self.play(enron_params.animate.shift(RIGHT*3), contracts_params.animate.shift(LEFT*3))
        self.play(TransformMatchingShapes(enron_params, avg_params, transform_mismatches=True), FadeOut(contracts_params))

        func = MathTex(r"X = e^{9.97 + 1.63 Z}")

        self.next_slide()
        self.play(TransformMatchingShapes(log_normal_formula, func, transform_mismatches=True), FadeOut(avg_params))
        self.next_slide()
        self.play(func.animate.shift(DOWN*1), FadeOut(log_norm_text))
        self.play(map(lambda x: x.animate.shift(LEFT*4).shift(DOWN*7), [data_sources_title, 
                                                                ext_dat_text, 
                                                                ext_dat_box,
                                                                synth_dat_text,
                                                                synth_dat_box,
                                                                ext_line,
                                                                synth_line,
                                                                enron_text,
                                                                enron_box,
                                                                contracts_text,
                                                                contracts_box,
                                                                enron_line,
                                                                contracts_line]))
        self.play(map(FadeOut, [enron_box, 
                              enron_line, 
                              enron_text, 
                              contracts_box, 
                              contracts_line, 
                              contracts_text])) 
        self.play(synth_dat_text.animate.set_opacity(1), 
                  synth_line.animate.set_opacity(1), 
                  ext_dat_text.animate.set_opacity(0.3), 
                  ext_line.animate.set_opacity(0.3))
        
        markov_text = Text('Markov Text', font_size=24).shift(RIGHT*3)
        markov_box = draw_box(markov_text)
        random_text = Text('Random Text', font_size=24)
        random_box = draw_box(random_text)
        zeros_text = Text('Zeros', font_size=24).shift(LEFT*3)
        zeros_box = draw_box(zeros_text)
        
        self.next_slide()
        self.play(func.animate.shift(UP*3.7),
                  map(lambda x: x.animate.shift(UP*3.5), [data_sources_title, 
                                                                ext_dat_text, 
                                                                ext_dat_box,
                                                                synth_dat_text,
                                                                synth_dat_box,
                                                                ext_line,
                                                                synth_line,
                                                                func]))
        
        self.play(map(Write, [markov_text, random_text, zeros_text]))
        markov_line = make_graph_line(func, markov_box)
        random_line = make_graph_line(func, random_box)
        zeros_line = make_graph_line(func, zeros_box)
        self.play(map(Create, [markov_box, markov_line,
                               random_box, random_line, 
                               zeros_box, zeros_line]))
        self.next_slide()
        self.play(map(lambda x: x.animate.shift(UP*3.5).shift(RIGHT*3), [data_sources_title, 
                                                                ext_dat_text, 
                                                                ext_dat_box,
                                                                synth_dat_text,
                                                                synth_dat_box,
                                                                ext_line,
                                                                synth_line,
                                                                func,
                                                                markov_text,
                                                                markov_box,
                                                                markov_line,
                                                                random_text,
                                                                random_box,
                                                                random_line,
                                                                zeros_text,
                                                                zeros_box,
                                                                zeros_line]))
        self.play(map(lambda x: x.animate.set_opacity(0.3), [random_text, random_line, markov_text, markov_line]))

        zeros_samp =  Text('00000000000\n00000000000\n00000000000\n00000000000', font_size=24)
        random_samp = Text('26c1e3ae1d4\n7faf7b4579b\n353ab30e6d8\nba0c6d9e6fa', font_size=24)

        self.next_slide()
        self.play(Write(zeros_samp))
        self.next_slide()
        self.play(map(lambda x: x.animate.shift(LEFT*3), [data_sources_title, 
                                                                ext_dat_text, 
                                                                ext_dat_box,
                                                                synth_dat_text,
                                                                synth_dat_box,
                                                                ext_line,
                                                                synth_line,
                                                                func,
                                                                markov_text,
                                                                markov_box,
                                                                markov_line,
                                                                random_text,
                                                                random_box,
                                                                random_line,
                                                                zeros_text,
                                                                zeros_box,
                                                                zeros_line,
                                                                zeros_samp]))
        self.play(Write(random_samp), 
                  map(lambda x: x.animate.set_opacity(0.3), [zeros_text, zeros_line]),
                  map(lambda x: x.animate.set_opacity(1), [random_text, random_line]))

        phrase = MarkupText('"the real difference between the test of happiness\nand the test of will is simply that the test of\nhappiness is a test and the other isn\'t"', font_size=24)
        phrase_orig = copy.deepcopy(phrase)

        arrow = CurvedArrow(start_point=phrase.get_top() + LEFT * 3 + UP*0.1,
                            end_point=phrase.get_top() + LEFT * 2.5 + UP*0.1,
                            angle=-PI/3,
                            tip_length=0.15)

        self.next_slide()
        self.play(map(FadeOut, [zeros_samp, random_samp]))
        self.play(map(lambda x: x.animate.set_opacity(0.3), [random_text, random_line]),
                  map(lambda x: x.animate.set_opacity(1), [markov_text, markov_line])) 
        self.play(map(lambda x: x.animate.shift(LEFT*3), [data_sources_title, 
                                                                ext_dat_text, 
                                                                ext_dat_box,
                                                                synth_dat_text,
                                                                synth_dat_box,
                                                                ext_line,
                                                                synth_line,
                                                                func,
                                                                markov_text,
                                                                markov_box,
                                                                markov_line,
                                                                random_text,
                                                                random_box,
                                                                random_line,
                                                                zeros_text,
                                                                zeros_box,
                                                                zeros_line]))
        self.next_slide()
        self.play(Write(phrase))
        self.next_slide()
        self.play(Create(arrow))
        self.next_slide()

        chain_0 = MarkupText('{\n"the": {"real": 1},\n}', font_size=24).shift(RIGHT*3)
        self.play(phrase.animate.shift(LEFT*3), arrow.animate.shift(LEFT*3), Write(chain_0))
        self.next_slide()
        chain_1 = MarkupText('{\n"the": {"real": 1},\n"real": {"difference": 1},\n}', font_size=24).shift(RIGHT*3)
        self.play(arrow.animate.shift(RIGHT*0.6))
        self.play(chain_0.animate.become(chain_1.move_to(chain_0)))
        self.next_slide()
        chain_2 = MarkupText('{\n"the": {"real": 1},\n"real": {"difference": 1},\n"difference": {"between": 1}\n}', font_size=24).shift(RIGHT*3)
        self.play(arrow.animate.shift(RIGHT*1.3))
        self.play(chain_0.animate.become(chain_2.move_to(chain_0)))
        chain_3 = MarkupText('{\n"the": {"real": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1}\n}', font_size=24).shift(RIGHT*3)
        self.play(arrow.animate.shift(RIGHT*1.4))
        self.play(chain_0.animate.become(chain_3.move_to(chain_0)))
        self.next_slide()
        chain_4 = MarkupText('{\n"the": {"real": 1, "test": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1}\n}', font_size=24).shift(RIGHT*3)
        self.play(arrow.animate.shift(RIGHT*0.6))
        self.play(chain_0.animate.become(chain_4.move_to(chain_0)))
        self.next_slide()
        chain_full = MarkupText('{\n"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n"of": {"happiness": 2, "will": 1},\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}\n}', font_size=22).shift(DOWN*-0.5)
        self.play(FadeOut(arrow), chain_0.animate.become(chain_full.move_to(chain_0)).shift(UP*-0.5))

        phrase_und = MarkupText('"<u>the real</u> difference between <u>the test</u> of happiness\nand <u>the test</u> of will is simply that <u>the test</u> of\nhappiness is a test and <u>the other</u> isn\'t"', font_size=24)

        chain_und_0 = MarkupText('<u>{\n"the": {"real": 1, "test": 3, "other": 1}</u>,\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n"of": {"happiness": 2, "will": 1},\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}\n}', font_size=22).shift(DOWN*-0.5)
        gen_0 = MarkupText('the . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)
        chain_und_1 = MarkupText('{\n"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n<u>"test": {"of": 3, "and": 1}</u>,\n"of": {"happiness": 2, "will": 1},\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}\n}', font_size=22).shift(DOWN*-0.5)
        gen_1 = MarkupText('the test . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)
        chain_und_2 = MarkupText('{\n"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n<u>"of": {"happiness": 2, "will": 1}</u>,\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}\n}', font_size=22).shift(DOWN*-0.5)
        gen_2 = MarkupText('the test of . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)
        chain_und_3 = MarkupText('{"\nthe": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n"of": {"happiness": 2, "will": 1},\n<u>"happiness": {"and": 1, "is": 1}</u>,\n"and": {"the": 2},\n"will": {"is": 1},\n"is": {"simply": 1, "a": 1},\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}\n}', font_size=22).shift(DOWN*-0.5)
        gen_3 = MarkupText('the test of happiness . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)
        chain_und_4 = MarkupText('{\n"the": {"real": 1, "test": 3, "other": 1},\n"real": {"difference": 1},\n"difference": {"between": 1},\n"between": {"the": 1},\n"test": {"of": 3, "and": 1},\n"of": {"happiness": 2, "will": 1},\n"happiness": {"and": 1, "is": 1},\n"and": {"the": 2},\n"will": {"is": 1},\n<u>"is": {"simply": 1, "a": 1}</u>,\n"simply": {"that": 1},\n"that": {"the": 1},\n"a": {"test": 1},\n"other": {"isn\'t": 1}\n}', font_size=22).shift(DOWN*-0.5)
        gen_4 = MarkupText('the test of happiness is . . .', font_size=18).shift(DOWN*2).shift(LEFT*4)

        self.next_slide()
        self.play(phrase.animate.become(phrase_und.move_to(phrase)), chain_0.animate.become(chain_und_0.move_to(chain_0)))
        self.next_slide()
        self.play(Write(gen_0), phrase.animate.become(phrase_orig.move_to(phrase)))
        self.next_slide()
        self.play(TransformMatchingShapes(gen_0, gen_1, transform_mismatches=True), chain_0.animate.become(chain_und_1.move_to(chain_0)))
        self.next_slide()
        self.play(TransformMatchingShapes(gen_1, gen_2, transform_mismatches=True), chain_0.animate.become(chain_und_2.move_to(chain_0)))
        self.next_slide()
        self.play(TransformMatchingShapes(gen_2, gen_3, transform_mismatches=True), chain_0.animate.become(chain_und_3.move_to(chain_0)))
        self.next_slide()
        self.play(TransformMatchingShapes(gen_3, gen_4, transform_mismatches=True), chain_0.animate.become(chain_und_4.move_to(chain_0)))

        self.next_slide()
        self.play(map(FadeOut, [gen_4, chain_0, phrase]))
        markov_bullets = ['• Published by Andrey Markov in 1906',
                          '• Developed to prove that the law of large numbers applied to dependent values',
                          '• Trained on the United States Reports (1754-2014)']
        markov_bullets = VGroup(map(lambda x: Text(x, font_size=18), markov_bullets)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        markov_sample = Text('...with the uses authorized under the statute , the rights , interests\n and rights of the parties to this proceeding the court would be put in \n jail and a $ 10 , 000 or  imprisoned not more than $ 5 , 000 miles to 2 , \n however , the language of the charter , without any corresponding advantage \n to the damage to settled principles , if an exchange is defined to include \n any charge for such freights . section 14 ( a ) took effect . but we think \n where the constitutionally forbidden comments , honest , and unequivocal \n possession of said land herein described...\n', font_size=18)
        markov_sample.next_to(markov_bullets, DOWN, buff=0.5)
        self.play(Write(markov_bullets))
        self.play(Write(markov_sample))
        self.next_slide()
        self.play(FadeOut(markov_bullets), FadeOut(markov_sample))
        self.play(map(lambda x: x.animate.shift(RIGHT*5).shift(DOWN*7), [data_sources_title, 
                                                                ext_dat_text, 
                                                                ext_dat_box,
                                                                synth_dat_text,
                                                                synth_dat_box,
                                                                ext_line,
                                                                synth_line,
                                                                func,
                                                                markov_text,
                                                                markov_box,
                                                                markov_line,
                                                                random_text,
                                                                random_box,
                                                                random_line,
                                                                zeros_text,
                                                                zeros_box,
                                                                zeros_line]))
        self.play(map(FadeOut, [func, 
                                markov_text, markov_box, markov_line,
                                random_text, random_box, random_line,
                                zeros_text, zeros_box, zeros_line]),
                map(lambda x: x.animate.set_opacity(1), [ext_line, ext_dat_text]))
        self.play(map(FadeOut, [ext_dat_text, ext_dat_box, ext_line, synth_dat_text, synth_dat_box, synth_line]))
        self.play(FadeOut(data_sources_title))

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
        self.play(TransformMatchingShapes(retrieval_clue, formal_clue, transform_mismatches=True), 
                  TransformMatchingShapes(retrieval_qa, formal_qa, transform_mismatches=True), 
                  types[1].animate.set_opacity(1), types[0].animate.set_opacity(0.3))
        self.next_slide()
        self.play(TransformMatchingShapes(formal_clue, informal_clue, transform_mismatches=True), 
                  TransformMatchingShapes(formal_qa, informal_qa, transform_mismatches=True), 
                  types[2].animate.set_opacity(1), types[1].animate.set_opacity(0.3))
        
        names = MarkupText('"names": [\n        "Havelock Vetinari",\n        "Sam Vimes",\n        "Ziarenko Javid",\n        "Sheeana Brugh",\n        "Alef Burzmali",\n        "Ammel Brodrig",\n        "Glawen Curr",\n        "Preem Palver",\n        "Lewis Pirenne",\n        "Manuel Belgrano",\n        "Bernardo Velazco"\n        ...', font_size=22).shift(LEFT*5)
        # topics = MarkupText('"topics": \n"the confidential communication",\n"the spillover event",\n"the uncontrolled chain reactions",\n"the disfavorable documentation",\n"the boss\' temper",\n"the executive drama",\n"the mass layoffs",\n"the new allegations"\n...', font_size=18).shift(LEFT*3.5)

        self.next_slide()
        self.play(FadeOut(types))
        self.play(Write(names))

        informal_clue_filled = Text('clues: "There is substantial evidence proving the {topic}."\n        "Galwen Curr considers all available evidence when\n        making assessments."', font_size=24).shift(RIGHT*2.5).shift(UP*1.5)
        informal_qa_filled = Text('question: "Does Galwen Curr believe the {topic}?",\nanswer:  "Likely"', font_size=24).shift(RIGHT*2.5).shift(DOWN*1.5)

        self.next_slide()
        self.play(TransformMatchingShapes(informal_clue, informal_clue_filled, transform_mismatches=True), 
                  TransformMatchingShapes(informal_qa, informal_qa_filled, transform_mismatches=True))

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
            return VGroup(*[Dot(point=[xi, yi, 0], color=color, radius=0.05) for xi, yi in zip(x, y)], label)
    
        blob_10 = make_blob(10, (5, 1), 'GREEN_D')
        blob_25 = make_blob(25, (3.75, -1), 'GREEN_D')
        blob_50 = make_blob(50, (1.55, 1), 'GREEN_D')
        blob_100 = make_blob(100, (-0.7, -2), 'GREEN_D')
        blob_250 = make_blob(250, (-3.5, 1.5), 'GREEN_D')
        blob_500 = make_blob(500, (-5, -2), 'GREEN_D')
        label_500 = Text("500", font_size=24).move_to([-5, -2 + math.cbrt(5) + 0.2, 0])

        uploaded = VGroup([Text(i, font_size=18) for i in ['2 x Simple Retrieval', '2 x Formal Logic', '2 x Informal Logic']])
        uploaded.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(DOWN*3).shift(RIGHT*3.75)
        self.play(Create(blob_10))
        self.play(Create(blob_25))
        self.play(Create(blob_50))
        self.play(Create(blob_100))
        self.play(Create(blob_250))
        # self.play(Create(blob_500), Write(label_500))
        self.play(Create(blob_500))
        self.play(Write(uploaded))

        def make_orange(blobject):
            idxs = [random.randint(0, len(blobject)-2) for _ in range(6)]
            self.play(*[blobject[idx].animate.set_color(ORANGE) for idx in idxs], run_time=0.2)

        for blobject in [blob_10, blob_25, blob_50, blob_100, blob_250, blob_500]:
            make_orange(blobject)

        self.next_slide()
        self.play(FadeOut(uploaded), *[FadeOut(VGroup(*blob[:-1])) for blob in [blob_10, 
                                                                                blob_25, 
                                                                                blob_50, 
                                                                                blob_100, 
                                                                                blob_250, 
                                                                                blob_500]])
        
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
                                                              'Markov'])).arrange(DOWN, aligned_edge=RIGHT, buff=0.7)
        corp_names.rotate(-PI/2).next_to(grid, UP, buff=0.2)

        self.play(*[TransformMatchingShapes(labels, grid[i]) for i in range(5)], Create(grid_box))
        self.play(FadeIn(corp_names))
        self.next_slide()

        three_grids = VGroup(*[grid.copy().scale(0.6) for _ in range(3)]).shift(UP*2)
        three_grids.arrange(RIGHT, buff=1)
        vend_labels = VGroup(*[Text(i, font_size=24) for i in ['Lexis', 'Westlaw', 'Harvey']]).arrange(LEFT, buff=2.6)
        vend_labels.next_to(three_grids, UP, buff=0.2).shift(LEFT*0.1)
        self.play(FadeOut(corp_names))
        self.play(Transform(grid, three_grids[0]), *[FadeIn(three_grids[i]) for i in range(1, 3)])
        self.play(FadeIn(vend_labels))
        self.next_slide()
        self.play(FadeOut(vend_labels))

        self.set_camera_orientation(phi=0*DEGREES)

        stack = VGroup(*[three_grids.copy().shift(IN * i * 1) for i in range(10)])
        
        # self.add(stack)
        self.play(FadeIn(stack), run_time=1)        
        self.move_camera(phi=-10*DEGREES, frame_center=UP*1, run_time=2)

        total_questions = Text('5,400 questions', font_size=24).shift(DOWN*2).shift(RIGHT*4)
        total_files = Text('140,250 files', font_size=24).shift(DOWN*2)
        total_vaults = Text('900 vaults', font_size=24).shift(DOWN*2).shift(LEFT*4)

        self.next_slide()
        self.play(Write(total_vaults))
        self.play(Write(total_files))
        self.play(Write(total_questions))
        self.next_slide()
        self.play(map(FadeOut, [three_grids, 
                                stack, 
                                clues_text, 
                                clues_box, 
                                total_questions, 
                                total_files, 
                                total_vaults,
                                grid,
                                grid_box]))


class d_Results(Slide):
    def construct(self):
        # tired_boss = ImageMobject('exhibits/tired_boss.png').shift(LEFT*3).scale(0.7)
        # boss_label = Text('The AI', font_size=24).next_to(tired_boss, UP)
        # tired_dad = ImageMobject('exhibits/tired_dad.png').shift(RIGHT*3)
        # dad_label = Text('Me', font_size=24).next_to(tired_dad, UP)

        # self.play(FadeIn(tired_dad), Write(dad_label))
        # self.next_slide()
        # self.play(FadeIn(tired_boss), Write(boss_label))
        # self.next_slide()
        # self.play(map(FadeOut, [tired_dad, tired_boss, dad_label, boss_label]))

        results_text = Text('III. Results', font_size=36)
        results_text = VGroup(results_text, draw_box(results_text))
        self.play(FadeIn(results_text))
        self.next_slide()
        self.play(FadeOut(results_text))

        lex_email = ImageMobject('exhibits/lex_email.png').scale(2)
        highlight_0 = Rectangle(height=0.3, width=4, fill_color=YELLOW, fill_opacity=0.2, stroke_width=0)
        highlight_0.next_to(lex_email, RIGHT).shift(DOWN*1.25).shift(LEFT*4.8)
        highlight_1 = Rectangle(height=0.3, width=3, fill_color=YELLOW, fill_opacity=0.2, stroke_width=0)
        highlight_1.next_to(lex_email, LEFT).shift(DOWN*1.6).shift(RIGHT*3.3)

        self.play(FadeIn(lex_email))
        self.next_slide()
        self.play(*[Create(i) for i in [highlight_0, highlight_1]])

        self.next_slide()
        self.play(map(FadeOut, [lex_email, highlight_0, highlight_1]))


class e_AnovaGraph(Slide):
    def construct(self):
        def make_blob(n_points, center, color):
            base_radius = math.cbrt(n_points*0.15)
            angles = np.random.uniform(0, 2*np.pi, n_points)
            radii = np.sqrt(np.random.uniform(0, 1, n_points)) * base_radius
            x = center[0] + radii * np.cos(angles)
            y = center[1] + radii * np.sin(angles)
            return VGroup(*[Dot(point=[xi, yi, 0], color=color, radius=0.05) for xi, yi in zip(x, y)])


        q_1 = Text('Question 1:\nDoes Corpus Affect Performance?', font_size=36)

        anova_name = Text('Analysis Of Variance', font_size=24).shift(UP*3)
        anova_abr = Text('ANOVA', font_size=24).shift(UP*3)
        anova_full = MathTex(r'F = \frac{\sum_{j} n_j (\bar{X}_j - \bar{X})^2 / (k-1)}{\sum_{j}\sum_{i} (X_{ij} - \bar{X}_j)^2 / (N-k)}')
        anova_simple = MathTex(r"F = \frac{Variance\ Between\ Groups}{Variance\ Within\ Groups}")



        tukey_name = Text('Tukey-Kramer Pairwise Test', font_size=24).shift(LEFT*1).shift(UP*0.5)
        tukey_abr = Text('Tukey-Kramer', font_size=24).shift(UP*0.5).shift(LEFT*1)
        tukey_full = MathTex(r"q = \frac{\bar{X}_i - \bar{X}_j}{\sqrt{\frac{MS_{within}}{2}\left(\frac{1}{n_i} + \frac{1}{n_j}\right)}}").shift(LEFT*1.5).shift(DOWN*1)
        tukey_simple = Text('Is group 1 different from group 2?', font_size=24).shift(DOWN*1).shift(LEFT*0.7)

        blob_1 = make_blob(25, [-3, 1, 0], PURPLE_C)
        blob_2 = make_blob(25, [-0.5, 0.5, 0], RED_C)
        blob_3 = make_blob(25, [-2.5, -1, 0], GOLD_C)

        self.play(Write(q_1))
        self.next_slide()
        self.play(FadeOut(q_1))
        self.play(Write(anova_name))
        self.play(TransformMatchingShapes(anova_name, anova_abr, transform_mismatches=True))
        self.next_slide()
        self.play(Write(anova_full))
        self.play(TransformMatchingShapes(anova_full, anova_simple, transform_mismatches=True))
        self.next_slide()
        self.play(anova_simple.animate.scale(0.5).shift(RIGHT*3).shift(UP*2.3), anova_abr.animate.shift(RIGHT*3))
        self.play(Write(tukey_name), Write(tukey_full))
        self.play(TransformMatchingShapes(tukey_full, tukey_simple, transform_mismatches=True))
        self.next_slide()
        self.play(TransformMatchingShapes(tukey_name, tukey_abr, transform_mismatches=True))
        self.play(tukey_abr.animate.shift(RIGHT*4.1), tukey_simple.animate.scale(0.7).shift(RIGHT*4).shift(UP*0.7))
        self.next_slide()
        self.play(Create(blob_1), Create(blob_2), Create(blob_3))
        self.next_slide()
        self.play(blob_1.animate.shift(DOWN*1).shift(RIGHT*1), blob_2.animate.shift(LEFT*1), blob_3.animate.shift(UP*1).shift(RIGHT*0.5))
        self.next_slide()
        self.play(blob_1.animate.move_to([-4, 1.5, 0]), blob_2.animate.move_to([-1, 1, 0]), blob_3.animate.move_to([-3, -2, 0]))
        self.next_slide()
        self.play(blob_2.animate.move_to([-3.5, 1, 0]))
        self.play(blob_2.animate.move_to([-1, 1, 0]))
        self.play(blob_3.animate.move_to([-4, 1, 0]))
        self.play(blob_3.animate.move_to([-3, -2, 0]))
        self.next_slide()
        self.play(map(FadeOut, [anova_abr, anova_simple, tukey_abr, tukey_simple, blob_1, blob_2, blob_3]))

        corps = ['Markov', 'Enron', 'Zeros', 'Random', 'Contracts']
        n = len(corps)
        radius = 2

        dots = VGroup()
        labels = VGroup()
        for i, corp in enumerate(corps):
            angle = (2 * PI * i) / n
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            dot = Dot([x, y, 0], color=BLUE)
            label = Text(corp, font_size=24).next_to(dot, np.array([np.cos(angle), np.sin(angle), 0]), buff=0.2)
            dots.add(dot)
            labels.add(label)

        self.play(Create(dots), Write(labels))
        pentagram = []
        for pair in combinations([i for i in range(5)], 2):
            if set(pair) in [{1, 0}, {3, 2}]:
                pentagram.append(Line(start=dots[pair[0]], end=dots[pair[1]], color=RED))
            else:
                pentagram.append(DashedLine(start=dots[pair[0]], end=dots[pair[1]], color='#222222'))
        self.play(*map(Create, pentagram))
        self.next_slide()
        self.play(*map(FadeOut, pentagram + [dots, labels]))

        with open('data/corp_avg_dict.json', 'r') as infile:
            data = json.load(infile)
        percent_data = {}
        for corp in data:
            corp_dict = {}
            for size in data[corp]:
                corp_dict[size] = 100*data[corp][size]/6
            percent_data[corp] = corp_dict
        colors = [BLUE, PURPLE, GREEN, RED, YELLOW]

        plot_axes = Axes(
            x_range=[1, 3, 1],
            y_range=[0, 100, 10],
            x_length=9,
            y_length=5.5,
            axis_config={"font_size": 24},
            x_axis_config={
                "scaling": LogBase(base=10),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 100, 10),
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
        for (label, points), color in zip(percent_data.items(), colors):
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
        for (label, _), color in zip(percent_data.items(), colors):
            dot = Dot(color=color, radius=0.1)
            text = Text(label, font_size=20, color=color)
            text.next_to(dot, RIGHT, buff=0.15)
            item = VGroup(dot, text)
            legend_items.add(item)

        legend_items.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend_box = SurroundingRectangle(legend_items, color=WHITE, buff=0.2)
        legend = VGroup(legend_box, legend_items)
        legend.to_corner(UR, buff=0.5)

        self.play(Write(title))
        self.play(Create(plot_axes), Create(plot_labels), Create(tick_labels), run_time=3)
        self.next_slide()
        self.play(Create(legend), Create(lines), run_time=10)
        self.wait()



class f_Regression(Slide):

    def construct(self):
        q2 = Text('Question 2:\nDoes Number of Files Impact Performance?', font_size=36)
        self.play(Write(q2))
        self.next_slide()
        self.play(FadeOut(q2))
        
        with open('data/fit_stats.json', 'r') as f:
            data = json.load(f)
        stats_dict = data['stats_dict']
        weighted_fit = data['weighted_fit']

        corp_colors = [BLUE, RED, GREEN, YELLOW, PURPLE]
        vendors = list(stats_dict.keys())

        # exp_decay = MathTex(r"f(x) = ae^{-bx} + c")

        self._fitting()

        plot_axes = Axes(
            x_range=[1, 3, 1],
            y_range=[0, 100, 10],
            x_length=9,
            y_length=5.5,
            axis_config={"font_size": 24},
            x_axis_config={"scaling": LogBase(base=10)},
            y_axis_config={"numbers_to_include": np.arange(0, 101, 10)},
            tips=False,
        )
        custom_ticks = [10, 25, 50, 100, 250, 500]
        tick_labels = VGroup(*[
            MathTex(str(v), font_size=20).next_to(plot_axes.c2p(v, 0), DOWN, buff=0.2)
            for v in custom_ticks
        ])
        y_label = plot_axes.get_y_axis_label("\%\ Correct", edge=LEFT, direction=LEFT)
        y_label.rotate(PI/2).shift(LEFT * 0.5)
        x_label = plot_axes.get_x_axis_label("Number\ of\ Files", edge=DOWN)
        x_label.shift(DOWN * 0.9).shift(LEFT * 2)
        plot_labels = VGroup(x_label, y_label)


        self.play(Create(plot_axes), Create(plot_labels), Create(tick_labels))

        for vendor in vendors:
            self._make_vendor_slide(vendor, stats_dict[vendor], weighted_fit.get(vendor), corp_colors, plot_axes)
        self.play(*[FadeOut(i) for i in [plot_axes, plot_labels, tick_labels]])

    def _fitting(self):
        fitting_title = Text('Regression Analysis?', font_size=36)
        self.play(Write(fitting_title))
        self.next_slide()
        self.play(fitting_title.animate.shift(UP*3.5))
        linx = [i/364 for i in range(0, 365)]
        liny = [i/364 for i in range(0, 365)]
        lin_title = Text('Widget Factory', font_size=30)
        lin_eq = MathTex(r"f(x) = mx + b").shift(LEFT*2) 
        lin_y_lab = Text('# of Widgets', font_size = 20).rotate(90 * DEGREES)
        lin_x_lab = Text('Time', font_size = 20)

        a = 0.0241 ; b = 3.6706

        scap = 0 ; ecap = 223
        expx = [i / ecap for i in range(scap, ecap)]
        expy = [a * np.exp(b * i/ecap) for i in range(scap, ecap)]
        exp_title = Text('Widget Factory Factory', font_size=30)
        exp_eq = MathTex(r"g(x) = a^x+b").shift(LEFT*2)

        with open('data/population.filtered/population.csv', 'r') as infile:
            pop_df = pd.read_csv(infile)
        popx = pop_df['Year'].to_list()
        popx = [(i-1800)/(max(popx)-1800) for i in popx]
        popy = pop_df['Population'].to_list()
        popy = [i/max(popy) for i in popy]
        pop_title = Text('Cambodia\'s Population since 1800', font_size=36)
        pop_eq = MathTex(r"P = P_0 e^{kt}").shift(LEFT*2)
        pop_y_lab = Text('# of People', font_size = 20).rotate(90 * DEGREES)

        plot_axes = Axes(
            x_range=[0, 1, 0.25],
            y_range=[0, 1, 0.25],
            x_length=8,
            y_length=5,
            axis_config={"font_size": 24},
            tips=False,
        ).shift(DOWN*1)

        lin_graph = plot_axes.plot_line_graph(x_values=linx, 
                                          y_values=liny, 
                                          line_color=BLUE,
                                          add_vertex_dots=False)
        lin_title.next_to(lin_graph, UP, buff=0.2)
        lin_x_lab.next_to(lin_graph, DOWN, buff=0.2)
        lin_y_lab.next_to(lin_graph, LEFT, buff=0.2)
        exp_graph = plot_axes.plot_line_graph(x_values=expx, 
                                          y_values=expy, 
                                          line_color=BLUE, 
                                          add_vertex_dots=False)
        exp_title.next_to(exp_graph, UP, buff=0.2)
        lin_x_lab.next_to(lin_graph, DOWN, buff=0.2).rotate
        lin_y_lab.next_to(lin_graph, LEFT, buff=0.2)
        pop_graph = plot_axes.plot_line_graph(x_values=popx, 
                                          y_values=popy, 
                                          line_color=GREEN, 
                                          add_vertex_dots=False)
        pop_title.next_to(pop_graph, UP, buff=0.2)
        pop_y_lab.next_to(lin_graph, LEFT, buff=0.2)
        lin_x_lab.next_to(lin_graph, DOWN, buff=0.2)

        self.play(Create(lin_graph), Create(plot_axes), Write(lin_title), Write(lin_x_lab), Write(lin_y_lab))
        self.next_slide()
        self.play(Write(lin_eq))
        self.next_slide()    
        self.play(TransformMatchingShapes(lin_title, exp_title, transform_mismatches=True))
        self.play(TransformMatchingShapes(lin_eq, exp_eq, transform_mismatches=True))
        self.play(TransformMatchingShapes(lin_graph, exp_graph, transform_mismatches=True))
        self.next_slide()
        self.play(TransformMatchingShapes(exp_title, pop_title, transform_mismatches=True))
        self.play(TransformMatchingShapes(exp_eq, pop_eq, transform_mismatches=True))
        self.play(FadeIn(pop_graph), TransformMatchingShapes(lin_y_lab, pop_y_lab, transform_mismatches=True))
        self.next_slide()
        self.play(map(FadeOut, [pop_graph,
                                pop_eq, 
                                pop_title, 
                                fitting_title, 
                                exp_graph,
                                pop_y_lab,
                                lin_x_lab, 
                                plot_axes]))


    def _make_vendor_slide(self, vendor, vendor_dict, fit, corp_colors, plot_axes):
        title = Title(f'{vendor} — Mean by Corpus', include_underline=False, font_size=36)
        lines = VGroup()
        legend_items = VGroup()
        for (corp, d), color in zip(vendor_dict.items(), corp_colors):
            xs = [int(k) for k in d.keys()]
            ys = [(d[k]['mean'] / 6) * 100 for k in d.keys()]
            line = plot_axes.plot_line_graph(
                x_values=xs,
                y_values=ys,
                line_color=color,
                add_vertex_dots=True,
                vertex_dot_radius=0.05,
            )
            lines.add(line)

            dot = Dot(color=color, radius=0.08)
            text = Text(corp, font_size=18, color=color).next_to(dot, RIGHT, buff=0.15)
            legend_items.add(VGroup(dot, text))

        legend_items.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend_box = SurroundingRectangle(legend_items, color=WHITE, buff=0.2, fill_opacity=0)
        legend = VGroup(legend_box, legend_items).to_corner(UR, buff=0.5)

        # exponential decay fit
        fit_line = None
        r2_label = None
        if fit:
            a, b, c, r2 = float(fit['a']), float(fit['b']), float(fit['c']), float(fit['R2'])
            # scale fit to percent
            a_pct = a * (100 / 6)
            c_pct = c * (100 / 6)
            xs_fit = list(range(10, 501, 10))
            ys_fit = [float(np.clip(a_pct * np.exp(-b * x) + c_pct, 0, 100)) for x in xs_fit]
            fit_curve = plot_axes.plot_line_graph(
                x_values=xs_fit,
                y_values=ys_fit,
                line_color=WHITE,
                add_vertex_dots=False,
                stroke_width=3,
            )
            fit_line = DashedVMobject(fit_curve["line_graph"], num_dashes=30)
            r2_label = MathTex(rf"R^2 = {r2:.3f}", font_size=24).to_corner(DL, buff=0.5)

        # animate
        self.play(Write(title))
        # self.play(Create(plot_axes), Create(plot_labels), Create(tick_labels), run_time=3)
        self.play(Create(lines), Create(legend), run_time=3)
        self.next_slide()
        if fit_line:
            self.play(lines.animate.set_stroke(opacity=0.5), run_time=1)
            self.play(Create(fit_line), Write(r2_label), run_time=3,)
            self.next_slide()

        # fade out for next vendor
        # to_fade = VGroup(title, plot_axes, plot_labels, tick_labels, lines, legend)
        to_fade = VGroup(title, lines, legend)
        if fit_line:
            to_fade.add(fit_line, r2_label)
        self.play(FadeOut(to_fade))



class g_Conclusion(Slide, ThreeDScene):
    def construct(self):
        self._further()

        conc = Text(' V. Conclusions', font_size=36)
        conc = VGroup(conc, draw_box(conc))
        q1 = Text('1. Does Corpus Affect Performance?', font_size=24).shift(UP*1).shift(LEFT*2.5)
        a1 = Text('Yes', font_size=24).shift(UP*0.5).shift(RIGHT*2)
        q2 = Text('2. Does Number of Files Impact\nPerformance?', font_size=24).shift(DOWN*1).shift(LEFT*2.5)
        a2 = Text('Yes regarding Lexis\nand Westlaw, no regarding\nHarvey', font_size=24).shift(DOWN*2.5).shift(RIGHT*2)

        self.play(FadeIn(conc))
        self.next_slide()
        self.play(FadeOut(conc), Write(q1))
        self.next_slide()
        self.play(Write(a1))
        self.next_slide()
        self.play(Write(q2))
        self.next_slide()
        self.play(Write(a2))

        questions = Text('Thank you!\nQuestions?', font_size=24)
        self.next_slide()
        self.play(map(FadeOut, [q1, q2, a1, a2]), Write(questions))

    def _further(self):
        discussion_title = VGroup(Text('IV. Discussion', font_size=36))
        discussion_title += draw_box(discussion_title)
        self.play(Write(discussion_title[0]), Create(discussion_title[1]))
        self.play(discussion_title.animate.shift(UP*3.5).shift(LEFT*2))
        parallelization = Text('1. Parallelization', font_size=24)
        self.play(Write(parallelization.next_to(discussion_title, RIGHT)))
        serial = VGroup(map(lambda x: Text(x, font_size=20), ['• Fixed compute requirement', 
        '• Low overhead', 
        '• High task complexity',
        '• Necessary for dependant conditions',
        '• Time scales with inputs'])).arrange(DOWN, aligned_edge=LEFT).shift(LEFT*2).shift(UP*1.2)
        parallel = VGroup(map(lambda x: Text(x, font_size=20), ['• Flexible compute requirement', 
        '• High overhead', 
        '• Low task complexity',
        '• Good for independant cases',
        '• Constant(ish) time'])).arrange(DOWN, aligned_edge=LEFT).shift(LEFT*3).shift(UP*1)
        dots = VGroup(*[Dot([-3, 2-(0.7*i), 0], radius=0.2, fill_opacity=1, color=GREEN) for i in range(8)])
        comp = Rectangle(height=0.5, width=0.5, fill_opacity=1, color=ORANGE).shift(DOWN*0.45).shift(RIGHT*0.21)
        self.play(Create(dots))
        self.play(Create(comp))
        self.play(dots.animate.rotate(90*DEGREES))
        self.play(Write(serial))
        for i in range(9):
            self.play(dots.animate.shift(RIGHT*0.7))
        self.next_slide()
        self.play(dots.animate.rotate(-90*DEGREES))
        self.play(FadeOut(serial))
        self.play(dots.animate.shift(LEFT*5.6))
        comps = VGroup([Rectangle(height=0.5, width=0.5, fill_opacity=1, color=ORANGE).move_to([1, 2-(0.7*i),0]) for i in range(8)])
        self.play(TransformMatchingShapes(comp, comps)) 
        self.play(dots.animate.shift(RIGHT*6), run_time=5)
        self.play(Write(parallel))
        self.next_slide()
        self.play(map(FadeOut, [dots, comps, parallel]))

        non_lin = Text('2. Non-linear Retrieval', font_size=24).next_to(discussion_title, RIGHT)
        self.play(TransformMatchingShapes(parallelization, non_lin, transform_mismatches=True))
        problem = VGroup(*[Text(i, font_size=18) for i in ['Clues:',
                                                           '{x} and {y} do not both know of {topic}', 
                                                           '{y} knows of {topic}']])
        problem.arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(UP*1)
        question = Text('Q: does {x} know of {topic}?', font_size=18).next_to(problem, LEFT, buff=1)

        colors = [BLUE, GREEN, YELLOW, RED, PURPLE, WHITE, GRAY]
        docs = VGroup()
        for i in range(4):
            for j in range(4):
                doc = Rectangle(height=0.3, width=0.3, fill_opacity=0, color=random.choice(colors))
                docs.add(doc.shift(RIGHT*i*0.5).shift(DOWN*j*0.5))

        self.play(Write(problem))
        self.play(Write(question))
        self.next_slide()
        self.play(Create(docs.shift(DOWN*1)))

        arrow_1 = CurvedArrow(start_point=question.get_bottom()+DOWN*0.2,
                            end_point=docs.get_left()+LEFT*0.2,
                            # angle=-PI/3,
                            tip_length=0.5)
        x_lab = Text('{x}', font_size=24).next_to(arrow_1, DOWN, buff=0.1)
        
        arrow_2 = Arrow(start=docs.get_top(),
                            end=problem.get_bottom(),
                            tip_length=0.5)
        arrow_3 = Arrow(end=docs.get_top(),
                            start=problem.get_bottom(),
                            tip_length=0.5).next_to(arrow_2, LEFT, buff=0.02)
        y_lab = Text('{x}, {y}', font_size=24).next_to(arrow_2, RIGHT, buff=0.2)
        
        ans = Text('No', font_size=24).shift(RIGHT*4).shift(DOWN*2)

        arrow_4 = CurvedArrow(start_point=problem.get_right()+RIGHT*0.2,
                            end_point=ans.get_top()+UP*0.2,
                            angle=-PI/3,
                            tip_length=0.5)

        self.play(Create(arrow_1))
        self.play(Write(x_lab))
        self.next_slide()
        self.play(Create(arrow_2), Create(arrow_3), Write(y_lab))
        self.play(problem[2].animate.set_opacity(0.3))
        self.next_slide()
        self.play(Create(ans), Create(arrow_4))
        self.next_slide()
        self.play(map(FadeOut, [problem, 
                                question, 
                                docs, 
                                arrow_1, 
                                arrow_2, 
                                x_lab, 
                                y_lab, 
                                ans, 
                                arrow_3, 
                                arrow_4,
                                discussion_title,
                                non_lin]))

        

        




