# 第034套编辑与重建

正式阅读文件是output中的三个PDF：试卷版10页、学生详解版77页（正文76页）、教师备课版100页（正文99页）。对应三个Markdown保存在markdown。23幅题图及解答图的TikZ源文件、矢量PDF、PNG、LaTeX、构建与核验脚本和预览全部保留。

内容主文件为markdown/蔡题034_教师备课.md。修改主文件后，在本目录运行：

```sh
python3 scripts/build_all.py
```

脚本从教师主文件提取学生前五模块和试卷题干，重新核验八题、编译全部图稿与三版本PDF、检查结构与正文深度，并生成逐页总览。学生版和试卷版Markdown是生成文件，不直接编辑。图形应修改figures/题XX_图稿源文件.tex，成品正文不嵌入源码。

构建固定A4、12pt、四边22mm、行距1.24、段距0.35em，不通过间距、重复文字或额外分页补页。第5题第（3）问文字与对应题图使用一个不可拆分的排版盒，避免题文留在前页而下一页只有图。

第2题必须保留模型条件说明：静力承载、固定球心滑动、两壁纯滚动是不同问题；原题不足以唯一选择起动分支。解析给出完整条件和经直接动力学核验的反例，不强给互斥区域。第7题左侧同像答案已更正为物距64 cm、像距320 cm，证据保存在独立光线验证结果中。

当前机器验收为build/strict-quality.json，实际视觉复审为preview/formal/visual-review.json。视觉记录绑定PDF的SHA-256；重编译后校验值改变时，应检查受影响页面并更新记录，不能只凭编译成功宣布视觉验收。重点页高清图可用scripts/render_review_pages.py重新生成。

drafts、旧分题preview、工作稿复核报告.md及build/working-quality.json是保留的历史阶段材料。只有明确需要重新汇入全部分题稿时才使用build_all.py的--from-drafts参数，以免覆盖主文件后续编辑。第2题内部诊断记录也不替代正式解析。

沿用项目现有Pandoc、XeLaTeX、qpdf、Poppler和Python环境。第2题优化核验使用已存在的/Users/dongxingxi/.local/share/uv/tools/docling/bin/python及其中的SciPy；脚本中的SCIENTIFIC_PYTHON指定这个运行时。迁移机器时需改为已经具备SciPy的Python路径。本次没有另行安装依赖。

原始试卷、手写答案及全部既有辅助文件未删除、未转移；保护校验值见核对记录.md。第101套未修改。
