import asyncio,os,socket,subprocess,sys,time
from pathlib import Path
import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

def test_http_protocol():
    root=Path(__file__).resolve().parents[1]
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
    env=dict(os.environ,COURSE_ROOT=str(root),PYTHONPATH=str(root),MCP_PORT=str(port))
    options={'creationflags':subprocess.CREATE_NO_WINDOW} if os.name=='nt' else {}
    process=subprocess.Popen([sys.executable,'-m','dcom_mcp.server','--http'],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,**options)
    try:
        url=f'http://127.0.0.1:{port}/mcp'
        deadline=time.monotonic()+30
        while True:
            try:
                httpx.get(url,timeout=.5);break
            except httpx.TransportError:
                if time.monotonic()>deadline:raise AssertionError('HTTP server did not start')
                time.sleep(.1)
        async def run():
            async with streamable_http_client(url) as (read,write,_):
                async with ClientSession(read,write) as session:
                    await session.initialize()
                    response=await session.call_tool('list_chapters',{})
                    assert not response.isError and 'Introduction' in response.content[0].text
        asyncio.run(run())
    finally:
        process.terminate();process.wait(timeout=10)
