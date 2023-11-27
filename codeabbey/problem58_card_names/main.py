def solve(suits, ranks, _):
	suit_value = suits[_ // 13]
	rank_value = ranks[_ % 13]
	return f"{rank_value}-of-{suit_value}"

def start(suits, ranks):
	n = int(input().strip())
	nums = list(map(lambda n: int(n.strip()), input().strip().split()))
	for _ in nums:
		print(solve(suits, ranks, _), end=' ')

def init():
	suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
	return suits, ranks

if __name__ == '__main__':
	suits, ranks = init()
	start(suits, ranks)
