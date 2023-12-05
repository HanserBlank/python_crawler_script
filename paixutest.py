# 回答数据
answers = {
    '@dana25249': 52,
    '@MyraSapir': 35,
    '@prediction27051': 72,
    '@BeatriceBertie3': 25,
    '@hogan601599': 76,
    '@Fg6mvD46415': 35,
    '@CatherineFanny6': 38,
    '@BishopG32393966': 16,
    '@Bd19uW58789': 42,
    '@Valenti98437308': 26,
    '@AntoniaZachar15': 66,
    '@MaxwellKitto2': 37,
    '@LeifWalton6': 73,
    '@ward_doree57828': 28,
    '@zs2_y55239': 52,
    '@ArmstrongB68717': 64,
    '@holmes_rob55366': 76,
    '@3kadOv23846': 32,
    '@LauraCoffe20557': 23,
    '@burton_len86671': 82,
    '@eleanor_sp12364': 65,
    '@alberta660402': 16
}

# 目标值
target_value = 67

# 计算每个回答的差距
differences = {name: abs(value - target_value) for name, value in answers.items()}

# 找到差距最小的10个回答
closest_answers = sorted(differences.items(), key=lambda x: x[1])[:10]

# 输出结果
print("最接近67的10个回答：")
for name, value in closest_answers:
    print(f"{name} ")
