import itertools

nums = [
    (1, 370), (2, 340), (3, 330), (4, 400), (5, 360),
    (6, 170), (7, 220), (8, 430), (9, 200), (10, 180),
    (11, 200), (12, 170), (13, 370), (14, 300)
]
target = 820

def solve():
    valid_subsets = []
    # Generate all subsets with sum >= 820 and length between 2 and 7
    for r in range(2, 8):
        for combo in itertools.combinations(nums, r):
            s = sum(x[1] for x in combo)
            if s >= target:
                indices = sorted(x[0] for x in combo)
                values = [x[1] for x in combo]
                valid_subsets.append({'sum': s, 'indices': indices, 'values': values})

    # Sort subsets by sum to prioritize those closest to 820
    valid_subsets.sort(key=lambda x: x['sum'])

    best_selection = None
    min_total_sum = float('inf')

    # Recursive search with higher limit
    def find_disjoint(current_selection, used_indices, start_idx):
        nonlocal best_selection, min_total_sum
        
        if len(current_selection) == 4:
            total = sum(x['sum'] for x in current_selection)
            if total < min_total_sum:
                min_total_sum = total
                best_selection = list(current_selection)
                if min_total_sum == 3280: # 820 * 4
                    return True
            return False

        # No limit for exhaustive search on 14 items
        for i in range(start_idx, len(valid_subsets)):
            subset = valid_subsets[i]
            
            # Pruning based on sorting
            current_sum = sum(x['sum'] for x in current_selection)
            remaining = 4 - len(current_selection)
            if current_sum + subset['sum'] + (remaining - 1) * target >= min_total_sum:
                break

            subset_indices = set(subset['indices'])
            if subset_indices.isdisjoint(used_indices):
                if find_disjoint(current_selection + [subset], used_indices | subset_indices, i + 1):
                    return True
        return False

    find_disjoint([], set(), 0)
    
    if best_selection:
        # Sort selection by sum for pretty printing
        best_selection.sort(key=lambda x: x['sum'])
        
        used_indices = set()
        for item in best_selection:
            used_indices.update(item['indices'])
            
        remaining = [x for x in nums if x[0] not in used_indices]
        
        print("최적 조합 결과 (각 조합별 최소 2개 이상 선택):")
        for i, item in enumerate(best_selection):
            indices_str = ", ".join(map(str, item['indices']))
            formula = " + ".join(map(str, item['values']))
            print(f"{i+1}. {item['sum']} (번호: {indices_str}) / 식: {formula} = {item['sum']}")
            
        print("\n남은 데이터:")
        if remaining:
            rem_str = ", ".join(f"{x[0]}번({x[1]})" for x in remaining)
            print(f"- {rem_str}")
        else:
            print("- 없음")
            
        print(f"\n총합 최적화 결과: {sum(x['sum'] for x in best_selection)} (820x4 대비 +{sum(x['sum'] for x in best_selection)-3280})")
    else:
        print("조건을 만족하는 4개의 조합을 찾을 수 없습니다.")

solve()
