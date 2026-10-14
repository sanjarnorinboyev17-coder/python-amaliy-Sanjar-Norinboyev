"""2.1 amaliy vazifa: data types va control flow."""


def get_even_numbers(numbers: list[int]) -> list[int]:
	"""Ro'yxatdan juft sonlarni ajratib qaytaradi."""
	return [number for number in numbers if number % 2 == 0]


def sum_numbers_from_one_to_hundred() -> int:
	"""1 dan 100 gacha bo'lgan sonlar yig'indisini for bilan hisoblaydi."""
	total = 0
	for number in range(1, 101):
		total += number
	return total


def divide_numbers(dividend: float, divisor: float) -> float:
	"""Ikki sonni bo'ladi; nolga bo'lish xatosi chaqiruvchiga uzatiladi."""
	return dividend / divisor


def main() -> None:
	numbers = [3, 8, 11, 14, 17, 20, 25]
	even_numbers = get_even_numbers(numbers)
	print(f"Boshlang'ich ro'yxat: {numbers}")
	print(f"Juft sonlar: {even_numbers}")

	servers = {
		"web-server": "192.168.1.10",
		"database-server": "192.168.1.20",
		"backup-server": "192.168.1.30",
	}
	print("Serverlar va IP manzillar:")
	for server_name, ip_address in servers.items():
		print(f"{server_name}: {ip_address}")

	print(f"1 dan 100 gacha yig'indi: {sum_numbers_from_one_to_hundred()}")

	try:
		whole_number = int(input("Butun son kiriting: "))
		print(f"Siz {whole_number} sonini kiritdingiz.")
	except ValueError:
		print("Xatolik: iltimos, faqat butun son kiriting.")

	try:
		dividend = float(input("Bo'linuvchini kiriting: "))
		divisor = float(input("Bo'luvchini kiriting: "))
		result = divide_numbers(dividend, divisor)
		print(f"Bo'lish natijasi: {result}")
	except ValueError:
		print("Xatolik: bo'lish uchun son kiriting.")
	except ZeroDivisionError:
		print("Xatolik: sonni nolga bo'lish mumkin emas.")


if __name__ == "__main__":
	main()
