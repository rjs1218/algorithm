'''
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
'''

kg = int(input())   # 설탕 kg 입력받기
count = 0           # 봉지 개수

# kg에 맞는 최소 봉지 개수 찾기
while True:
    if kg%5 == 0:   # 5로 나눠진다면 5kg 봉지에 넣기
        kg -= 5
        count += 1
    
    # 5로 안 나눠지고 3으로 나눠진다면 3kg 봉지에 넣기
    elif kg%5 != 0 and kg%3 == 0:
        kg -= 3
        count += 1

    elif kg%5 !=0:  # 일단 5kg 봉지에 넣어봄
        kg -= 5
        count += 1

    if kg == 0:     # 0kg이라면 멈추기
        break

    if kg < 3:
        count = -1  # 상근이가 가지고 있는 봉지로 정확하게 kg을 만들 수 없는 경우
        break

print(count)
