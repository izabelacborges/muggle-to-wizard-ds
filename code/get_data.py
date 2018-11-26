import urllib.request

# list of tuples with book names and links
books = [("hp1_sorcerers-stone", "http://www.glozman.com/TextPages/Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt"), 
         ("hp2_chamber-of-secrets", "http://www.glozman.com/TextPages/Harry%20Potter%202%20-%20Chamber%20of%20Secrets.txt"), 
         ("hp3_prisioner-of-azkaban", "http://www.glozman.com/TextPages/Harry%20Potter%203%20-%20The%20Prisoner%20Of%20Azkaban.txt"), 
         ("hp4_globet-of-fire", "http://www.glozman.com/TextPages/Harry%20Potter%204%20-%20The%20Goblet%20Of%20Fire.txt"), 
         ("hp5_order-of-the-phoenix", "http://www.glozman.com/TextPages/Harry%20Potter%205%20-%20Order%20of%20the%20Phoenix.txt"), 
         ("hp6_half-blood-prince", "http://www.glozman.com/TextPages/Harry%20Potter%206%20-%20The%20Half%20Blood%20Prince.txt"), 
         ("hp7_deathly-hallows", "http://www.glozman.com/TextPages/Harry%20Potter%207%20-%20Deathly%20Hollows.txt")]

for name, url in books:
    urllib.request.urlretrieve(url, './data/{}.txt'.format(name))
    print("Downloaded '{}' to 'data/' folder.".format(name))
