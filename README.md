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

完整PDF成品和配图请从[完整备份附件](https://github.com/sabercldong/zhixin-mock-exams/releases/tag/backup-2026-10-12)下载并恢复。恢复后的第001—037套最近整理的读者版位于 `deliveries/zhixin-2/质心模拟题_正式版`。其余套题可从对应交付目录或 `project/蔡题NNN/整理版/output` 查阅，部分套题的PDF在 `output/pdf` 中。

题目整理及逐套复核已覆盖102套。最近一次清理来源评价、修订标注的工作覆盖第001—037套；第038—102套尚未按这一新增要求统一检查。

## 完整备份与恢复

仓库跟踪可编辑文稿、LaTeX/TikZ源码、计算脚本和索引，并保留已上传的部分PDF与配图。全部原文件，包括所有PDF成品、配图、交付压缩包、构建文件、检查页、预览图和历史文件，保存于[完整备份附件](https://github.com/sabercldong/zhixin-mock-exams/releases/tag/backup-2026-10-12)。完整工程的编译和阅读请使用恢复目录。

备份按文件内容去重，保存为14个ZIP；其中13个ZIP拆成较小的上传分片。路径映射保存于 `snapshot-manifest.json`；同一内容在多个目录中的副本会在恢复时补齐。

1. 下载该备份中的全部 `backup-*` 附件、`archive-parts.json`、`snapshot-manifest.json`、`restore_backup.py` 和 `SHA256SUMS.txt`，放在同一目录。
2. 使用Python 3执行：

```sh
python3 restore_backup.py --destination ../质心模拟题_完整恢复
```

恢复程序先合并较小的上传分片，再校验每个ZIP、每份文件、全部副本和符号链接。目标目录必须为空。完成后可把恢复目录上传到百度网盘。

GitHub页面自动提供的“Source code”压缩包只包含Git跟踪的文件；完整备份应下载上述全部附件。

已安装并登录GitHub CLI的用户，也可以一次下载全部备份附件：

```sh
gh release download backup-2026-10-12 --repo sabercldong/zhixin-mock-exams --dir backup
python3 backup/restore_backup.py --destination ../质心模拟题_完整恢复
```

此仓库为私有仓库。快照日期：2026年10月12日。
