from arcade_protocol.crypto import (
    sign_score,
    random_32bytes,
)


class GameInterface():

    def __init__(self, contract, player):
        self.contract = contract
        self.player = player

    @staticmethod
    def new_payment_code():
        payment_code = random_32bytes()
        return payment_code

    def confirm_payment(self, payment_code):
        stored_payment_code = self.contract.get_payment_code(
            self.player,
        )
        confirmed = stored_payment_code == payment_code
        error = not confirmed
        return error

    def sign(self, key, score):
        vrs = sign_score(
            key,
            self.contract.address,
            self.contract.game_id,
            self.player,
            score,
        )
        return vrs
