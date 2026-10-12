"""Independent q05 renderer; no earlier source or evidence is replaced."""
import render_figures as engine
engine.NAMES={"05":["question-05","normals-05","curvature-05","auxiliary-05","perturbation-05","space-05"]}
if __name__=="__main__": engine.main()
