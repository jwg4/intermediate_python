import sys

# txRedis - Redis client for twisted.
# https://github.com/deldotdr/txRedis/blob/master/examples/pubsub.py

from twisted.internet import reactor, protocol, defer
from twisted.python import log

from txredis.client import RedisClient, RedisSubscriber

REDIS_HOST = 'localhost'
REDIS_PORT = 6379


def getRedisSubscriber():
    clientCreator = protocol.ClientCreator(reactor, RedisSubscriber)
    return clientCreator.connectTCP(REDIS_HOST, REDIS_PORT)


def getRedis():
    clientCreator = protocol.ClientCreator(reactor, RedisClient)
    return clientCreator.connectTCP(REDIS_HOST, REDIS_PORT)


@defer.inlineCallbacks
def runTest():
    redis1 = yield getRedisSubscriber()
    redis2 = yield getRedis()

    log.msg("redis1: SUBSCRIBE w00t")
    response = yield redis1.subscribe("w00t")
    log.msg("subscribed to w00t, response = %r" % response)

    log.msg("redis2: PUBLISH w00t 'Hello, world!'")
    response = yield redis2.publish("w00t", "Hello, world!")
    log.msg("published to w00t, response = %r" % response)

    reactor.stop()


def main():
    log.startLogging(sys.stdout)
    reactor.callLater(0, runTest)
    reactor.run()


if __name__ == "__main__":
    main()
