from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "markdown" / "蔡题101_教师备课.md"


TYPE_POSITION = {
    "1": "分段抛体与瞬时碰撞综合题。第（1）问以质点模型训练运动分段、弹性反射和时间根筛选；第（2）问加入刚体自转与滑动摩擦冲量，属于从质点力学向刚体碰撞过渡的典型题。",
    "2": "偏心弹性碰撞与刚体平面运动综合题。先用三个守恒关系确定碰后状态，再用相对运动与有限杆几何研究二次碰撞，重点考查“碰撞过程”和“碰后运动”的分层建模。",
    "3": "对称电阻网络题。前两问以等势合并和递推不动点为主，第三问升级为节点电压与二阶差分方程，是从初等电路化简过渡到离散场方法的代表题。",
    "4": "带电粒子加速、碰撞输运与飞行器受力综合题。计算链条从单个离子的能量和动量出发，经电流换算为动量流率，最终连接推力、阻力、功率和升力门槛。",
    "5": "正弦交流稳态电路题。以串联谐振、共轭阻抗和相量叠加为核心，同时考查峰值、有效值与平均功率之间的关系。",
    "6": "热辐射形系数与热平衡题。先求局部点到三块板的辐射权重，再沿整板积分得到视因数，最后用斯忒藩—玻尔兹曼定律建立热平衡。",
    "7": "傅里叶光学与相衬成像题。利用离散空间频谱、小相位展开和像面干涉，把透明样品的相位信息转化为可测的强度对比度。",
    "8": "随机过程与统计物理综合题。第一问由对称跃迁主方程证明 $H$ 单调不增，第二问在归一化与平均能量约束下求稳定分布。",
}


PHYSICAL_IMAGE = {
    "1": "把运动看成三段抛物线与两个瞬时反射。质点模型中，地面只使竖直速度反向，墙面只使水平速度反向；实心球模型中，法向冲量负责反弹，切向冲量同时改变质心切向速度和角速度。",
    "2": "碰撞瞬间，哑铃获得质心平动和绕质心转动。碰后在质心参考系中，小球沿水平直线运动，哑铃则像一根不断转动的指针；第二次碰撞就是这条直线与有限杆段再次相交。",
    "3": "给 $A$、$O$ 两端加测试电压后，电势从端口沿圆环向两侧传播。对称节点等势，可折叠网络；一般情形中，相邻节点电势按固定递推关系衰减。",
    "4": "每个离子在一个平均自由程内从静止加速，碰撞时把动量交给中性空气，随后重新从静止加速。许多离子连续重复这一过程，形成稳定的动量流和宏观推力。",
    "5": "把各电流相量看成复平面上的箭头。电感支路电流位于实轴下方，电容支路电流位于实轴上方；当两箭头关于总电流对称时，它们的虚部抵消、实部相加。",
    "6": "从第 4 板上一点向内半空间发出的光线最终落到其余三板之一。位置越靠近左侧，第 1 板所张视野越大；位于中点时左右对称。整板视因数就是把每一点的这种分配沿板累加。",
    "7": r"第一透镜把样品分解成零级参考光和 $\pm k_*$ 侧带。相位板分别处理参考光与侧带，第二透镜再把它们叠加；亮暗来自复振幅干涉，而不是单个频谱斑自身的强弱。",
    "8": "把每个量子态看成一个概率容器，状态之间有双向概率流。若两态概率不同，较大概率一侧的流出更多，概率差逐渐缩小；$H$ 用来量化这种趋近平衡的过程。",
}


ENTRY = {
    "1": "先把未知初速度分解为水平分量 $u$ 和向下竖直分量 $w$，再引入落地前竖直速率 $q$。用同一高度对应的两个时刻写出 $l-x$ 与 $l+x$，这是消去轨迹细节的入口。",
    "2": r"先求质心位置和转动惯量，再把碰后状态压缩为三个未知量 $v$、$V_c$、$\omega$。依次写线动量、关于质心的角动量和机械能守恒。",
    "3": "在端口 $AO$ 接测试电压，先找等势点。能靠对称性折叠就先折叠；不能彻底折叠时，对任一普通节点列基尔霍夫电流方程。",
    "4": "始终从一个离子开始：先把摩尔质量换成单粒子质量，再用一个自由程内的电场功求碰前动量。之后才乘碰撞次数和单位时间离子数。",
    "5": "先准确识别 $U_0$ 所跨的前级串联段，写出该段阻抗 $Z_0$。第（2）问再从两支路电流相位对称推出两支路阻抗互为共轭。",
    "6": "先选第 4 板上一点 $P$，对目标板上的面积元写出源面余弦、接收面余弦和距离平方反比，再按轴向和横向依次积分。",
    "7": r"第一步不是做傅里叶积分，而是把余弦写成两个复指数。第（2）问只保留 $e^{i\varphi}$ 的一阶项，使零级和两个侧带直接显现。",
    "8": r"先按“流入减流出”写主方程并验证总概率守恒。求 $\dot H$ 时，关键操作是把原双重求和与交换 $i,j$ 后的式子相加取平均。",
}


INSIGHTS = {
    "1": [
        "弹性反射不必逐段重新求抛物线；利用速度分量反号和镜像法即可拼接整段运动。",
        "二次方程的代数根必须对应真实运动阶段，根的筛选属于物理推理的一部分。",
        "滑动摩擦方向由接触点相对速度决定，不能只看球心速度。",
    ],
    "2": [
        "偏心冲量同时产生质心平动和自转，以质心为矩心能把两种运动清楚分开。",
        "无限直线相交只是必要条件，交点还必须位于真实有限杆段上。",
        "临界参数通常对应端点接触或相切状态，可先求边界而不必先求全部运动时间。",
    ],
    "3": [
        "对称节点等势的前提是电路结构和端口激励同时保持对称。",
        "第（2）问的结果与 $N$ 无关，源于递推映射存在不动点 $r$。",
        "节点电压差分方程是连续场方程的离散版本，指数型解反映电势沿网络衰减。",
    ],
    "4": [
        "电流 $I$ 不是粒子数流率；单位时间离子数应为 $I/e$。",
        "力是动量变化率，因此必须先求单离子动量，再乘单位时间粒子数。",
        "最小驱动条件取约束等号，这是处理阈值与最优化问题的通用方法。",
    ],
    "5": [
        "$U_0$ 只跨前级串联段，因此第（1）问的谐振条件不依赖 $L_1$。",
        "相位对称不仅要求相角相反，还要求两支路电流模长相等；本题由共轭阻抗同时保证。",
        "峰值相量计算平均功率时必须出现 $1/2$，也可用各电阻焦耳热独立复核。",
    ],
    "6": [
        "局部权重之和恒定、整板视因数之和为 $1$，是比具体积分更重要的守恒约束。",
        "长管虽可画成二维截面，辐射仍分布在三维立体角中，不能省略轴向积分。",
        "热平衡平均的是 $T^4$ 对应的辐射功率，而不是温度本身。",
    ],
    "7": [
        "纯相位样品的信息已经存在于侧带，只是普通明场没有把它线性转成强度差。",
        "相位板把原本正交的扰动旋转到参考光方向，实现空间外差式读出。",
        "透镜线性处理的是复振幅，探测器测量的是复振幅模平方。",
    ],
    "8": [
        "跃迁系数对称不等于瞬时概率流相等，净流仍由两态概率差决定。",
        "交换求和指标并取平均，是把整体表达式改写成逐项可定号形式的核心技巧。",
        "对称主方程本身给出等概率稳态；玻尔兹曼形式还依赖平均能量约束的变分解释。",
    ],
}


EXTRA_VARIATION = {
    "1": "把地面碰撞的恢复系数改为 $e_1$、墙面碰撞的恢复系数改为 $e_2$。要求只建立分段方程，不必化到最终闭式。训练目标是区分“反向”和“大小保持”这两个条件。",
    "2": r"把入射小球质量 $80m$ 改为一般质量 $M$，重新写出三个守恒方程，并分别讨论 $M\gg5m$ 与 $M\ll5m$ 两个极限。",
    "3": "把圆环每段电阻改为 $R_s$、每根辐条电阻改为 $R_r$，写出一般特征方程，并判断特征根乘积为何等于 $1$。",
    "4": r"若碰撞后离子并非速度归零，而是保留碰前速度的固定比例 $\gamma$，建立单个自由程的递推关系，并讨论 $\gamma\to0$ 的退化。",
    "5": "若两并联支路中的电阻分别为 $R_1$、$R_2$，研究仅令两电抗绝对值相等是否仍能保证电流关于 $I_0$ 相位对称。",
    "6": "保持 $T_1=T_3=T$，令 $T_2$ 从 $T$ 缓慢升高。求 $T_4$ 对 $T_2$ 的变化率，并解释为什么高温板影响更强。",
    "7": "把零级振幅衰减系数从 $1/4$ 改为一般 $a$，推导对比度 $C(a)$，并求使对比度最大的 $a$。",
    "8": "先对两态系统直接解出 $p_1(t)$、$p_2(t)$，再代入 $H(t)$ 检查其单调性，用显式解验证一般证明。",
}


def between(text: str, start: str, end: str | None) -> str:
    a = text.find(start)
    if a < 0:
        raise RuntimeError(f"missing marker: {start}")
    a += len(start)
    if end is None:
        b = len(text)
    else:
        b = text.find(end, a)
        if b < 0:
            raise RuntimeError(f"missing marker: {end}")
    return text[a:b].strip()


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def main() -> None:
    source = PATH.read_text(encoding="utf-8")
    front_match = re.match(r"\A(---\n.*?\n---\n)", source, flags=re.S)
    if front_match is None:
        raise RuntimeError("missing front matter")
    front = front_match.group(1)
    body = source[front_match.end() :].lstrip()

    appendix_marker = "# 蔡题 101｜答案核验记录"
    appendix_at = body.find(appendix_marker)
    appendix = ""
    if appendix_at >= 0:
        appendix = body[appendix_at:].strip()
        body = body[:appendix_at].rstrip()

    problem_pattern = re.compile(
        r"(?m)^# 蔡题 101｜第 (\d+) 题（竞赛教学设计）\n"
    )
    matches = list(problem_pattern.finditer(body))
    if len(matches) != 8:
        raise RuntimeError(f"expected 8 problems, found {len(matches)}")

    preface = body[: matches[0].start()].strip()
    rebuilt: list[str] = []

    for index, match in enumerate(matches):
        number = match.group(1)
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        block = body[start:end].strip()
        block = re.sub(r"(?:\n\s*\\newpage\s*)+$", "", block).strip()

        module_one = between(
            block, "## 一、题目重构与考点分析", "## 二、教师用标准解答与推导"
        )
        question = between(module_one, "### 1. 题目文本", "### 2. 核心考点")
        knowledge = between(module_one, "### 2. 核心考点", None)

        solution = between(
            block, "## 二、教师用标准解答与推导", "## 三、学情诊断与易错辨析"
        )
        first_answer = re.search(r"(?m)^### 解答（", solution)
        if first_answer is None:
            raise RuntimeError(f"problem {number}: missing first answer")
        overview = between(
            solution[: first_answer.start()], "### 解题路线总览", None
        )
        analysis = solution[first_answer.start() :].strip()
        analysis = re.sub(r"(?m)^### 解答（", "### （", analysis)

        diagnostics = between(
            block, "## 三、学情诊断与易错辨析", "## 四、启发式教学活动设计"
        )
        foundation = between(
            diagnostics,
            "### 1. 高一新生的知识台阶",
            "### 2. 教练式引导与纠错话术",
        )
        diagnostic_tail = between(
            diagnostics, "### 2. 教练式引导与纠错话术", None
        )
        first_error = re.search(r"(?m)^- \*\*", diagnostic_tail)
        if first_error is None:
            raise RuntimeError(f"problem {number}: missing error list")
        guided_questions = diagnostic_tail[: first_error.start()].strip()
        error_and_diagnosis = diagnostic_tail[first_error.start() :].strip()
        diagnosis_marker = "**分层诊断建议：**"
        if diagnosis_marker not in error_and_diagnosis:
            raise RuntimeError(f"problem {number}: missing diagnosis marker")
        errors, layered_diagnosis = error_and_diagnosis.split(diagnosis_marker, 1)
        errors = errors.strip()
        layered_diagnosis = layered_diagnosis.strip()

        teaching = between(block, "## 四、启发式教学活动设计", None)
        flow = between(teaching, "### 1. 建议课堂流程", "### 2. 课堂引导问题")
        variations = between(teaching, "### 2. 课堂引导问题", None)

        new_block = f"""# 蔡题 101｜第 {number} 题（竞赛教学设计）

## 一、题型定位

### 题目

{question}

### 定位说明

{TYPE_POSITION[number]}

## 二、知识点

{knowledge}

## 三、物理图像

{PHYSICAL_IMAGE[number]}

## 四、解题入口

{ENTRY[number]}

{overview}

## 五、解析

{analysis}

## 六、关键洞察

{bullets(INSIGHTS[number])}

## 七、易错点

{errors}

## 八、课堂讲解建议

### 概念铺垫

{foundation}

### 讲解与纠错

{guided_questions}

### 分层处理

{layered_diagnosis}

### 课堂流程

{flow}

## 九、变式训练

### 基础变式

{variations}

### 进阶变式

{EXTRA_VARIATION[number]}"""
        rebuilt.append(new_block.strip())

    front = front.replace(
        "教师备课详解｜面向高一竞赛新生的循序讲解、完整推导与教学设计",
        "教师备课详解｜题型定位、物理图像、完整解析与变式训练",
    )
    preface = preface.replace(
        "# 教师使用导言｜面向高一竞赛新生的教学原则 {.unnumbered}",
        "# 教师使用导言｜循序讲解原则 {.unnumbered}",
    )
    result = (
        front
        + "\n"
        + preface
        + "\n\n\\newpage\n\n"
        + "\n\n\\newpage\n\n".join(rebuilt)
    )
    if appendix:
        result += "\n\n\\newpage\n\n" + appendix
    PATH.write_text(result.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
