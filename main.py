import Weather
import MP3

def main():
    weather = Weather.Weather("http://tj.nineton.cn/Heart/index/all?city=CHSN000000")
    content = weather.getData()
    mp3 = MP3.MP3('IEqP5sQIhGSiVGyzGy6FjnwZ', 'nWeh0xWjaUBFPILiAqB3PZDqmK4uWDOr', content)
    if (mp3.getMP3()):
        mp3.playmusic()

if __name__ == '__main__' :
    main()


