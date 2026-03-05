"""
摘要关键点提取器工具
从长文本中提取关键要点、行动项和利益相关者影响
"""

import re
from typing import Dict, List, Any
from datetime import datetime


class KeyPointsExtractor:
    """
    从文本中提取关键要点的工具
    
    功能:
    - 提取最重要的3-5个关键点,识别行动项和计划, 分析利益相关者影响,提供文本统计信息
    """
    
    def __init__(self, name: str = "key_points_extractor"):
        self.name = name
        self.description = "从长文本中提取关键要点、行动项和利益相关者影响"
    
    def execute(self, text: str, max_points: int = 5) -> Dict[str, Any]:
        """
        执行关键点提取
        
        Args:
            text: 输入文本（至少10个字符）
            max_points: 最大关键点数量（1-10之间）
            
        Returns:
            包含关键点、摘要、行动项等的字典
            
        Raises:
            ValueError: 当输入无效时
        """
        try:
            # 输入验证
            self._validate_input(text, max_points)
            
            # 预处理文本
            cleaned_text = self._preprocess_text(text)
            
            # 提取关键点
            key_points = self._extract_key_points(cleaned_text, max_points)
            
            # 生成摘要
            summary = self._generate_summary(key_points)
            
            # 识别行动项
            action_items = self._identify_action_items(cleaned_text)
            
            # 分析利益相关者影响
            stakeholder_impact = self._analyze_stakeholder_impact(cleaned_text)
            
            # 统计信息
            statistics = self._get_statistics(cleaned_text)
            
            return {
                "success": True,
                "key_points": key_points,
                "summary": summary,
                "action_items": action_items,
                "stakeholder_impact": stakeholder_impact,
                "statistics": statistics,
                "metadata": {
                    "processing_time": datetime.now().isoformat(),
                    "tool_version": "1.0.0"
                }
            }
            
        except ValueError as e:
            # 返回结构化的错误信息
            return {
                "success": False,
                "error": str(e),
                "error_type": "ValidationError"
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"处理过程中发生错误: {str(e)}",
                "error_type": "ProcessingError"
            }
    
    def _validate_input(self, text: str, max_points: int):
        """验证输入参数"""
        if not isinstance(text, str):
            raise ValueError(f"text必须是字符串，得到的是{type(text).__name__}")
        
        if len(text.strip()) < 10:
            raise ValueError("text长度至少为10个字符")
        
        if not isinstance(max_points, int):
            raise ValueError(f"max_points必须是整数，得到的是{type(max_points).__name__}")
        
        if max_points < 1 or max_points > 10:
            raise ValueError("max_points必须在1-10之间")
    
    def _preprocess_text(self, text: str) -> str:
        """预处理文本"""
        # 去除多余空白
        text = re.sub(r'\s+', ' ', text.strip())
        return text
    
    def _extract_key_points(self, text: str, max_points: int) -> List[str]:
        """
        提取关键点（基于规则）
        
        规则：
        1. 包含数字的句子（金额、百分比、日期）
        2. 包含关键词的句子（宣布、推出、计划、增长等）
        3. 段落首句和末句
        """
        # 分句
        sentences = re.split(r'[。！？.!?]', text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
        
        # 打分规则
        scored_sentences = []
        for i, sentence in enumerate(sentences):
            score = 0
            
            # 规则1：包含数字
            if re.search(r'\d+', sentence):
                score += 3
            
            # 规则2：包含金额符号
            if re.search(r'[¥$€亿元万元]', sentence):
                score += 2
            
            # 规则3：包含关键词
            keywords = ['宣布', '推出', '计划', '增长', '下降', '投资', '发布', 
                       '创新', '突破', '首次', '重大', '关键', '重要']
            for kw in keywords:
                if kw in sentence:
                    score += 1
            
            # 规则4：段落首句和末句
            if i == 0 or i == len(sentences) - 1:
                score += 1
            
            # 规则5：包含百分比
            if re.search(r'\d+%|\d+百分比', sentence):
                score += 2
            
            scored_sentences.append((sentence, score))
        
        # 按分数排序，取前max_points个
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        key_points = [s[0] for s in scored_sentences[:max_points]]
        
        return key_points if key_points else ["未能提取到关键点"]
    
    def _generate_summary(self, key_points: List[str]) -> str:
        """生成一句话摘要"""
        if not key_points:
            return "无内容可总结"
        
        # 简单组合关键点前几个词
        summary = "；".join(key_points[:2])
        if len(summary) > 100:
            summary = summary[:97] + "..."
        
        return summary
    
    def _identify_action_items(self, text: str) -> List[str]:
        """识别行动项"""
        action_patterns = [
            r'(将|计划|准备|打算|预计).{5,20}(。|$)',
            r'(需要|必须|应该).{5,20}(。|$)',
            r'(推出|发布|上线|启动).{5,20}(。|$)'
        ]
        
        actions = []
        for pattern in action_patterns:
            matches = re.findall(pattern, text)
            actions.extend([m[0] if isinstance(m, tuple) else m for m in matches])
        
        return actions[:3]  # 最多返回3个
    
    def _analyze_stakeholder_impact(self, text: str) -> Dict[str, str]:
        """分析利益相关者影响"""
        stakeholders = {
            'investors': ['股东', '投资者', '投资方', '股价', '分红'],
            'employees': ['员工', '裁员', '招聘', '薪资', '福利'],
            'customers': ['客户', '用户', '消费者', '体验', '服务'],
            'partners': ['合作伙伴', '供应商', '渠道']
        }
        
        impact = {}
        text_lower = text.lower()
        
        for stakeholder, keywords in stakeholders.items():
            mentioned = any(kw in text_lower for kw in keywords)
            if mentioned:
                # 简单判断情感倾向
                positive = any(word in text_lower for word in ['增长', '提升', '利好', '增加'])
                negative = any(word in text_lower for word in ['下降', '裁员', '减少', '风险'])
                
                if positive and not negative:
                    impact[stakeholder] = '正面影响'
                elif negative and not positive:
                    impact[stakeholder] = '负面影响'
                else:
                    impact[stakeholder] = '影响不确定'
        
        return impact if impact else {'general': '无明显特定利益相关者影响'}
    
    def _get_statistics(self, text: str) -> Dict[str, Any]:
        """获取文本统计信息"""
        sentences = re.split(r'[。！？.!?]', text)
        sentences = [s for s in sentences if s.strip()]
        
        # 识别关键数据
        numbers = re.findall(r'\d+\.?\d*', text)
        percentages = re.findall(r'\d+%', text)
        money = re.findall(r'[¥$€]\d+\.?\d*[亿万元]?', text)
        
        return {
            'total_characters': len(text),
            'total_sentences': len(sentences),
            'avg_sentence_length': round(len(text) / max(len(sentences), 1), 1),
            'key_data_points': {
                'numbers_found': len(numbers),
                'percentages_found': len(percentages),
                'money_mentions': len(money)
            }
        }


# 兼容作业要求的Tool包装类
class Tool:
    def __init__(self, name: str, description: str, fn):
        self.name = name
        self.description = description
        self.fn = fn
    
    def execute(self, **kwargs):
        return self.fn(**kwargs)


# 创建工具实例
def create_key_points_tool():
    extractor = KeyPointsExtractor()
    return Tool(
        name="key_points_extractor",
        description="从长文本中提取关键要点、行动项和利益相关者影响",
        fn=extractor.execute
    )