



class Scoring(object):

    def __init__(self, ID, username, applytime, isscored, scoringtime, result, score,  ispublish, judge):
        self.ID = ID
        self.username = username
        self.applytime = applytime
        self.isscored = isscored
        self.scoringtime = scoringtime
        self.result = result
        self.score = score
        self.judge = judge
        print(type(ispublish))
        print("ispublic值：", ispublish)
        if ispublish == 1:
            self.ispublish = "是"
        else:
            self.ispublish = "否"

    def __str__(self) -> str:
        return "ID:" + str(self.ID) + ",  username :" + self.username + ", applytime: " + self.applytime + ", isscored: " + self.isscored
        # ", scoringtime:" + self.scoringtime + ", result： " + self.result + ", score: " + str(self.score) + ", judge:" + str(self.judge) + ", is publish: " + str(self.ispublish)



