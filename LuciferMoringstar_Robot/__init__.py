from .Utils import (
   get_filter_results,
   get_file_details,
   is_subscribed,
   get_poster,
   Media
)
from .Channel import (
   RATING,
   GENRES
)

HELP = """<b>𝙷𝙴𝚈 {} ,
𝘏𝘦𝘳𝘦 𝘐𝘴 𝘛𝘩𝘦 𝘏𝘦𝘭𝘱 𝘍𝘰𝘳 𝘔𝘺 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴."""

ABOUT ="""
╔════❰ ꪖ᥇ꪮꪊ𝓽 ꪑ𝘴ᧁ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ 𝙈𝙔 𝙉𝘼𝙈𝙀 - <a href="https://t.me/No_Way_Home_bot"> TomHolland </a>
║┣⪼ Ⓓ︎Ⓔ︎Ⓥ︎1 - <a href="https://t.me/PeterParkerspide"> 𝙿𝚎𝚝𝚎𝚛ᵖᵃʳᵏᵉʳ </a>
║┣⪼ 𝓛𝓲𝓫𝓻𝓪𝓻𝓻𝔂 - 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
║┣⪼ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 - 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
║┣⪼ 𝓓𝓪𝓽𝓪 𝓑𝓪𝓼𝓮 - 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
║┣⪼ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻 -  𝙷𝙴𝚁𝙾𝙺𝚄
║┣⪼ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼 - v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪"""

RULES = """<b>𝙷𝙴𝚈 {message.from_user.mention},
𝘏𝘦𝘳𝘦 𝘐𝘴 𝘛𝘩𝘦 RULES 𝘍𝘰𝘳 𝘔𝘺 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴."""

    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

