import itertools

nums = [
    (1, 370), (2, 340), (3, 330), (4, 400), (5, 360),
    (6, 170), (7, 220), (8, 430), (9, 200), (10, 180),
    (11, 200), (12, 170), (13, 370), (14, 300)
]
target = 820

# Fix the first combination as requested: 4번 + 8번
fixed_indices = {4, 8}
fixed_values = [400, 430]
fixed_sum = sum(fixed_values)

remaining_nums = [x for x in nums if x[0] not in fixed_indices]

def solve():
    valid_subsets = []
    # Generate valid subsets from remaining numbers (count >= 2, sum >= 820)
    for r in range(2, 7):
        for combo in itertools.combinations(remaining_nums, r):
            s = sum(x[1] for x in combo)
            if s >= target:
                valid_subsets.append({
                    'sum': s,
                    'indices': sorted(x[0] for x in combo),
                    'values': [x[1] for x in combo]
                })

    valid_subsets.sort(key=lambda x: x['sum'])

    best_selection = None
    min_total_sum = float('inf')

    def find_disjoint(current_selection, used_indices, start_idx):
        nonlocal best_selection, min_total_sum
        
        # We need 3 more combinations (to make 4 total)
        if len(current_selection) == 3:
            total = sum(x['sum'] for x in current_selection)
            if total < min_total_sum:
                min_total_sum = total
                best_selection = list(current_selection)
                if min_total_sum == target * 3:
                    return True
            return False

        for i in range(start_idx, len(valid_subsets)):
            subset = valid_subsets[i]
            
            # Pruning
            current_sum = sum(x['sum'] for x in current_selection)
            remaining_needed = 3 - len(current_selection)
            if current_sum + subset['sum'] + (remaining_needed - 1) * target >= min_total_sum:
                break

            if set(subset['indices']).isdisjoint(used_indices):
                if find_disjoint(current_selection + [subset], used_indices | set(subset['indices']), i + 1):
                    return True
        return False

    find_disjoint([], set(), 0)
    
    # Prepend the fixed combination
    final_selection = [{
        'sum': fixed_sum,
        'indices': sorted(list(fixed_indices)),
        'values': fixed_values
    }]
    if best_selection:
        final_selection.extend(best_selection)
        
        print("최적 조합 결과 (4번+8번 고정 및 3개 추가 조합):")
        for i, item in enumerate(final_selection):
            indices_str = ", ".join(map(str, item['indices']))
            formula = " + ".join(map(str, item['values']))
            status = " (고정)" if i == 0 else ""
            print(f"{i+1}. {item['sum']} (번호: {indices_str}){status} / 식: {formula} = {item['sum']}")
            
        used_all = set()
        for item in final_selection: used_all.update(item['indices'])
        remaining = [x for x in nums if x[0] not in used_all]
        
        print("\n남은 데이터:")
        if remaining:
            rem_str = ", ".join(f"{x[0]}번({x[1]})" for x in remaining)
            print(f"- {rem_str}")
        else:
            print("- 없음")
            
        total_score = sum(x['sum'] for x in final_selection)
        print(f"\n최적화 총합: {total_score} (820x4 대비 +{total_score - 3280})")
    else:
        print("고정 조건을 포함하여 4개의 조합을 완성할 수 없습니다.")

if __name__ == "__main__":
    solve()
