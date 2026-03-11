import sys

nums = [
    (1, 370), (2, 340), (3, 330), (4, 400), (5, 360),
    (6, 170), (7, 220), (8, 430), (9, 200), (10, 180),
    (11, 200), (12, 170), (13, 370), (14, 300)
]
target = 820

scenarios = [
    ("균형형", 0.5, 0.3, 0.2),
    ("균등성 강조", 0.4, 0.5, 0.1),
    ("개수 최소 강조", 0.4, 0.2, 0.4)
]

def solve():
    # 5^14 is about 6M. Let's use a more targeted search.
    # Pre-generate valid subsets to drastically reduce the search space.
    import itertools
    
    valid_subsets = []
    for r in range(2, 8):
        for combo in itertools.combinations(nums, r):
            s = sum(x[1] for x in combo)
            if s >= target:
                valid_subsets.append({
                    'sum': s,
                    'indices': set(x[0] for x in combo),
                    'values': [x[1] for x in combo],
                    'count': r
                })
    
    # Sort to prune better
    valid_subsets.sort(key=lambda x: x['sum'])
    
    for name, w1, w2, w3 in scenarios:
        best_selection = None
        min_score = float('inf')

        # We can optimize the search by picking subsets one by one
        # but only considering the 'best' candidates.
        # However, for a true mathematical optimum, we need a broader search.
        
        def calculate_score(selection):
            deviations = [s['sum'] - target for s in selection]
            sum_d = sum(deviations)
            mean_d = sum_d / 4
            variance = sum((d - mean_d)**2 for d in deviations) / 4
            sum_n = sum(s['count'] for s in selection)
            return w1 * sum_d + w2 * variance + w3 * sum_n

        def find_optimal(current_selection, used_indices, start_idx):
            nonlocal best_selection, min_score
            
            if len(current_selection) == 4:
                score = calculate_score(current_selection)
                if score < min_score:
                    min_score = score
                    best_selection = list(current_selection)
                return

            # Search range: Limit the candidates to top N to avoid explosion
            # but N should be large enough to find the global optimum for variance
            search_limit = min(start_idx + 150, len(valid_subsets))
            for i in range(start_idx, search_limit):
                subset = valid_subsets[i]
                if subset['indices'].isdisjoint(used_indices):
                    find_optimal(current_selection + [subset], used_indices | subset['indices'], i + 1)

        find_optimal([], set(), 0)
        
        print(f"=== {name} 최적해 (w1={w1}, w2={w2}, w3={w3}) ===")
        if best_selection:
            best_selection.sort(key=lambda x: x['sum'])
            for i, item in enumerate(best_selection):
                idx_list = sorted(list(item['indices']))
                print(f"조합 {i+1}: 합계 {item['sum']} (번호: {idx_list}) / {item['count']}개 사용 / 식: {' + '.join(map(str, item['values']))}")
            
            all_used = set().union(*(s['indices'] for s in best_selection))
            remaining = [x for x in nums if x[0] not in all_used]
            print(f"남은 데이터: {', '.join(f'{x[0]}번({x[1]})' for x in remaining) if remaining else '없음'}")
            print(f"최종 Score: {min_score:.2f}")
        else:
            print("최적해를 찾지 못했습니다.")
        print("-" * 30)

if __name__ == "__main__":
    solve()
