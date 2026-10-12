# 第025套本轮复核

三版正式PDF在 `output/`。学生每题5模块，教师每题9模块及4道完整变式。当前状态见 `CHECKPOINT_本轮复核.json`，当前计算、排版证据见 `build/` 和 `preview/formal/visual-review.json`。历史记录中的“待确认”属于原题条件或当时状态，应结合正文中的条件说明阅读。

`drafts/` 为8份题稿，`markdown/` 为三版正文，`latex/` 为统一模板，`build/` 为编译源文件和核验记录，`figures/` 为全部TikZ、PDF、PNG及所需辅助数据。上级 `试卷.pdf` 是未修改的原始扫描。

在本“整理版”目录运行：

```sh
python3 scripts/rebuild_sources.py
python3 scripts/render_figures.py
python3 scripts/verify_physics.py
python3 scripts/build_all.py
```

运行需要Python 3及NumPy、SciPy、SymPy、PyMuPDF、Pillow，Pandoc、qpdf和含ctex、TikZ的XeLaTeX环境。编译脚本自动寻找Codex LaTeX插件，也可用 `CODEX_LATEX_COMPILER` 指定其 `compile_latex.py` 路径。

`rebuild_sources.py` 以本轮快照重建题稿与图稿；人工编辑题稿后，可跳过此步直接重新构建。重新构建会把版面审读状态重置为未审，必须重新查看新PDF才能再次确认。旧写稿和旧质检脚本在 `历史记录/`，只供溯源。批次新增70道变式的独立检查入口在包顶层 `核验/verify_added.py`。
