class AntiSpamInvites(object):
    def __init__(self, config):
        self._blocked_homeservers = config.get("blocked_homeservers", [])

    def check_event_for_spam(self, event):
        return False # allowed

    def user_may_invite(self, inviter_user_id, invitee_user_id, room_id):
        for bad_hs in self._blocked_homeservers:
            if inviter_user_id.endswith(":" + bad_hs):
                return False # not allowed
        return True # allowed

    def user_may_create_room(self, user_id):
        return True # allowed

    def user_may_create_room_alias(self, user_id, room_alias):
        return True # allowed

    def user_may_publish_room(self, user_id, room_id):
        return True # allowed

    @staticmethod
    def parse_config(config):
        return config # no parsing needed
