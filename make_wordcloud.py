from wordcloud import WordCloud

import log_handler as lh

default_wordcloud = WordCloud(width=1080,
                              height=640,
                              font_path='fonts/NanumGothic.ttf')


def make_wordcloud(chat_log_text: str) -> None:
    wordcloud = default_wordcloud.generate(chat_log_text)
    image = wordcloud.to_image()
    image.show()


if __name__ == '__main__':
    chat_log_file = lh.find_log_file()

    log_reader = lh.get_log_reader(chat_log_file)
    log_data = lh.read_all_log(log_reader)

    user_log_string = lh.get_user_log_string(log_data)
    message_log_string = lh.get_message_log_string(log_data)

    make_wordcloud(user_log_string)
    make_wordcloud(message_log_string)
