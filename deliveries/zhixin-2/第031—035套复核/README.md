# 第031—035套复核交付包

本包包含5套、40题、160道完整解答变式、120幅配图、15份正式PDF，共858页。沿用对话“质心模拟题3”的最近标准，并使用 humanizer-zh 清理表达。详细结果见 `复核报告.md`，当前验收见 `核验/最终交付验收.json`。

每套的正式PDF在 `蔡题NNN/整理版/output/`，文件名为 `第NNN套_试卷版.pdf`、`第NNN套_学生详解版.pdf`、`第NNN套_教师备课版.pdf`。各套同目录中的 `README_本轮复核.md` 提供重建命令，`CHECKPOINT_本轮复核.json` 标明本轮状态。

题稿、Markdown、TeX、TikZ源文件、图形PDF/PNG、原始扫描、物理核验与编译日志均已保留。五套从源快照迁到新目录删除生成物后重建，全部通过图像、文字与页面栅格一致性检查。重建会重新生成PDF并清除“已经人工审读”的状态；对新PDF仍须重新检查。

新增变式可在包目录运行 `python3 核验/verify_added.py`，需要NumPy、SciPy、SymPy。文档与图稿构建还需Python、PyMuPDF、Pillow、Pandoc、qpdf和含ctex、TikZ的XeLaTeX环境；可用 `CODEX_LATEX_COMPILER` 指定Codex LaTeX插件的编译脚本。

`核验/最终PDF版面审读.json` 记录当前PDF及查看过的页面图像；`核验/baseline_binding_audit.json` 记录旧版审读绑定。用于继承审读的12份旧版PDF收在 `核验/基线PDF/`，正式阅读使用各套 `output/` 中的15份当前文件。第035套全部采用本轮页面审读证据。

`MANIFEST_SHA256.json` 提供包内所有其他文件的SHA256。`历史记录/` 与 `baseline-review/` 用于溯源，当前状态以本轮验收和各套CHECKPOINT为准。原始下载目录没有改动。下一批从第036套开始。
