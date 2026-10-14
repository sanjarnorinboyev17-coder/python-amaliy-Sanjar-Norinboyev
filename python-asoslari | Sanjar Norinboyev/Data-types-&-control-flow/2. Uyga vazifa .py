"""2.2 uyga vazifa: monitoring, closure va validatsiya."""

import re
from collections.abc import Callable


class InvalidServerNameError(Exception):
	"""Server nomi talab qilingan formatga mos kelmaganda chiqariladi."""


def print_down_servers(monitoring: dict[str, str]) -> None:
	"""Statusi down bo'lgan serverlarni chop etadi."""
	down_servers = [
		server_name
		for server_name, status in monitoring.items()
		if status == "down"
	]
	print(f"Ishlamayotgan serverlar: {down_servers}")


def make_status_checker(expected_status: str) -> Callable[[str], bool]:
	"""expected_status qiymatini closure ichida saqlovchi funksiya yaratadi."""

	def is_expected_status(current_status: str) -> bool:
		return current_status == expected_status

	return is_expected_status


def validate_server_name(server_name: str) -> str:
	"""Server nomi faqat harf, raqam va tirelardan iboratligini tekshiradi."""
	if not re.fullmatch(r"[A-Za-z0-9-]+", server_name):
		raise InvalidServerNameError(
			"Server nomi faqat harf, raqam va '-' belgilaridan iborat bo'lishi kerak."
		)
	return server_name


def validate_port(port_text: str) -> int:
	"""Portni butun son va 1-65535 oralig'ida ekanini tekshiradi."""
	try:
		port = int(port_text)
	except ValueError as error:
		raise ValueError("Port butun son bo'lishi kerak.") from error

	if not 1 <= port <= 65535:
		raise ValueError("Port 1 dan 65535 gacha bo'lishi kerak.")
	return port


def main() -> None:
	monitoring = {
		"web-server": "up",
		"database-server": "down",
		"cache-server": "down",
		"backup-server": "up",
	}
	print_down_servers(monitoring)

	divisible_by_three = [number for number in range(1, 51) if number % 3 == 0]
	print(f"1 dan 50 gacha 3 ga bo'linadigan sonlar: {divisible_by_three}")

	is_down = make_status_checker("down")
	down_count = sum(is_down(status) for status in monitoring.values())
	print(f"Closure orqali topilgan down serverlar soni: {down_count}")

	server_name = input("Server nomini kiriting: ")
	try:
		validate_server_name(server_name)
		print(f"Server nomi to'g'ri: {server_name}")
	except InvalidServerNameError as error:
		print(f"Server nomi xatosi: {error}")

	port_text = input("Port raqamini kiriting: ")
	try:
		port = validate_port(port_text)
		print(f"Port to'g'ri: {port}")
	except ValueError as error:
		print(f"Port xatosi: {error}")


if __name__ == "__main__":
	main()
