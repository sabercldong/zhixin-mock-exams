# 第010套复核定稿

2026年10月10日，按“质心模拟题3”的标准复核。本套8题，每题4道变式，共40幅图。试卷、学生详解、教师备课分别为9、58、74页（含封面）。学生版每题含5个模块，教师版含9个模块。全部正文、推导、变式、原始扫描及最终页面已经审读，修正记录见本目录“核对记录.md”及批次“复核报告.md”。

## 文件与重建

`output/pdf/`保存三份定稿；`drafts/`保存8道完整题稿；`markdown/`保存三版文稿；`latex/template.tex`为统一模板；`build/`保存可直接编译的TeX及编译日志；`figures/`保存40幅独立PNG、40幅矢量PDF、8份TikZ源文件和8份图集；`scripts/`保存生成与物理核查程序。

在有Python（PyMuPDF、NumPy、SciPy）、Pandoc、qpdf及XeLaTeX的环境下，可在本目录执行：

```sh
python3 scripts/write_drafts.py
python3 scripts/make_figures.py
python3 scripts/render_figures.py
python3 scripts/build_documents.py
```

编译脚本优先读取`CODEX_LATEX_COMPILER`，未设置时查找当前用户Codex LaTeX插件内的`compile_latex.py`。如复制到另一台电脑，需要提供相应编译入口及中文字体。生成器与当前定稿同步；编译不会自动宣称新一轮人工审读完成。批次已在迁移目录实际重建第010套全部40幅图及三份PDF，详情见批次`核验/迁移重建报告.json`。

原始扫描保存在批次`原始扫描/蔡题010/`；部分“答案.pdf”存在跨套混页，不能作为逐题完全匹配的参考答案。
