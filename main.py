import vk_api
from random import randint
import time
import os
from console_ui import ConsoleUI


"""global"""
main_acc = ["", "", int()]
bot_accs = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]


def auth_handler():
    key = input("Enter auth code: ")
    return int(key), True


def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)


def ui():
    console_ui = ConsoleUI()
    default_msg = "Comment posted by AutolikeBot\n======CODED BY PFUB======="
    returned = console_ui.main_menu()
    message = input("Input message (if not, bot will use default message): ")
    data = returned
    if message:
        main(data, message)
    else:
        main(data, default_msg)


def bots_likes(log_pass_bot, profile_id, new_post_id, group):
    global vk_bot
    for i in log_pass_bot:
        login_bot, pass_bot = i[0], i[1]
        if login_bot == "":
            continue
        try:
            vk_session_bot = vk_api.VkApi(login=login_bot,
                                          password=pass_bot,
                                          auth_handler=auth_handler,
                                          captcha_handler=captcha_handler
                                          )
            vk_session_bot.auth()
            vk_bot = vk_session_bot.get_api()
        except vk_api.AuthError as exc:
            print(exc)
        try:
            comments = vk_bot.wall.getComments(
                owner_id=group,
                post_id=new_post_id,
                sort="desc"
            )
            comment_id = 0
            for j in range(len(comments["items"])):
                if comments["items"][j]["from_id"] == int(profile_id):
                    comment_id = comments["items"][j]["id"]
                    break
            vk_bot.likes.add(
                type="comment",
                owner_id=group,
                item_id=comment_id
            )
            print("Лайк на коммент успешно поставлен")
        except vk_api.VkApiError as exc:
            print(exc)
        vk_session_bot, vk_bot = None, None
    return


def main_account_send(login, password, group, new_post_id, message):
    global vk
    try:
        vk_session = vk_api.VkApi(login=login,
                                  password=password,
                                  auth_handler=auth_handler,
                                  captcha_handler=captcha_handler
                                  )
        vk_session.auth()
        vk = vk_session.get_api()
    except vk_api.AuthError as exc:
        print(exc)
    try:
        vk.likes.add(
            type="post",
            owner_id=group,
            item_id=new_post_id
        )
        print("Пост успешно лайкнут")
    except Exception as exc:
        print(exc)
        return
    try:
        vk.wall.createComment(
            owner_id=group,
            post_id=new_post_id,
            message=message,
            random_id=randint(0, 2 ** 64)
        )
        print("Комментарий успешно написан")
    except Exception as exc:
        print(exc)
        return
    return


def main(data, msg):
    global vk, vk_bot, main_acc

    """
                                              ==============
                                              |  Настройки |
                                              ==============
    """
    message = msg    # сюда вписать шаблонное сообщение
    login, password, profile_id = data[0][0], data[0][1], data[0][2]  # сюда вхуячиваешь логин (номер телефона)
    log_pass_bot = data[1:]
    group = -170524888  # -181348137 - winstrike    id группы

    """
                                              ==============
                                              |  Алгоритм  |
                                              ==============
                                              Не лезь - убьет!
    """
    try:
        vk_session = vk_api.VkApi(login=login,
                                  password=password,
                                  auth_handler=auth_handler,
                                  captcha_handler=captcha_handler
                                  )
        vk_session.auth()
        vk = vk_session.get_api()
    except vk_api.AuthError as exc:
        print(exc)
    last_post_date = 0
    while True:
        try:
            posts = vk.wall.get(
                owner_id=group
            )
            new_post_date = posts["items"][0]["date"]
            new_post_id = posts["items"][0]["id"]
            if last_post_date < new_post_date:
                print(f"Вышел новый пост от {time.ctime(new_post_date)}")
                last_post_date = new_post_date
                main_account_send(login, password, group, new_post_id, message)
                bots_likes(log_pass_bot, profile_id, new_post_id, group)
        except vk_api.VkApiError as exc:
            print("Error:", exc)
        time.sleep(1)


if __name__ == "__main__":
    ui()
