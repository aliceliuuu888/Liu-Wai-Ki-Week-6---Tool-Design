# Liu-Wai-Ki-Week-6---Tool-Design
# 摘要关键点提取器工具

## 工具描述
从长文本中自动提取关键要点、行动项和利益相关者影响，帮助用户快速理解文档核心内容。

## 功能特点
- **关键点提取**：识别最重要的3-5个句子
- **摘要生成**：自动生成一句话摘要
- **行动项识别**：找出文本中的行动计划
- **利益相关者分析**：分析不同群体的影响
- **文本统计**：提供基本的统计信息

## 安装依赖

```bash
pip install python-dotenv
```

## 配置 API Key（可选）

1. **复制环境变量示例文件**：
```bash
cp .env.example .env
```

2. **编辑 `.env` 文件**，填入你的 DeepSeek API key：
```
DEEPSEEK_API_KEY=sk-你的key在这里
```

3. **运行演示程序**：
```bash
python demo.py
```

## 使用示例

```python
from tool import KeyPointsExtractor

# 创建提取器
extractor = KeyPointsExtractor()

# 提取关键点
text = "这是一段需要分析的文本..."
result = extractor.execute(text, max_points=5)

if result["success"]:
    print(result["key_points"])
else:
    print(f"错误: {result['error']}")
```

##  输出格式示例

```json
{
    "success": true,
    "key_points": ["Q3营收50亿美元，同比增长20%", "将在亚洲开设5家新工厂"],
    "summary": "公司业绩增长但伴随重组裁员",
    "action_items": ["开设新工厂", "裁员1000人"],
    "stakeholder_impact": {
        "investors": "正面影响",
        "employees": "负面影响"
    },
    "statistics": {
        "total_characters": 350,
        "total_sentences": 8
    }
}
```

##  文件结构

```
.
├── tool.py          # 工具实现
├── demo.py          # 演示脚本
├── README.md        # 本文档
├── .env.example     # 环境变量示例
└── .gitignore       # Git忽略文件
```

##  演示内容

运行 `demo.py` 会展示：
-  **成功案例**：CEO演讲文本分析
-  **错误案例**：空文本、无效参数处理

## ⚠️ 注意事项

- API Key 是可选配置，不配置也能运行（使用模拟模式）
- 如果要使用真实 API，请确保账户有余额
- 永远不要提交 `.env` 文件到 GitHub
