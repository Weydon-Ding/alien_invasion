class GameStats():
	'''跟踪游戏的统计信息'''
	
	def __init__(self,ai_settings):
		'''初始化统计信息'''
		self.ai_settings = ai_settings
		self.reset_stats()
		# 游戏刚启动时处于非活动状态
		self.game_active = False
		self.high_score = self.read_high_score(ai_settings)
		
	def read_high_score(self,ai_settings):
		'''读取合理的最高得分数据'''
		filename = ai_settings.filename
		# 从本地读取最高分
		try:
			with open(filename) as file_object:
				high_score_str = file_object.read()
		except FileNotFoundError:
			with open(filename,'w') as file_object:
				file_object.write('0')
				high_score_str = '0'
		# 检验数据类型
		try:
			high_score = int(high_score_str)
		except ValueError:
			with open(filename,'w') as file_object:
				file_object.write('0')
			return 0
		else:
			return high_score
		
	def reset_stats(self):
		'''初始化在游戏运行期间可能变化的统计信息'''
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
