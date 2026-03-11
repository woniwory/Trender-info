import itertools
import statistics

# 데이터 정의
nums = [
    (1, 370), (2, 340), (3, 330), (4, 400), (5, 360),
    (6, 170), (7, 220), (8, 430), (9, 200), (10, 180),
    (11, 200), (12, 170), (13, 370), (14, 300)
]
target = 820

def calculate_score(selection, w1, w2, w3):
    deviations = [s['sum'] - target for s in selection]
    sum_d = sum(deviations)
    mean_d = sum_d / 4
    variance = sum((d - mean_d)**2 for d in deviations) / 4
    std_dev = variance ** 0.5
    total_items = sum(len(s['indices']) for s in selection)
    
    # Score calculation
    score = (w1 * sum_d) + (w2 * std_dev) + (w3 * total_items)
    return score, sum_d, std_dev, total_items

def solve():
    # 유효한 조합 생성
    valid_subsets = []
    for r in range(2, 6):
        for combo in itertools.combinations(nums, r):
            s = sum(x[1] for x in combo)
            if s >= target:
                valid_subsets.append({
                    'sum': s,
                    'indices': set(x[0] for x in combo),
                    'values': [x[1] for x in combo]
                })

    valid_subsets.sort(key=lambda x: x['sum'])

    # 시나리오 설정
    scenarios = [
        {"name": "근접도 우선형 (w1=0.7, w2=0.2, w3=0.1)", "w1": 0.7, "w2": 0.2, "w3": 0.1},
        {"name": "균등성 우선형 (w1=0.2, w2=0.7, w3=0.1)", "w1": 0.2, "w2": 0.7, "w3": 0.1},
        {"name": "아이템 최소화형 (w1=0.3, w2=0.2, w3=0.5)", "w1": 0.3, "w2": 0.2, "w3": 0.5},
    ]

    for sc in scenarios:
        w1, w2, w3 = sc["w1"], sc["w2"], sc["w3"]
        best_selection = None
        min_score = float('inf')
        best_stats = None

        # Search limit for reliable results in reasonable time
        def find_disjoint(current, used, start_idx):
            nonlocal best_selection, min_score, best_stats
            
            if len(current) == 4:
                score, s_d, s_v, t_i = calculate_score(current, w1, w2, w3)
                if score < min_score:
                    min_score = score
                    best_selection = list(current)
                    best_stats = (s_d, s_v, t_i)
                return

            limit = min(start_idx + 150, len(valid_subsets))
            for i in range(start_idx, limit):
                subset = valid_subsets[i]
                if subset['indices'].isdisjoint(used):
                    find_disjoint(current + [subset], used | subset['indices'], i + 1)

        find_disjoint([], set(), 0)
        
        print(f"\n[{sc['name']}]")
        if best_selection:
            best_selection.sort(key=lambda x: x['sum'])
            for i, item in enumerate(best_selection):
                indices = sorted(list(item['indices']))
                print(f"  조합 {i+1}: 합 {item['sum']} (번호: {indices}) | 식: {' + '.join(map(str, item['values']))}")
            s_d, s_v, t_i = best_stats
            print(f"  >> 분석: 오차합 {s_d}, 표준편차 {s_v:.2f}, 아이템수 {t_i}")
        else:
            print("  결과 없음")

if __name__ == "__main__":
    solve()
