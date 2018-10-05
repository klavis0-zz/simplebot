import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def main():

    vk_session = vk_api.VkApi(token='')
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            text=event.text
            if text.lower() == 'привет':
                vk.messages.send(
                    peer_id=event.peer_id,
                    message='Привет!')

if __name__ == '__main__':
    main()
