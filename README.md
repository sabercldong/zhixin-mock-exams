# 质心模拟题

102套物理竞赛模拟题项目。每套提供试卷、学生详解、教师备课三版，并保存 Markdown、LaTeX、TikZ 图稿、计算脚本和复核记录。

## 目录

- `project/`：主项目，包含蔡题001—蔡题102。
- `deliveries/zhixin-2/`：“质心模拟题2”的交付目录，覆盖第001—037套。
- `deliveries/zhixin-3/`：“质心模拟题3”的交付目录，覆盖第048—102套。
- `deliveries/takeover/`：“质心模拟题3（接管）”的交付目录，覆盖第038—047套。
- `index/snapshot-manifest.json`：全部文件的路径、大小、SHA-256及恢复映射。

最早“质心模拟题”的独立工作目录为空；它的题库工程已在主项目中。

## 阅读成品

第001—037套最近整理的读者版位于 [正式版目录](deliveries/zhixin-2/质心模拟题_正式版)。其余套题可从对应交付目录或 `project/蔡题NNN/整理版/output` 查阅，部分套题的PDF在 `output/pdf` 中。

题目整理及逐套复核已覆盖102套。最近一次清理来源评价、修订标注的工作覆盖第001—037套；第038—102套尚未按这一新增要求统一检查。

## 完整备份与恢复

仓库跟踪可编辑工程、文稿、图稿和PDF成品。全部原文件，包括较大的交付压缩包、构建文件、检查页、预览图和历史文件，另存于[完整备份附件](https://github.com/sabercldong/zhixin-mock-exams/releases/tag/backup-2026-10-12)。

备份按文件内容去重，分成若干独立ZIP附件。路径映射保存于 `snapshot-manifest.json`；同一内容在多个目录中的副本会在恢复时补齐。

1. 下载该备份中的全部 `backup-*` 附件、`archive-parts.json`、`snapshot-manifest.json`、`restore_backup.py` 和 `SHA256SUMS.txt`，放在同一目录。
2. 使用Python 3执行：

```sh
python3 restore_backup.py --destination ../质心模拟题_完整恢复
```

恢复程序先合并较小的上传分片，再校验每个ZIP、每份文件、全部副本和符号链接。目标目录必须为空。完成后可把恢复目录上传到百度网盘。

GitHub页面自动提供的“Source code”压缩包只包含Git跟踪的文件；完整备份应下载上述全部附件。

此仓库为私有仓库。快照日期：2026年10月12日。
