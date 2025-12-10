import logging

from extract.card import extract_card
from parse_args import parse_args


def main():
    context = parse_args()
    for card_id in context.card_ids:
        try:
            extract_card(context, card_id)
        except Exception as e:
            logging.critical(f'Card({card_id}) 解析失败： {str(e)}', exc_info=True)


if __name__ == '__main__':
    main()
