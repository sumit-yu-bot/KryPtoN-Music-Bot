HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID", "17221046"])
    API_HASH = environ["API_HASH", "233ef51a2c05a3979f95d7c7730cf320"]
    SUDO_CHAT_ID = environ["SUDO_CHAT_ID", "2139088940"]
    SESSION_STRING = environ["SESSION_STRING","BQBa1twSr7GwBqVgA2cdxK4xnt8zTSoYuPvmch0HQ-KgmEbn238U6Dhv0XDubJU5YSbL9FcDRRE10J3ivyD6NBUHlIZQpBmOtrEY4iKD1qLcpyLzFEwRgaGD4ydKxZLDYqMyw6PQc69SvQl1HbYGH4s5qNY6Cp2b780mFaXXtD-NG-oG76ca5kh3tSAEA_3CibOKOgho0hR-D0vjOjZecMd71kVfj2-U3I9TG4vv0zwJHTdQwUtNF5I-qfuDQmsgZ81A8G5pqjEG9rD7WLzQUMOpatLbwHLPJ3_ELOo05AFpK-Mebg5xGq41ScsjI0Rp-eP_RJCBFLuvMwkh-_nCx3a-AAAAAUqDigcA"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 123456
    API_HASH = "asdnsfkj1412kjh4"
    SUDO_CHAT_ID = "12304"


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
