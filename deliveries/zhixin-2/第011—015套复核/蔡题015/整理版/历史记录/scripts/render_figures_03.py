"""Independent q03 collection renderer; preserves q01/q02 entries and evidence."""
import render_figures as engine
engine.NAMES = {'03': ['question-03', 'material-03', 'domain-03', 'particle-03', 'supports-03', 'pressure-03']}
if __name__ == '__main__':
    engine.main()
