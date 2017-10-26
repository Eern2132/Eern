#!/usr/bin/env python3

import reactor_bot

import datetime
from freezegun import freeze_time

class TestReactorBot:

	def test_extract_emoji(self):
		lines_and_emojis = {
			' M)-ystery meat': 'M',
			'🐕 dog sandwiches': '🐕',
			'3 blind mice': '3',
			'🇺🇸 flags': '🇺🇸',
			'<:python3:232720527448342530> python3!': '<:python3:232720527448342530>',
		}

		for input, output in lines_and_emojis.items():
			assert reactor_bot.extract_emoji(input) == output


	def test_emojify(self):
		assert reactor_bot.emojify('<:python3:232720527448342530>') == ':python3:232720527448342530'
		assert reactor_bot.emojify('a') == '🇦'
		# this one's wonky--sometimes we return invalid emoji,
		# but that's ok, because Discord throws them out with an error ;)
		assert reactor_bot.emojify('123') == '123⃣'
		assert reactor_bot.emojify('0') == '0⃣'
		assert reactor_bot.emojify('6') == '6⃣'
		assert reactor_bot.emojify('asdfghjkl;') == 'asdfghjkl;'


	def test_get_letter_emoji(self):
		io_map = {
			'A': '🇦',
			'B': '🇧',
			'C': '🇨',
			'D': '🇩',
			'E': '🇪',
			'F': '🇫',
			'G': '🇬',
			'H': '🇭',
			'I': '🇮',
			'J': '🇯',
			'K': '🇰',
			'L': '🇱',
			'M': '🇲',
			'N': '🇳',
			'O': '🇴',
			'P': '🇵',
			'Q': '🇶',
			'R': '🇷',
			'S': '🇸',
			'T': '🇹',
			'U': '🇺',
			'V': '🇻',
			'W': '🇼',
			'X': '🇽',
			'Y': '🇾',
			'Z': '🇿'
		}

		# one of these tests will fail on april fools
		# (hint: it's "B")
		# unless we force the date to not be april fools
		with freeze_time("2018-01-01"):
			for input, output in io_map.items():
				assert reactor_bot.get_letter_emoji(input) == output

		with freeze_time("2018-04-01"):
			assert reactor_bot.get_letter_emoji('B') == '🅱'

	def test_get_digit_emoji(self):
		io_map = {
			'0': '0⃣',
			'1': '1⃣',
			'2': '2⃣',
			'3': '3⃣',
			'4': '4⃣',
			'5': '5⃣',
			'6': '6⃣',
			'7': '7⃣',
			'8': '8⃣',
			'9': '9⃣',
		}

		for input, output in io_map.items():
			assert reactor_bot.get_digit_emoji(input) == output


	def test_april_fools(self):
		with freeze_time("2017-10-31"):
			assert not reactor_bot.april_fools()
		with freeze_time("2018-04-01"):
			assert reactor_bot.april_fools()