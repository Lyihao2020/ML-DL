# 练习

def make_album(singer, name, number=''):
    album = {'singer': singer, 'name': name}
    if number:
        album['number'] = number
    return album

albums = []

while True:
    print('\nEnter \'q\' to quit anytime.')
    singer = input('Please tell me the singer: ')
    if singer == 'q':
        break

    name = input('Please tell me the name of this album: ')
    if name == 'q':
        break

    test = input('Do you want add the numbers of this album? (yes / no) ')
    if test.lower() == 'yes':
        number = input('Please tell me the number of this album: ')
        if number.isdigit():
            album = make_album(singer, name, number)
            albums.append(album)
        else:
            print('Invalid input. Please enter a number.')
    elif test.lower() == 'no':
        album = make_album(singer, name)
        albums.append(album)
    elif test.lower() == 'q':
        break

    continue_test = input('Continue? (yes / no) ')
    if continue_test.lower() == 'no' or continue_test.lower() == 'q':
        break

if albums:
    print('\nAlbums are as followed.')
    for album in albums:
        album_info = ', '.join(f'{key}: {value}' for key, value in album.items() if value)
        print(f'\t{album_info}')
else:
    print('\nAlbums are empty. Please add.')