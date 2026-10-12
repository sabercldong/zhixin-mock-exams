# 第016套本轮复核定稿

复核日期：2026年10月11日。三版PDF在 `output/pdf/`。各版含完整八题，学生每题5模块，教师每题9模块及4道带完整解答的变式。当前验收以本包顶层复核报告及核验目录为准。

`drafts/` 保存题稿，`markdown/` 保存三版正文，`build/` 保存TeX、计算核验和编译记录，`latex/template.tex` 为统一模板；`figures/` 保存全部TikZ源文件及配图PDF、PNG。原始扫描在上级目录。`历史记录/`、`baseline-review/`、`preview/` 及旧检查点保留既往证据，其中“待验收”是当时状态。

重建需Python 3及PyMuPDF、NumPy、SciPy、SymPy、Pillow，Pandoc、qpdf和带ctex、TikZ的XeLaTeX环境。编译入口自动查找当前用户的Codex LaTeX插件；也可用 `CODEX_LATEX_COMPILER` 指定插件的 `compile_latex.py`。下列命令在本“整理版”目录运行：

```sh
python3 scripts/rebuild_sources.py
python3 scripts/portable_render_figures.py
python3 scripts/prepare_documents.py
python3 scripts/build_documents.py
```

`rebuild_sources.py` 会以本轮快照重写8份题稿及全部TikZ源文件和所需辅助TeX。手工修改题稿后，可直接执行后续步骤，或先更新生成器。旧写稿程序放在 `历史记录/scripts/`，仅用于溯源。

计算与源稿结构检查：

```sh
python3 scripts/verify_question_01.py
python3 scripts/verify_question_02.py --complete
python3 scripts/verify_question_03.py --complete
python3 scripts/verify_question_04.py --complete
python3 scripts/verify_question_05.py --complete
python3 scripts/verify_question_06.py --complete
python3 scripts/verify_question_07.py --complete
python3 scripts/verify_question_08.py
python3 scripts/audit_sources.py 01 02 03 04 05 06 07 08
```

计算程序核验其记录所覆盖的公式和数值；完整验收还包括题源、条件、配图及PDF审读。长变式保留连续跨页的完整推导。
