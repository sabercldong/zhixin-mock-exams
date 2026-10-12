# 蔡题 101｜整理版说明

## 目录

- `markdown/蔡题101_试卷.md`：重新排版后的纯试卷正文。
- `markdown/蔡题101_学生详解.md`：完整题面、核心模型与逐步标准解答。
- `markdown/蔡题101_教师备课.md`：按“题型定位、知识点、物理图像、解题入口、解析、关键洞察、易错点、课堂讲解建议、变式训练”组织的教师版，并附答案核验。
- `markdown/蔡题101_核验记录.md`：手写答案比对、修正项和独立检查。
- `markdown/蔡题101_图稿索引.md`：题图、解答图及源文件对应关系。
- `figures/`：TikZ 源文件、矢量 PDF 和 PNG 预览图。
- `output/pdf/`：三套最终 PDF。
- `scripts/`：Markdown 分版、LaTeX 构建和答案核验程序。

## 构建顺序

1. 修改 `markdown/蔡题101_教师备课.md` 的正文内容。
2. 运行 `scripts/prepare_documents.py` 生成试卷版和学生详解版 Markdown。
3. 编译 `figures/蔡题101_图稿源文件.tex` 并更新各独立图形。
4. 运行 `scripts/build_documents.py` 生成三套 LaTeX 文件。
5. 使用 XeLaTeX 编译 `build/` 中的三个主文件。
6. 运行 `scripts/verify_answers.py` 检查关键结论。

原始 `试卷.pdf` 和 `答案.pdf` 不作任何修改。
