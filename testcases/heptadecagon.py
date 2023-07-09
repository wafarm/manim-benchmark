#!/usr/bin/env python3

from manim import *
from ManimExtras import *

class Heptadecagon(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        base_circle = Circle(3)
        base_line = Line(12 * LEFT, 12 * RIGHT, color=BLUE_D)
        dot_A = Dot(RIGHT * 3)
        dot_B = Dot(LEFT * 3)
        dot_O = Dot()
        dot_3 = Dot(UP * 3)
        dot_C = Dot(UP * 1.5)
        dot_D = Dot(UP * 0.75)

        self.play(Create(base_line))
        self.play(Create(base_circle))
        self.play(Create(dot_A), Create(dot_B))
        self.wait()
        self.play(self.camera.frame.animate.scale(1.5))
        
        circle_1 = CircleCreationWithLine(self, dot_A, dot_B, color=WHITE)
        circle_2 = CircleCreationWithLine(self, dot_B, dot_A, color=WHITE)

        l1 = Line(UP * 5.19615, DOWN * 5.19615, color=BLUE_D)
        self.play(Create(l1))
        self.play(FadeOut(circle_1), FadeOut(circle_2))
        self.play(Restore(self.camera.frame))

        self.play(Create(dot_O), Create(dot_3))
        circle_3 = CircleCreationWithLine(self, dot_3, dot_O, color=WHITE)

        l2 = Line(np.array((-2.59808, 1.5, 0)), np.array((2.59808, 1.5, 0)))
        self.play(Create(l2))
        self.play(Create(dot_C))
        self.play(FadeOut(circle_3), FadeOut(l2), FadeOut(dot_3))

        circle_4 = CircleCreationWithLine(self, dot_C, dot_O, color=WHITE)
        circle_5 = CircleCreationWithLine(self, dot_O, dot_C, color=WHITE)
        l3 = Line(np.array((-1.29904, 0.75, 0)), np.array((1.29904, 0.75, 0)))
        self.play(Create(l3))
        self.play(Create(dot_D))
        self.play(FadeOut(circle_4), FadeOut(circle_5), FadeOut(dot_C), FadeOut(l3), FadeOut(dot_O))

        l4 = Line(UP * 0.75, RIGHT * 3, color=BLUE_D)
        self.play(Create(l4))

        dot_F = Dot(np.array((1.70024, 0.32494, 0)))
        self.play(Create(dot_F))
        arc_1 = ArcCreationWithLine(self, dot_D, dot_F, deg(-75.96376))
        dot_E = Dot(DOWN * 1.00257)

        self.play(Create(dot_E))
        c6 = CircleCreationWithLine(self, dot_E, dot_F, color=WHITE)
        c7 = CircleCreationWithLine(self, dot_F, dot_E, color=WHITE)
        l5 = Line(dot_D.arc_center, np.array((1.99978, -1.81127, 0)))

        self.play(Create(l5))
        self.play(FadeOut(c6), FadeOut(c7))
        dot_H = Dot(np.array((1.07855, -0.63139, 0)))
        self.play(Create(dot_H))

        c8 = CircleCreationWithLine(self, dot_H, dot_E, color=WHITE)
        c9 = CircleCreationWithLine(self, dot_E, dot_H, color=WHITE)
        l6 = Line(np.array((0.86073, -1.75103, 0)), dot_D.arc_center, color=BLUE_D)
        l6_1 = Line(np.array((0.86073, -1.75103, 0)), np.array((-0.64126, 2.61333, 0)), color=BLUE_D)
        self.play(Create(l6))
        self.play(FadeOut(c8), FadeOut(c9), FadeOut(l5), FadeOut(dot_H), FadeOut(dot_E), FadeOut(dot_F))
        self.play(Transform(l6, l6_1))
        arc_1_1 = ArcCreationWithLine(self, dot_D, dot_E, deg(-161.00906))
        dot_L = Dot(np.array((0.57032, -0.90718, 0)))
        dot_K = Dot(np.array((-0.57032, 2.40718, 0)))

        self.play(Create(dot_L), Create(dot_K))
        arc2 = ArcCreationWithLine(self, dot_L, dot_K, deg(70), color=WHITE)
        arc3 = ArcCreationWithLine(self, dot_K, dot_L, deg(-70), color=WHITE)
        l7 = Line(dot_D.arc_center, np.array((-2.87032, -0.23782, 0)))
        self.play(Create(l7))
        self.play(FadeOut(arc2), FadeOut(arc3), FadeOut(dot_K))

        dot_N = Dot(np.array((-1.65718, 0.17968, 0)))
        self.play(Create(dot_N))
        c10 = CircleCreationWithLine(self, dot_N, dot_L, color=WHITE)
        c11 = CircleCreationWithLine(self, dot_L, dot_N, color=WHITE)
        l8 = Line(dot_D.arc_center, np.array((-1.48468, -2.29282, 0)), color=BLUE_D)
        self.play(Create(l8))
        self.play(FadeOut(c10), FadeOut(c11), FadeOut(dot_N), FadeOut(l7), FadeOut(dot_L), FadeOut(arc_1), FadeOut(arc_1_1))

        dot_Q = Dot(LEFT * 0.36595)
        dot_V = Dot(RIGHT * 0.25811)
        self.play(Create(dot_Q), Create(dot_V))
        self.play(FadeOut(dot_D), FadeOut(l8), FadeOut(l4), FadeOut(l6))
        c12 = CircleCreationWithLine(self, dot_A, dot_Q, color=WHITE)
        c13 = CircleCreationWithLine(self, dot_Q, dot_A, color=WHITE)
        l9 = Line(np.array((1.31703, 2.91499, 0)), np.array((1.31703, -2.91499, 0)))
        self.play(Create(l9))
        dot_T = Dot(RIGHT * 1.31703)
        self.play(Create(dot_T))
        self.play(FadeOut(c12), FadeOut(c13), FadeOut(l9))

        arc4 = ArcCreationWithLine(self, dot_T, dot_Q, deg(-38.50466))
        dot_U = Dot(UP * 1.04778)
        self.play(Create(dot_U))
        self.play(FadeOut(arc4), FadeOut(dot_T), FadeOut(dot_Q))

        arc5 = ArcCreationWithLine(self, dot_V, dot_U, deg(-103.83888))
        dot_W = Dot(RIGHT * 1.33722)
        self.play(Create(dot_W))
        self.play(FadeOut(arc5), FadeOut(dot_U), FadeOut(dot_V), FadeOut(l1))
        
        dot_Z = Dot(RIGHT * 0.03278)
        self.play(Create(dot_Z))
        c14 = CircleCreationWithLine(self, dot_W, dot_Z, color=WHITE)
        dot_A1 = Dot(RIGHT * 2.64165)
        self.play(Create(dot_A1))
        self.play(FadeOut(c14))

        arc6 = ArcCreationWithLine(self, dot_A1, dot_Z, deg(-70))
        arc7 = ArcCreationWithLine(self, dot_Z, dot_A1, deg(70))
        l10 = Line(dot_W.arc_center, np.array((1.33722, 2.68549, 0)))
        dot_C1 = Dot(l10.end)
        self.play(Create(l10))
        self.play(Create(dot_C1))
        self.play(FadeOut(arc6), FadeOut(arc7), FadeOut(dot_Z), FadeOut(dot_A1), FadeOut(l10), FadeOut(dot_W))

        self.play(FadeOut(dot_B), FadeOut(base_line))
        text1 = Text("Now you have two points of the heptadecagon.").move_to(UP * 1.5).scale(0.6)
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text1))

        base_angle = deg(360 / 17)
        dots = []
        animations = []
        for i in range(17):
            angle = base_angle * i
            dots.append(Dot(np.array((np.cos(angle) * 3, np.sin(angle) * 3, 0))))
            animations.append(Create(dots[i]))
        self.play(*animations)
        self.remove(dot_C1, dot_A)
        self.play(FadeOut(base_circle))

        
        for i in range(16):
            l = Line(dots[i].arc_center, dots[i + 1].arc_center)
            self.play(Create(l))
        self.play(Create(Line(dots[16].arc_center, dots[0].arc_center)))

        self.wait()

with tempconfig({"quality": "medium_quality", "disable_caching": True}):
    scene = Heptadecagon()
    scene.render()