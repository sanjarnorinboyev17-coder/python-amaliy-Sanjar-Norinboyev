"""1-mavzu amaliy vazifalari.

Skript ism bilan salomlashadi va berilgan papkadagi oddiy fayllar sonini sanaydi.
"""

import argparse
from pathlib import Path


def count_files(directory: Path) -> int:
	"""Papkaning ichidagi oddiy fayllar sonini qaytaradi."""
	return sum(path.is_file() for path in directory.iterdir())


def main() -> None:
	parser = argparse.ArgumentParser(description="Python amaliy vazifalari")
	parser.add_argument(
		"--name",
		default="Dunyo",
		help="Salomlashiladigan ism (standart: Dunyo)",
	)
	parser.add_argument(
		"--directory",
		type=Path,
		default=Path("."),
		help="Fayllari sanaladigan papka (standart: joriy papka)",
	)
	args = parser.parse_args()

	if not args.directory.is_dir():
		parser.error(f"Papka topilmadi: {args.directory}")

	print(f"Salom, {args.name}!")
	print(f"'{args.directory}' papkasida {count_files(args.directory)} ta fayl bor.")


if __name__ == "__main__":
	main()
