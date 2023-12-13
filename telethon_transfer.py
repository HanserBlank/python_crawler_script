from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
from telethon import events

# 替换为你的 API ID 和 API HASH
api_id = '26296878'
api_hash = 'b4cdd7855f5195e2864eedd852b17e23'
# 替换为你的登录信息
phone_number = '6283846723894'
username = 'mimi8778'

# 替换为你的源频道和目标频道的 ID
source_channel_id = -1001374839099  # 替换为源频道的 ID
target_channel_id = -1001930500682  # 替换为目标频道的 ID
proxy = {'proxy_type': 'socks5', 'addr': 'localhost', 'port': 7890}
# 创建 Telegram 客户端
client = TelegramClient(username, api_id, api_hash, proxy=proxy)


# 登录到 Telegram
print('正在链接')
client.connect()
print('链接结束')
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

# 定义事件处理函数
@client.on(events.NewMessage(chats=PeerChannel(source_channel_id)))
async def forward_new_messages(event):
    message = event.message
    # 发送消息到目标频道
    await client.send_message(target_channel_id, message)

# 运行客户端，监听新消息
with client:
    client.run_until_disconnected()
