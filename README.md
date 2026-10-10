# 工业产品画册

把设备照片、型号和技术参数整理成清楚、统一的产品画册。从单页介绍到多型号目录，兼顾产品信息、版面比例和印刷要求。

**中文** · [English](README.en.md)

由叶轶伦在实际项目中持续迭代，整理当前可分享的工作流、辅助脚本与参考资料。保留已有来源和许可，具体说明见 [NOTICE](NOTICE.md)。

## 可以做什么

- 先核对照片、型号、参数和应用场景。
- 围绕产品特点安排版式、信息层级和中英文文案。
- 检查产品准确性、阅读体验与实物印刷比例。
- 整理页面顺序、尺寸、分辨率和印刷交付说明。

## 工作流程

资料整理 → 页面计划 → 设计排版 → 逐页审核 → 印刷检查 → 交付

## 开始使用

先安装下方依赖，再复制 Skills。已有同名版本时请先备份；套件中的目录保持同级。

```bash
git clone https://github.com/ElliottYip/industrial-product-brochure.git
cd industrial-product-brochure
mkdir -p ~/.codex/skills
cp -R skills/* ~/.codex/skills/
```

在新会话中调用：

```text
使用 $industrial-product-brochure，根据设备照片、型号和参数规划一本 A4 产品画册。先整理素材与页面结构，做一页预览，再展开整本并准备印刷交付说明。
```

## 运行要求

支持文件读写的 Agent。页面审核脚本需要 Python 3.10+ 与 Pillow；图像编辑、PDF 输出和视觉检查使用宿主可用工具。

[详细配置与检查命令](docs/USAGE.md)

## 模块导航

- [industrial-product-brochure](skills/industrial-product-brochure/SKILL.md)

examples/ 提供可改写的任务简报；docs/ 记录配置、检查与版本来源。

## 当前版本

保留现有 1.0.0 基线及当前本地内容。重点是实际项目中积累的素材锁定、版式审阅、设备比例与印刷交付规则，原有 CHANGELOG 与 MIT 许可随包保留。

[迭代说明](CHANGELOG.md) · [验证记录](docs/VERIFICATION.md)

## 使用范围

这是制作流程与检查工具的集合，不是一键自动排版软件。产品参数以原始资料为准，最终印刷需由交付方确认。
