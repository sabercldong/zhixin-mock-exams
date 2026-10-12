# 第012套本轮复核定稿

复核日期：2026年10月11日。当前交付文件在 `output/pdf/`。三版均为完整八题；学生每题5模块，教师每题9模块及4道带解变式。当前验收结论以本包顶层“复核报告.md”和“核验/最终PDF版面审读.json”为准。

`drafts/` 是当前题稿，`markdown/` 是三版正文，`build/` 含对应TeX与编译记录，`latex/template.tex` 是统一模板，`figures/` 含TikZ源文件、矢量PDF和PNG。原始扫描保存在上级目录。`历史记录/`、`baseline-review/`、`preview/` 及旧检查点保存既往证据；旧记录中的“待验收”描述其生成当时的阶段，不是本轮最终状态。

重建需Python 3及PyMuPDF、NumPy、SciPy、SymPy、Pillow，Pandoc、qpdf，以及带ctex和TikZ的XeLaTeX运行环境。编译入口自动从当前用户的Codex LaTeX插件目录查找，也可设置 `CODEX_LATEX_COMPILER` 为该插件 `compile_latex.py` 的路径。原目录及第020套工程均不作为重建依赖。下面的命令在本“整理版”目录运行：

```sh
python3 scripts/rebuild_sources.py
python3 scripts/portable_render_figures.py
python3 scripts/build_documents.py
```

`rebuild_sources.py` 会用本轮保存的版本重写8份题稿及8份TikZ源文件；手工修改题稿后应直接执行后续编译命令，或先同步生成器。`历史记录/scripts/` 中的旧写稿程序只供溯源，可能包含旧措辞。

物理计算核验：

```sh
python3 scripts/verify_physics.py
```

计算脚本输出仅说明其覆盖的计算检查通过；整套验收还需题源、图稿和最终PDF审查。第014、015套保留长推导及连续跨页变式，未为压页删去解答。
