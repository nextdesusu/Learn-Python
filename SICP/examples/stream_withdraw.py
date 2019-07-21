def stream_withdraw(balance, amount_stream):
    yield balance
    for amount in amount_stream:
        yield balance - amount