# 第036套当前工程

本目录是2026年10月11日复核后的当前版本。正式三版PDF在 `output/`；8道完整题稿在 `drafts/`；教师版每题含4道带解答的变式。

当前验收状态见 `CHECKPOINT_本轮复核.json` 和 `preview/formal/visual-review.json`。`build/current-quality.json` 只记录自动技术检查，其 actual_visual_review=false 不代表当前人工审读状态；人工审读绑定记录独立保存。旧核对记录、旧验收报告、旧预览和旧 quality_check.py 放在 `历史记录/`。

正常修改从 drafts/question-NN.md 开始，再运行 `python scripts/build_all.py`。该入口从题稿生成三版Markdown与TeX、编译PDF并执行当前质量检查。不要在修改题稿后直接运行 rebuild_sources.py，否则会被交付时的快照覆盖。修改图稿后另运行 `python scripts/render_figures.py`。

在丢失源稿、需要恢复交付版本时，依次运行 `python scripts/rebuild_sources.py`、`python scripts/render_figures.py`、`python scripts/build_all.py`。本轮已在独立新目录删除题稿、图稿和生成物后实际执行这一流程；文档文字与72dpi页面像素均与交付版一致。

运行需要Python3（NumPy、SciPy、SymPy、PyMuPDF、Pillow）、pandoc、qpdf、XeLaTeX及ctex/TikZ，并使用LaTeX插件的compile_latex.py。build_all.py会发现本机该插件，或使用环境变量 CODEX_LATEX_COMPILER 指定其完整路径。包内未捆绑系统编译器；build中的重复PDF与辅助缓存已移除，正式PDF仅在output保存。

修改后应重新执行 scripts/verify_results.py、当前质量检查与页面审读。重新编译可能改变PDF内部时间戳；相同版本应以正文、图形与页面像素比较，旧视觉记录不能自动作为新版本验收。
