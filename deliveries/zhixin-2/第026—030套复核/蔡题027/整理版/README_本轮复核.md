# 第027套本轮复核

三版正式PDF在 `output/`。学生每题5模块，教师每题9模块及4道完整变式。当前状态见 `CHECKPOINT_本轮复核.json`，计算、版面证据见 `build/` 和 `preview/formal/visual-review.json`。历史状态已收在 `历史记录/`；模型限制以当前正文为准。

`drafts/` 为8份题稿，`markdown/` 为三版正文，`latex/` 为统一模板，`build/` 为TeX和核验记录，`figures/` 含全部TikZ、PDF、PNG。上级目录保留实际存在的原始试卷与答案扫描。

在本“整理版”目录运行：

```sh
python3 scripts/rebuild_sources.py
python3 scripts/render_figures.py
python3 scripts/verify_physics.py
python3 scripts/build_all.py
```

需要Python 3及NumPy、SciPy、SymPy、PyMuPDF、Pillow，Pandoc、qpdf和含ctex、TikZ的XeLaTeX环境。编译脚本自动寻找Codex LaTeX插件，也可用 `CODEX_LATEX_COMPILER` 指定 `compile_latex.py`。

`rebuild_sources.py` 从本轮快照恢复题稿与图稿。人工编辑题稿后，可跳过此步直接构建。重新构建会把版面审读状态重置为未审；应重新查看新PDF。旧写稿和旧质检入口仅供溯源。新增100道变式的独立检查入口在包顶层 `核验/verify_added.py`。
