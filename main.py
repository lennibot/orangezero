import Orange0

if __name__ == '__main__':
    """
    At the moment all this script does it check, update, and verify the current version of Paper.
    Eventually this main script will spawn several subprocesses that handle the various needs of a Minecraft Server.
    """
    orange0 = Orange0

    orange0.check_version()
    print('thread check')
