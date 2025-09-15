# import os
# import asyncio
# import contextlib
# import logging
# import jwt
# from aiohttp import web, WSMsgType
# import redis.asyncio as redis
#
# logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
# log = logging.getLogger('ws')
#
# WS_SECRET = os.getenv('WS_SECRET', 'your-secret-key')
# REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
# REDIS_LOCATION = os.getenv('REDIS_LOCATION', 'redis')
# REDIS_PORT = os.getenv('REDIS_PORT', '6379')
# REDIS_PASS = os.getenv('REDIS_PASS', None)
# REDIS_URL = '{host}://{location}:{port}/1'.format(host=REDIS_HOST, location=REDIS_LOCATION, port=REDIS_PORT)
# WS_PATH = os.getenv('WS_PATH', '/ws/staff-events')
# WS_REDIS_KEY = os.getenv('WS_REDIS_KEY', 'test')
# WS_POLL_INTERVAL = float(os.getenv('WS_POLL_INTERVAL', '5'))
#
# clients = set()
# r = None
#
#
# async def verify(request):
#     token = request.query.get('token')
#     if not token:
#         return None
#     try:
#         payload = jwt.decode(token, WS_SECRET, algorithms=['HS256'])
#         if not payload.get('is_staff'):
#             return None
#         return payload
#     except Exception as e:
#         log.warning('jwt verify failed: %s', e)
#         return None
#
#
# async def poll_and_send(ws):
#     while not ws.closed:
#         try:
#             val = await r.get(WS_REDIS_KEY)
#             if isinstance(val, (bytes, bytearray)):
#                 data = val.decode('utf-8', errors='ignore')
#             else:
#                 data = '' if val is None else str(val)
#             await ws.send_str(data)
#         except Exception as e:
#             log.exception('poll error: %s', e)
#         await asyncio.sleep(WS_POLL_INTERVAL)
#
#
# async def ws_handler(request):
#     payload = await verify(request)
#     if not payload:
#         return web.Response(status=403)
#     ws = web.WebSocketResponse(heartbeat=30)
#     await ws.prepare(request)
#     clients.add(ws)
#     task = asyncio.create_task(poll_and_send(ws))
#     try:
#         async for msg in ws:
#             if msg.type == WSMsgType.ERROR:
#                 break
#     finally:
#         task.cancel()
#         with contextlib.suppress(asyncio.CancelledError):
#             await task
#         clients.discard(ws)
#     return ws
#
#
# async def on_startup(app):
#     global r
#     r = redis.from_url(REDIS_URL, decode_responses=False)
#     await r.ping()
#     log.info('redis connected: %s', REDIS_URL)
#
#
# async def on_cleanup(app):
#     for ws in list(clients):
#         await ws.close(code=1001, message='server shutdown')
#     if r:
#         await r.aclose()
#
#
# def make_app():
#     app = web.Application()
#     app.router.add_get(WS_PATH, ws_handler)
#     app.on_startup.append(on_startup)
#     app.on_cleanup.append(on_cleanup)
#     return app
#
#
# if __name__ == '__main__':
#     host = os.getenv('WS_HOST', '0.0.0.0')
#     port = int(os.getenv('WS_PORT', '8081'))
#     web.run_app(make_app(), host=host, port=port)
