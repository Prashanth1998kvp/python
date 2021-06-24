import instaloader
ig=instaloader.Instaloader()
pic=input("enter username :")
ig.download_profile(pic,profile_pic_only=True)
