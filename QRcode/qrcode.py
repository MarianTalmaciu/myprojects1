import qrcode

img = qrcode.make('https://www.youtube.com/@Qatar2022')

img.save('qatar2002youtubeqrcode.jpg')

