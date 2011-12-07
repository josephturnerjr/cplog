import cplog

# Will print
cplog.log("Hey 1", 0)
# Won't print
cplog.log("Hey 2", 1)
cplog.log("Hey 3", 2)
cplog.echo_to_screen(False)
# won't print
cplog.log("Hey 4", 0)
cplog.echo_to_screen(True)
cplog.set_loglevel(5)
# Will print
cplog.log("Hey 5", 1)
cplog.log("Hey 6", 2)
cplog.set_loglevel(getattr(cplog, "notice"))
# Will
cplog.log("Hey 7", 2)
# Won't
cplog.log("Hey 8", 3)
