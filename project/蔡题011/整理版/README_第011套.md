# 第011套完整源码包

八题完成：学生五模块、教师九模块，32个带解变式、40幅TikZ图。三版正文页数8/56/72，各另有一页封面。校勘、96项主核验及8组补充核验见核对记录.md。

外层试卷.pdf与答案.pdf为未改动原扫描，分别三个物理页和四页本套手写解答；原题面前两页为本套，第三页属于第012套，未纳入整理稿。全部原页已实际查看，对照手写解后独立推导，已校勘弹道时间、开放填充总焓和引线路径等问题。

## 编辑与编译

drafts为八份九模块主稿，markdown为三版抽取稿。build包含三份TeX与编译日志，latex/template.tex为统一模板；figures包含40份独立矢量PDF、40份PNG及八份多图TikZ源。

包内build/*.tex使用相对图路径。解压后进入build目录，对各TeX运行XeLaTeX两遍；需ctex、TikZ及模板宏包。更换字体、引擎或版本可能改变分页，应重新审读。

修改主稿后运行scripts/build_documents.py，依赖pandoc、qpdf、PyMuPDF与XeLaTeX。默认使用当前电脑Codex附带compile_latex.py，路径见scripts/preview_drafts.py；迁移时可配置可用编译器，或直接编译包内TeX。render_figures.py的COMPILER也应对应修改。

write_drafts.py和make_figures.py保存全部正文与图稿生成逻辑，运行会覆盖对应文件；日常也可直接编辑主稿和图源。make_figures.py依赖NumPy，自动同步图名清单。七份脚本、八份主稿、八份图源与核验报告已在独立临时目录实际复现。

运行render_figures.py 06可重编译第6题配图，无参数时重编八题。verify_physics.py依赖NumPy和SciPy，生成physics_verification.json；其中96项主核验和8组补充核验均通过。

render_full_review.py依赖PyMuPDF与Pillow，生成审读图像；生成不代表实际查看。本次已查看25张全页总览、26页重点高清及八张40图总览，共覆盖三版139个物理页。preview/full-review保存预览、页索引与visual-reviewed.json；preview/source-reproduction.json记录源码复现。

build_report.json的完成标志只适用于当前审读并绑定SHA256的版本；任何后续改动重建均须重新审读。
