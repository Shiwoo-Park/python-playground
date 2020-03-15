"""
<실행 방법>

python main.py input.txt
또는
python main.py < input.txt
"""
from typing import Dict, List

from soomgo_backend.helpers import CreditCard


def process_commands(command_lines: List[str]) -> Dict[str, CreditCard]:
    cards_info = {}

    for command_line in command_lines:
        line_words = command_line.split()
        command = line_words[0]

        if command == "Add":
            card = CreditCard(
                card_name=line_words[1],
                card_id=line_words[2],
                limit=line_words[3][1:]
            )
            cards_info[card.name] = card
        elif command == "Charge":
            _, card_name, amount = line_words
            if card_name in cards_info:
                cards_info[card_name].charge(amount[1:])
            else:
                # 해당하는 신용카드가 없습니다.
                pass
        elif command == "Credit":
            _, card_name, amount = line_words
            if card_name in cards_info:
                cards_info[card_name].credit(amount[1:])
            else:
                # 해당하는 신용카드가 없습니다.
                pass

    return cards_info


if __name__ == "__main__":

    import fileinput

    commands = []
    for line in fileinput.input():
        commands.append(line.strip())

    cards_info = process_commands(commands)
    for card_name, card_data in cards_info.items():
        if card_data.is_valid:
            print("{}: ${}".format(card_name, card_data.balance))
        else:
            print("{}: error".format(card_name))
