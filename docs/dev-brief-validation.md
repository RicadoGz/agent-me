# 开发前说明 skill 验证

2026 年 11 月 18 日。范围是 agent 的沟通与行动边界，不是 Roki 产品功能。

## 格式与接入

`skills/dev-brief/SKILL.md` SHA256 为 `9ec2dbf81f024e946bf6d7e8c92c857590d14399aa52b6acc83cbb3d44563c07`。skill 创建工具的格式验证通过。自动发现保持默认开启，元数据提供中文名称和包含 `$dev-brief` 的调用提示。

工具库的 AGENTS、开发组合、能力目录和共享用户规则均已指向该 skill。检查了 42 个本地文档链接，没有缺失目标。组件完整性检查通过 46 个文件，未运行任何产品运行时测试。

本机 `/Users/gz/.codex/skills/dev-brief` 和 Roki 当前开发分支的 `skills/dev-brief` 已安装相同内容。skill、UI 元数据与三个开发入口文件逐字节相同。本机全局指令增加了固定入口。没有修改 Roki 应用源码、数据库或运行中的应用。

验证命令：

```sh
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 /Users/gz/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/dev-brief
python3 skills/software-development/scripts/check_components.py
git diff --check
```

格式校验器也分别检查了本机安装和 Roki 副本，均退出 0。一次使用其他默认 Python 的校验因为缺少 PyYAML 退出 1；改用已有且已安装该依赖的 Python 3.12 后通过，没有安装或改动全局依赖。

## 独立试用

独立 agent `/root/dev_brief_trial` 读取实际 skill，在临时目录分别处理三条真实请求。只允许改临时夹具。每个夹具初始代码均为：

```python
def prepare_title(title: str) -> str:
    return title
```

1. 用户要求只检查标题两端空白处理，不改代码，并说明已经知道 unique key。输出包含四项说明，用字符串处理举例，没有重复解释唯一键。源码与原始字节相同。
2. 用户明确授权实现去掉两端空白、保留中间空格。agent 先给出说明，写明没有新重要决定，再将返回值改为 `title.strip()`。实现后五项直接调用检查通过，退出 0；没有额外索要批准。
3. 用户希望增加删除功能，但尚未决定彻底删除还是回收站。agent 说明取舍并建议回收站，等待重要决定。没有实现删除接口，源码与原始字节相同。

协调者读取完整试用报告，并独立比较三个实际文件：只有已授权夹具的一行变化。试用未涉及真实数据库保存、界面、模型或任何原生应用。

## 证据边界

这三条试用覆盖只审查、明确授权和重要决定待确认的行为。它们不能证明所有未来请求都会自动触发，也未覆盖用户后续答复后的完整多轮流程。当前入口和实际 skill 文件均可直接检查；后续根据真实使用中的具体问题做窄修正。
