"""Independent q06 renderer; preserves earlier source and review bindings."""
import render_figures as engine

engine.NAMES = {"06": [
    "flow-06", "reference-06", "budget-06",
    "flowwork-06", "isothermal-06", "nozzle-06",
]}

if __name__ == "__main__":
    engine.main()
