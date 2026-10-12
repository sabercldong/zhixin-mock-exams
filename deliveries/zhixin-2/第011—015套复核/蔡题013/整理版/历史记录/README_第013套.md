# 第013套完整源码包

八题完成：学生五模块、教师九模块，32个完整带解变式、40幅TikZ图。三版正文页数8/56/71，各另有一页封面。校勘、96项主核验及8组补充核验见核对记录.md。

外层试卷.pdf与答案.pdf为未经改动的原扫描，分别4页（封面加3页试题）与7页。全部原页均已实际查看，八题完整，无外部补页。同向速度反例、准静态独轮车、共线电荷分支、钉子上升方向、双透镜两组正焦距、h与hbar及磁场近似阶次的说明见核对记录和正文。

## 编辑与编译

drafts为八份九模块主稿，markdown为三版抽取稿；build有三份TeX及日志，latex/template.tex为统一模板；figures有40份独立矢量PDF、40份PNG及八份多图TikZ源。

包内build/*.tex使用相对图路径。解压后进入build，对各TeX运行XeLaTeX两遍，需ctex、TikZ及模板宏包。字体、引擎和版本可能影响分页，迁移后应重新审读。

scripts/build_documents.py依赖pandoc、qpdf、PyMuPDF与XeLaTeX，默认使用当前电脑Codex附带的compile_latex.py，路径见preview_drafts.py；迁移时可配置对应编译器，也可直接编译包内TeX。render_figures.py的COMPILER需相应配置。

write_drafts.py和make_figures.py保存完整正文与图稿生成逻辑，运行会覆盖对应文件。日常可直接编辑主稿和图源，再构建。make_figures.py依赖NumPy，自动同步图名；render_figures.py无参数重编八题，也可用题号单编。verify_physics.py依赖NumPy、SciPy，生成physics_verification.json。

七份脚本、八份主稿、八份图源及物理报告已在独立临时目录逐字节复现。preview/source-reproduction.json记录复现结果。render_full_review.py依赖PyMuPDF与Pillow，仅生成审读图像，生成不代表实际查看。

本次实际查看24张全页总览、36页重点高清及八张40图总览，覆盖三版138个物理页。preview/full-review保留图像、页索引及visual-reviewed.json。build_report.json的完成标志仅适用于已审读并绑定SHA256的版本，任何后续改动重建均须重新验收。
