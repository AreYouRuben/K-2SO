from instapy import InstaPy

insta_username = 'user'
insta_password = 'password'
likes = 5
adm1Ig = 'adm1Ig'
adm2Ig = 'adm2Ig'
swIg = 'starwars'
mandalorianIg = 'themandalorian'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()


# set up all the settings
#session.set_relationship_bounds(enabled=True, potency_ratio=-1.21, delimit_by_numbers=True, max_followers=5, max_following=5, min_followers=2, min_following=1)
#session.set_do_comment(False, percentage=10)
#session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
#session.set_dont_include(['friend1', 'friend2', 'friend3'])
#session.set_dont_like(['pizza', 'girl'])

# do the actual liking
#session.like_by_tags(['natgeo', 'world'], amount=likes)

# follow account
#follow_by_list(followlist=[adm1Ig, adm2Ig], times=1, sleep_delay=10000, interact=False)
accs = [mandalorianIg]
session.follow_by_list(accs, times=1, sleep_delay=500, interact=False)


session.end()
