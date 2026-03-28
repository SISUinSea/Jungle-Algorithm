"""
[그리디 알고리즘 - 거스름돈]

문제 설명:
- 그리디(Greedy) 알고리즘으로 거스름돈을 계산합니다.
- 가장 큰 단위의 동전부터 사용하여 최소 개수로 거슬러줍니다.
- 매 순간 최선의 선택(가장 큰 동전)을 합니다.

입력:
- change: 거슬러줄 금액
- coins: 사용 가능한 동전 종류 (예: [500, 100, 50, 10])

출력:
- 필요한 동전의 개수
- 각 동전의 사용 개수

예제:
입력: change = 1260, coins = [500, 100, 50, 10]
출력:
500원: 2개
100원: 2개
50원: 1개
10원: 1개
총 6개

힌트:
- 큰 동전부터 사용
- 현재 동전으로 최대한 거슬러주기
- 나머지 금액으로 다음 동전 사용
"""

"""
# [문제명]

- 날짜: 2026-03-27
- 분류: Greedy
- 체감 난이도: 매우 쉬움, 실수 많았음.
- 결과: 자력 해결 

## 1. 문제를 어떻게 정의했나
- 이 문제의 본질을 나는 어떻게 이해했는가?

## 2. 처음 접근
- 처음엔 왜 DP라고 생각했나? / 왜 Greedy라고 생각했나?
- 처음 떠올린 방법은 무엇이었나?

## 3. 막힌 지점
- 어디서 막혔나?
- 문제 이해 / 상태 정의 / 점화식 / Greedy 성립 판단 / 구현 중 어디였나?

## 4. 전환점
- 무엇을 깨닫고 방향이 바뀌었나?

## 5-B. Greedy 설계
- 선택 기준:
- 정렬 기준:
- 왜 이 선택이 성립한다고 생각했나:
- 시간복잡도:

## 6. 구현에서 한 실수
- 실수 투성이였다... 누더기처럼 기운 코드로 통과했다.
- 1. for loop 안에서 change를 줄여나가는 코드를 깜빡했다.
- 2. 명세에 나온 없는 동전은 출력하지 않아야 하고, dict에 넣으면 안 된다는 조건도 보지 못했다.
    2.1 근데 그것을 처리하기 위한 조건문으로 change == 0인 경우, continue(?) 하도록 했다.
- 예: 초기값 설정 오류
- 예: 인덱스 범위 실수
- 예: 정렬 기준 실수
- 예: tie-breaking 누락

## 7. 검산 / 반례
- 작은 입력으로 직접 검산한 과정:
- 내가 생각한 반례 1:
- 반례 2:
- 반례 3:

## 8. 다시 만나면 쓸 규칙
- 다음 비슷한 문제에서 바로 떠올릴 한 문장
- 의사코드를 만들어놓고 구현을 시작한다 해서, 그렇게까지 느리지는 않을 것 같은데...?

## 9. 남은 질문
- 아직 찝찝한 점
"""

def make_change_greedy(change, coins):
    """
    그리디 알고리즘으로 거스름돈 계산
    
    Args:
        change: 거슬러줄 금액
        coins: 동전 종류 리스트 (큰 순서)
    
    Returns:
        (총 개수, {동전: 개수} 딕셔너리)
    """
    result = {}
    total_coins = 0
    
    for coin in coins:
        coin_count = (change // coin)
        if coin_count == 0: continue
        change = change % coin
        total_coins += coin_count
        result[coin] = coin_count
    
    return total_coins, result

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    change1 = 1260
    coins1 = [500, 100, 50, 10]
    total, details = make_change_greedy(change1, coins1)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change1}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 2
    change2 = 4570
    coins2 = [500, 100, 50, 10]
    total, details = make_change_greedy(change2, coins2)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change2}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 3
    change3 = 1000
    coins3 = [500, 100, 50, 10]
    total, details = make_change_greedy(change3, coins3)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change3}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")


