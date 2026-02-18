
def format_message(dist_num, dist_list, info_list):
    head = '📌 ' + f'<b>{dist_list[dist_num - 1].upper()}</b>' + ' <b>РАЙОН</b>\n'
    original_info = info_list[0][dist_num-1] #обязательно [0]
    formatted_info = []
    for i in range(len(original_info)):
        if 'Дата и время начала отключения' in original_info[i]:
            formatted_info.append('\n⏳ <u>ВРЕМЯ ОТКЛЮЧЕНИЯ</u>\nНачало:\n')
            formatted_info.append(original_info[i+1][:11]+'| '+original_info[i+1][11:] + '\n')
            formatted_info.append('Окончание:\n')
            formatted_info.append(original_info[i+3][:11]+'| '+original_info[i+3][11:] + '\n\n')
            formatted_info.append('📋 <u>ТИП ОТКЛЮЧЕНИЯ</u>\n')
            if original_info[i+5] == 'Плановое': formatted_info.append('✅ Плановое\n\n')
            else: formatted_info.append('📛 Аварийное\n\n')
            formatted_info.append('🏠 <u>ОТКЛЮЧЕННЫЕ ДОМА</u>\n')
        elif 'улица' in original_info[i] or 'проспект' in original_info[i] or 'шоссе' in original_info[i]:
            formatted_info.append('‣ ' + original_info[i] + '\n')
            if original_info[i + 1] != original_info[-1]:
                formatted_info.append(original_info[i + 1] + '\n')
            else:
                formatted_info.append(original_info[i + 1] + '\n')
    end = '\nБолее подробную информацию можно найти на муниципальном портале г. Новосибирска:'
    message_listed = [head] + formatted_info + [end]
    print(''.join(message_listed))
    return ''.join(message_listed)
