# 蔡题 099｜整理版说明

## 目录

- `markdown/蔡题099_试卷.md`：重新排版后的纯试卷正文。
- `markdown/蔡题099_学生详解.md`：完整题面、模型入口和逐步标准解答。
- `markdown/蔡题099_教师备课.md`：按“题型定位、知识点、物理图像、解题入口、解析、关键洞察、易错点、课堂讲解建议、变式训练”组织的教师版。
- `markdown/蔡题099_核验记录.md`：手写答案比对、独立计算和排版核验记录。
- `markdown/蔡题099_图稿索引.md`：题图与解答图的用途说明。
- `figures/`：TikZ 源文件、16 幅矢量 PDF 和 PNG 预览图。
- `output/pdf/`：三份最终 PDF。
- `output/preview/`：最终 PDF 的逐页渲染预览。
- `scripts/`：Markdown 分版、LaTeX 构建、图稿生成和答案核验程序。

## 构建顺序

1. 修改教师备课 Markdown 的正文。
2. 运行 `scripts/prepare_documents.py` 同步试卷版和学生版。
3. 运行 `scripts/render_figures.py` 编译并拆分 TikZ 图稿。
4. 运行 `scripts/build_documents.py` 生成三份 LaTeX 主文件。
5. 使用 XeLaTeX 编译 `build/` 中的三个主文件。
6. 运行 `scripts/verify_answers.py` 检查关键结论。

原始试卷与手写答案均保持不变；整理版不在正文中加入原始文件链接。
