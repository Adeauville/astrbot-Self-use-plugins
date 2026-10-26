from astrbot.api import AstrBot, event, register
from astrbot.api.event import filter, AstrMessageEvent, MessageChain
from astrbot.api.star import Context, Star, register

@register("sid_private", "custom", "管理员专用，群内/sid静默私聊返回，群内无提示", "1.0.0")
class SidPrivate(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("sid")
    async def sid_handler(self, event: AstrMessageEvent):
        # 校验管理员权限
        if not event.is_admin():
            yield event.plain_result("❌ 只有管理员可以执行该指令")
            return

        if event.is_group():
            sid_info = f"""session_id: {event.session_id}
user_id: {event.get_sender_id()}
group_id: {event.get_group_id()}
platform: {event.get_platform_name()}
"""
            # 只私聊发送，群内不输出任何消息
            await event.send_private_msg(event.get_sender_id(), MessageChain(sid_info))
            return
        else:
            # 私聊场景直接返回信息
            ret = f"""session_id: {event.session_id}
user_id: {event.get_sender_id()}
platform: {event.get_platform_name()}
"""
            yield event.plain_result(ret)
