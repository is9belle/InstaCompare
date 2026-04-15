import sys

# check for filename arguments as input
#if len(sys.argv) < 3:
#   print("Error: Usage: python instagramCompare.py <following_file> <followers_file>")
#   sys.exit(1)

following_file = "C:\\instagram\\following.json"
followers_file = "C:\\instagram\\followers_1.json"

file_following = open(following_file, "r")
file_followers = open(followers_file, "r")

followingList = []
followerList = []
notFollowingMeBack = []
notFollowingThemBack = []
okWithNot = ["4mybelly", "aztecblockchaingroup", "sdsuaiclub", "same.sdsu", "sdsugreenlove", "sdsu.gwc", "sdsugirlup", "sdsuleadandserve", 
             "sdsu_aitp", "sdsu_eleetcoders", "sdsuapsirho", "cloud9gg", "lftoxy", "muelleresportsmedicine", "sdsugreenlove", "therivesandiego", "leadershipclubofsdsu",
            "pibetaphisdsu", "sdsupanhellenic", "gammaphisdsu", "deltagammasdsu", "thetasdsu", "alphaphisdsu", "kappadeltasdsu", "axosdsu", "sdsuchio", 
            "sstarb0iiii", "taesroy", "luciaaferrato", "2hollis", "buldak_global", "riovaz", "elizabrowne_", "kaniiberry", "ariana_greenblatt", "aimeejaihall", "roblox",
            "joycee.e", "stxlkin", "bhertuy", "pinkpantheress", "heavnlyheavn", "absamahan", "internetgirlmusic", "eyebleachairdyed", "sundaykalogeras", "ihatebixby", 
            "0noahh", "hereisalden", "ashbluegutierrez", "evan.kohli", "1glaive", "ericdoa", "valorant", "1endie", "starfallxo", "starfallxo", "scruff.hb", "re6ce", "svphietran"]
deleted = ["mexican_crystals69", "akpineapple",  "shriyans_vittal", "pippers12344444445", "__xand3rr", "sergio760__", "marcelinesong_", "d_lo411", "__deleted__bhiebefgijhjcbfij", 
           "matt.hulu", "subidowido", "celeste.cartland", "kayydencebellardoo", "audrey.melani_", "sdsuclass_28", "brandongiolzetti", "", "", ""]
deactivated = ["tamsteroof", "kylessim", "mira_gandhi_", "sheldontan24", "nickvsalvatore", "averyhoangg", "mmonicaagil", "sososquali", "josephh.perez", "toren.rogers", "m_vargas619", 
               "andreamalia.b", "kingj4wsh", "justjordanlou", "kaylawnuh__", "brandongiolzetti", "ha_.rry9537", "carranzalaila"]

#add users to my following list
lines = file_following.readlines()
for line in lines:
   line = line.strip()

   if "title" in line:
      _, username = line.split(":", 1)
      username = username.strip(' "\',')
      followingList.append(username)


#add users to my followers list
lines = file_followers.readlines()
for line in lines:
   line = line.strip()

   if "value" in line:
      _, username = line.split(":", 1)
      username = username.strip(' "\',')
      followerList.append(username)

# compare lists (do not mutate while iterating)
notFollowingThemBack = [x for x in followerList if x not in followingList]
notFollowingMeBack = [x for x in followingList if x not in followerList]
interest = [x for x in notFollowingMeBack if x not in okWithNot and x not in deleted and x not in deactivated]

print("Not following them back:")
for x in notFollowingThemBack:
   print(x)

print("---------------------------------------")
print("Not following me back")
for x in notFollowingMeBack:
   print(x)

print("---------------------------------------")
print("Interest:")
for x in interest:
   print(x)

print("---------------------------------------")
print("Amount of followers: " + str(len(followerList)))
print("Amount of following: " + str(len(followingList)-len(deleted)-len(deactivated)))
print("Amount not following them back: " + str(len(notFollowingThemBack)))
print("Amount not following me back: " + str(len(notFollowingMeBack)))
print("Amount of interest: " + str(len(interest)))