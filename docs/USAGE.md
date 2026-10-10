# 使用与配置 · Usage

支持文件读写的 Agent。页面审核脚本需要 Python 3.10+ 与 Pillow；图像编辑、PDF 输出和视觉检查使用宿主可用工具。

An agent with file tools. Page audits require Python 3.10+ and Pillow; image editing, PDF export and visual review use the tools available in your host.

## 检查入口 · Checks

从仓库根目录执行；替换命令中的示例文件路径。
Run from the repository root and replace example paths with your files.

```bash
python3 skills/industrial-product-brochure/scripts/audit_pages.py --help
# Replace this path with your exported page images:
python3 skills/industrial-product-brochure/scripts/audit_pages.py /path/to/pages --expected-pages 8
```

## 工作目录 · Working directory

每个任务使用独立输出目录，保存原始资料、运行配置和审核结果。
Keep source assets, configuration and review records in a separate directory for each task.

[中文示例](../examples/brief.zh.md) · [English brief](../examples/brief.en.md)
