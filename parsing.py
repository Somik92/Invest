from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import investpy
import datetime
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

font_stock = ImageFont.truetype('/Users/somik/Desktop/Telegram/exljbris - Museo Cyrl 300.otf', size=45)
font_quotes = ImageFont.truetype('/Users/somik/Desktop/Telegram/exljbris - Museo Cyrl 300.otf', size=40)
font_time = ImageFont.truetype('/Users/somik/Desktop/Telegram/exljbris - Museo Cyrl 100.otf', size=30)
font_quote = ImageFont.truetype('/Users/somik/Desktop/Telegram/exljbris - Museo Cyrl 300.otf', size=23)
im = Image.new('RGB', (1100,450), color=('#000000'))
draw_text = ImageDraw.Draw(im)



def get_data(ticker, country, column):
    df = investpy.get_index_recent_data(ticker,country)
    df['Close'] =df['Close'].astype(float, round(2))
    df['High'] = df['High'].astype(float, round(2))
    df['Low'] = df['Low'].astype(float, round(2))
    df['Open'] = df['Open'].astype(float, round(2))
    df['change'] = df['Close'][-1] - df['Close'][-2]
    df['change'] = round(df['change'], 3)

    df['percent'] = df['change'] / df['Close'][-1] * 100
    df['percent'] = round(df['percent'], 3)


    return str(list(df.last('1D')[column])).replace('[', '').replace(']', '')

def line(dlina, shirina, colour):
    green_line = Image.open('/Users/somik/Desktop/Telegram/'+colour+'_line.png').convert("RGBA")
    im.paste(green_line, (dlina, shirina), green_line)
def usa(dlina, shirina):
    usa = Image.open('/Users/somik/Desktop/Telegram/usa120.png').convert("RGBA")
    im.paste(usa, (dlina, shirina), usa)
def text(text, dlina, shirina, colour, font):
    draw_text.text(
        (dlina, shirina),
        text,
        # Добавляем шрифт к изображению
        font=font,
        fill=colour)



line(50, 100, 'green')
line(50, 200, 'red')
line(50, 300, 'purple')

usa(350, 83)
usa(350, 183)
usa(350, 283)

text('S&P500', 83, 115,'#000000', font_stock)
text('Dow Jones', 83, 215, '#000000', font_stock)
text('Nasdaq', 83, 315, '#000000', font_stock)
text(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 50, 30, '#FFFFFF', font_time)



text(get_data('S&P 500', 'United States', 'Close'), 483, 120, '#000000', font_quotes)
text(get_data('Dow 30', 'United States', 'Close'), 483, 220, '#000000', font_quotes)
text(get_data('Nasdaq', 'United States', 'Close'), 483, 320, '#000000', font_quotes)

text(get_data('S&P 500', 'United States', 'change'), 710, 120, '#000000', font_quotes)
text(get_data('Dow 30', 'United States', 'change'), 710, 220, '#000000', font_quotes)
text(get_data('Nasdaq', 'United States', 'change'), 710, 320, '#000000', font_quotes)


text(get_data('S&P 500', 'United States', 'percent')+ '%', 900, 120, '#000000', font_quotes)
text(get_data('Dow 30', 'United States', 'percent') + '%', 900, 220, '#000000', font_quotes)
text(get_data('Nasdaq', 'United States', 'percent') + '%', 900, 320, '#000000', font_quotes)


im.show()
im.save('/Users/somik/Desktop/Telegram/index/index_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '.png')