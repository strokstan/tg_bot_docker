# Image
FROM python:3.9
# Copy files to a container
ADD . /tg_bot
# Installation of pip libraries
RUN pip install -r /tg_bot/requirements.txt
# Start the bot
CMD ["python", "/tg_bot/tg_bot_main.py"]