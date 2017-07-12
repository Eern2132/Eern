#!/usr/bin/env python3

import pytest
import poll_bot

class TestPollBot:

	def test_extract_emoji(self):
		lines_and_emojis = {
			' M)-ystery meat': 'M',
			'🐕 dog sandwiches': '🐕',
			'3 blind mice': '3',
			'🇺🇸 flags': '🇺🇸',
			'<:python3:232720527448342530> python3!': '<:python3:232720527448342530>',
		}
		
		for input, output in lines_and_emojis.items():
			assert poll_bot.extract_emoji(input) == output
	
	
	def test_emojify(self):
		# custom emoji extraction is the only feature unique to emojify()
		# so we'll test the other functionality in other tests
		assert poll_bot.emojify('<:python3:232720527448342530>') == ':python3:232720527448342530'