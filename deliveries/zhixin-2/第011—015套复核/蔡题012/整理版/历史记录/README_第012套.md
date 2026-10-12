# 第012套完整源码包

八题完成：学生五模块、教师九模块，32个带解变式、40幅TikZ图。三版正文页数8/56/72，各另有一页封面。校勘、96项主核验及8组补充核验见核对记录.md。

外层试卷.pdf与答案.pdf为未经改动的第012套原扫描，分别三页和四页。原题面前两页为印刷第2、3页，第三物理页为空白。缺失首页已由第011套原卷物理第3页补齐；补充完整原PDF保存在preview/第011套原卷_含第012套首页.pdf，前两页仅作为来源保留。原卷有效页、空白页、补充首页与四页手写解均已实际查看。人影双分支、返回相位、纯滚动、半空间扩散和回声路径条件及原答案差异见核对记录。

## 编辑与编译

drafts为八份九模块主稿，markdown为三版抽取稿。build包含三份TeX与编译日志，latex/template.tex为统一模板；figures包含40份独立矢量PDF、40份PNG及八份多图TikZ源。

包内build/*.tex使用相对图路径。解压后进入build目录，对各TeX运行XeLaTeX两遍；需ctex、TikZ及模板宏包。更换字体、引擎或版本可能改变分页，应重新审读。

修改主稿后运行scripts/build_documents.py，依赖pandoc、qpdf、PyMuPDF与XeLaTeX。默认使用当前电脑Codex附带compile_latex.py，路径见scripts/preview_drafts.py；迁移时可配置可用编译器，或直接编译包内TeX。render_figures.py的COMPILER也应对应修改。

write_drafts.py和make_figures.py保存全部正文与图稿生成逻辑，运行会覆盖对应文件；日常也可直接编辑主稿和图源。make_figures.py依赖NumPy，自动同步图名清单。七份脚本、八份主稿、八份图源与核验报告已在独立临时目录实际复现。

运行render_figures.py 06可重编译第6题配图，无参数时重编八题。verify_physics.py依赖NumPy和SciPy，生成physics_verification.json；其中96项主核验和8组补充核验均通过。

render_full_review.py依赖PyMuPDF与Pillow，生成审读图像；生成不代表实际查看。本次已查看25张全页总览、36页重点高清及八张40图总览，共覆盖三版139个物理页。preview/full-review保存预览、页索引与visual-reviewed.json；preview/source-reproduction.json记录源码复现。

build_report.json的完成标志只适用于当前审读并绑定SHA256的版本；任何后续改动重建均须重新审读。
