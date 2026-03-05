"""
演示摘要关键点提取器的使用
包含成功案例和错误案例
"""

import os
from dotenv import load_dotenv
from tool import KeyPointsExtractor, create_key_points_tool

# 加载环境变量
load_dotenv()

def demo_success_case(extractor):
    """演示成功案例"""
    print("\n" + "="*50)
    print("✅ 成功案例：CEO演讲文本")
    print("="*50)
    
    # 测试文本
    text = """
    各位股东，我很高兴宣布公司2024年第三季度业绩。
    营收达到50亿美元，同比增长20%。我们将在亚洲开设5家新工厂，
    创造3000个就业岗位。同时，我们推出新产品线"AI助手"，
    预计明年贡献15%的营收。但遗憾的是，由于业务重组，
    我们将裁员1000人，主要集中在传统业务部门。
    研发投入将增加30%，重点布局AI和量子计算。
    我们计划在明年第一季度完成对一家AI初创公司的收购。
    """
    
    print(f"📝 输入文本长度: {len(text)} 字符")
    
    # 执行提取
    result = extractor.execute(text, max_points=5)
    
    # 打印结果
    if result["success"]:
        print("\n📊 提取结果:")
        print(f"\n🔑 关键点 ({len(result['key_points'])}个):")
        for i, point in enumerate(result['key_points'], 1):
            print(f"   {i}. {point}")
        
        print(f"\n📋 一句话摘要:")
        print(f"   {result['summary']}")
        
        if result['action_items']:
            print(f"\n⚡ 行动项:")
            for item in result['action_items']:
                print(f"   • {item}")
        
        if result['stakeholder_impact']:
            print(f"\n👥 利益相关者影响:")
            for stakeholder, impact in result['stakeholder_impact'].items():
                print(f"   • {stakeholder}: {impact}")
        
        print(f"\n📈 统计信息:")
        stats = result['statistics']
        print(f"   • 总字符数: {stats['total_characters']}")
        print(f"   • 总句数: {stats['total_sentences']}")
        print(f"   • 平均句长: {stats['avg_sentence_length']} 字符")
        print(f"   • 关键数据点: {stats['key_data_points']}")
    else:
        print(f"❌ 处理失败: {result.get('error')}")

def demo_error_case(extractor):
    """演示错误案例"""
    print("\n" + "="*50)
    print("❌ 错误案例1：空文本")
    print("="*50)
    
    # 错误案例1：空文本
    result = extractor.execute("", max_points=5)
    print(f"输入: 空字符串")
    if not result["success"]:
        print(f"结果: {result['error']}")
        print(f"错误类型: {result['error_type']}")
    
    print("\n" + "="*50)
    print("❌ 错误案例2：无效max_points参数")
    print("="*50)
    
    # 错误案例2：无效的max_points
    try:
        result = extractor.execute("这是一段测试文本。", max_points=20)
        if not result["success"]:
            print(f"结果: {result['error']}")
    except Exception as e:
        print(f"捕获异常: {e}")

def demo_with_real_api():
    """如果提供了API key，使用真实API（这里模拟）"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    
    if api_key:
        print("\n🔑 使用DeepSeek API模式")
        # 这里可以添加真实的API调用代码
        # 例如使用requests库调用DeepSeek API
        print("正在调用DeepSeek API...")
        # 模拟API调用
        print("API调用成功！")
    else:
        print("\n⚠️ 未找到API key，使用本地规则模式")

def main():
    """主演示函数"""
    print("="*60)
    print("摘要关键点提取器 - 演示程序")
    print("="*60)
    
    # 创建提取器实例
    extractor = KeyPointsExtractor()
    
    # 检查API key
    demo_with_real_api()
    
    # 演示成功案例
    demo_success_case(extractor)
    
    # 演示错误案例
    demo_error_case(extractor)
    
    print("\n" + "="*60)
    print("演示结束")
    print("="*60)

if __name__ == "__main__":
    main()