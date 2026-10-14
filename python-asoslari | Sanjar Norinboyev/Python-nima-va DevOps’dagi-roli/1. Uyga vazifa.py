"""1.2 uyga vazifa: subcommands bilan oddiy CLI."""

import argparse
from pathlib import Path


def write_status(status_file: Path, status: str) -> None:
	status_file.write_text(status + "\n", encoding="utf-8")
	print(f"Xizmat holati: {status}")


def main() -> None:
	parser = argparse.ArgumentParser(description="Xizmatni boshqarish CLI")
	parser.add_argument(
		"--state-file",
		type=Path,
		default=Path("service_status.txt"),
		help="Holat yoziladigan fayl (standart: service_status.txt)",
	)
	commands = parser.add_subparsers(dest="command", required=True)

	commands.add_parser("start", help="Xizmatni ishga tushirish")
	commands.add_parser("stop", help="Xizmatni to'xtatish")

	args = parser.parse_args()

	if args.command == "start":
		write_status(args.state_file, "running")
	elif args.command == "stop":
		write_status(args.state_file, "stopped")


if __name__ == "__main__":
	main()
