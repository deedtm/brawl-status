import brawlstats
import vk_api
from time import sleep
from tokens import bs_token, mytoken
from random import choice


def main():
    vk_session = vk_api.VkApi(token=mytoken)
    vk = vk_session.get_api()
    counter = 1
    emoji_counter = 0
    emojis = ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚']
    while True:
        try:
            try:
                client = brawlstats.Client(token=bs_token, timeout=10)
                player = client.get_profile('89P00L8UG')

                trophies = player.trophies
                # highest_trophies = player.highest_trophies
                brawlers = player.brawlers
                brawlers_amount = len(brawlers)
                x3v3_victories = player.x3vs3_victories
                solo_victories = player.solo_victories
                duo_victories = player.duo_victories

                random_brawler = choice(brawlers)

                if emoji_counter <= 11:
                    emoji = emojis[emoji_counter]
                else:
                    emoji_counter = 0
                    emoji = emojis[emoji_counter]

                status_text = f'{trophies} 🏆 | '
                status_text += f'🛡 {x3v3_victories} | '
                status_text += f'🗡 {solo_victories} | '
                status_text += f'⚔️ {duo_victories} | '
                status_text += f'{brawlers_amount} 👥 | '
                status_text += f"{emoji} {random_brawler['name']} — {random_brawler['trophies']} | "
                vk.status.set(text=status_text)

            except brawlstats.errors.Forbidden as invalid_api:
                print(invalid_api)
        except vk_api.exceptions.Captcha as captcha:
            print('-------------------[ ⏬ КАПЧА ⏬ ]-------------------')
            print(captcha.sid)
            print(captcha.get_image())
            print(captcha.get_url())
            print('-------------------[ ⏫ КАПЧА ⏫ ]-------------------')
            sleep(120)

        my_status = vk.status.get(user_id='402806692')['text']
        print(f'вывод статуса номер {counter} - {my_status}')

        sleep(60)
        counter += 1
        emoji_counter += 1


if __name__ == '__main__':
    main()
