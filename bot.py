import telebot
import datetime
import feedparser

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['movies', 'help'])
def send_time(message):
	bluray_rss_feed = 'http://www.scnsrc.me/category/films/bluray/feed/'
	feed = feedparser.parse( bluray_rss_feed )
	movies = []
	for i in range(10):
		movies.append(feed[ 'entries' ][i]['title'])
	movie_message = '{}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n'.format(movies[0], movies[1], movies[2], movies[3], movies[4], movies[5], movies[6], movies[7], movies[8], movies[9])
	bot.reply_to(message, movie_message)


bot.polling()