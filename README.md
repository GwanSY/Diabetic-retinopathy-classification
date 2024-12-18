# Diabetic-retinopathy-classification
本系统旨在详细描述基于Transformer的糖尿病视网膜病变（DR）智能诊疗可视化平台的设计思路、实现过程及操作方法。通过提供全面的技术和使用文档，帮助开发人员明确系统的开发目标，指导用户高效使用平台功能，并为系统的维护与升级提供参考，确保系统在实际应用中发挥最大效用，助力糖尿病视网膜病变的早期诊断与治疗。

# 项目背景

糖尿病（Diabetes Mellitus，简称DM）是一种以高血糖为主要表现的慢性代谢性疾病，其长期高血糖状态会导致全身代谢紊乱，对微循环系统产生不良影响。糖尿病视网膜病变（Diabetic Retinopathy，简称DR）是糖尿病引发的常见并发症之一，对患者的眼底微血管造成损害，是导致成人失明的主要原因之一。DR的病变早期症状往往轻微，容易被忽视，但若未能及时干预，可能会导致视力严重受损甚至永久性失明。
中国是全球糖尿病患者人数最多的国家，患者数量超过1.4亿人。然而，近50%的患者未能及时发现或了解自身的病情。随着病程的进展，DR的发病率逐步升高，及时开展早期筛查和干预至关重要。然而，当前我国医疗系统主要依赖于医生的人工诊断，对患者进行眼底图像分析与分级，这种手工诊断既耗费时间，又容易受到医生专业水平和主观判断的限制。医疗资源不足和医务人员的高负荷工作也可能导致误诊、漏诊情况的发生。
为应对这一挑战，国家已在“十四五”眼健康规划中明确提出，提升糖尿病视网膜病变的早诊早治和规范化治疗水平，并将其作为国家战略之一。随着人工智能和深度学习技术的发展，基于机器学习和计算机视觉的辅助诊断技术逐渐成为智能医疗领域的重要方向。通过对患者的眼底图像进行自动化分析与分级，不仅能够缓解医生的工作压力，还能提高诊断的效率和准确性，为大规模筛查提供技术支持。

# 系统

![image](https://github.com/GwanSY/Diabetic-retinopathy-classification/blob/main/%E5%9B%BE%E7%89%871.png)